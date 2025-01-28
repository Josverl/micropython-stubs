# This file is part of the se05x package.
# Copyright (c) 2024 Arduino SA
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
# An implementation of ISO7816-3/4 standards.
import struct
import logging
from micropython import const
from time import sleep

# PCB bits
_NAD_OFFSET = 0
_PCB_OFFSET = 1
_LEN_OFFSET = 2
_INF_OFFSET = 3

# Blocks
_I_BLOCK = 0x00
_I_BLOCK_N = 6
_I_BLOCK_M = 5

_S_BLOCK = 0xC0
_S_BLOCK_REQ = 0x3F

_R_BLOCK = 0x80
_R_BLOCK_N = 4
_R_BLOCK_ERR = 0x03

# S-Block request/response
_RESYNC_REQ = 0x00
_IFS_REQ = 0x01
_ABORT_REQ = 0x02
_WTX_REQ = 0x03
_END_SESSION_REQ = 0x05
_CHIP_RESET_REQ = 0x06
_GET_ATR_REQ = 0x07
_SOFT_RESET_REQ = 0x0F

_CLA_ISO7816 = 0x00
_INS_GP_SELECT = 0xA4

_STATE_IBLK = 0
_STATE_SBLK = 1
_STATE_SEND = 2
_STATE_RECV = 3
_STATE_WAIT = 4
_STATE_WWTX = 5
_STATE_DONE = 6


def log_enabled(level):
    return logging.getLogger().isEnabledFor(level)


class SmartCard:
    def __init__(self, bus, nad, aid):
        self.seq = 0
        self.bus = bus
        self.sad = nad & 0xF0
        self.dad = nad & 0x0F
        self.aid = aid
        self.atr = None

        # TODO: Optimize these
        self.w_buf = memoryview(bytearray(512))
        self.r_buf = memoryview(bytearray(512))
        self.s_buf = memoryview(bytearray(32))
        self.apdu_buf = memoryview(bytearray(512))

        self.block_name = {_I_BLOCK: "I-Block", _R_BLOCK: "R-Block", _S_BLOCK: "S-Block"}
        self.state_name = {
            _STATE_IBLK: "IBLK",
            _STATE_SBLK: "SBLK",
            _STATE_SEND: "SEND",
            _STATE_RECV: "RECV",
            _STATE_WAIT: "WAIT",
            _STATE_WWTX: "WWTX",
            _STATE_DONE: "DONE",
        }
        self.apdu_status = {
            0x6700: "Wrong length",
            0x6985: "Conditions not satisfied",
            0x6982: "Security status not satisfied",
            0x6A80: "Wrong data",
            0x6984: "Data invalid",
            0x6986: "Command not allowed",
            0x6A82: "File not found",
            0x6A84: "File full",
            0x6D00: "Invalid or not supported instruction code.",
        }

    def _block_type(self, pcb):
        return _I_BLOCK if pcb & 0x80 == 0 else pcb & 0xC0

    def _block_size(self, buf):
        # NAD, PCB, LEN, INF[LEN], CRC[2]
        return 3 + buf[_LEN_OFFSET] + 2

    def _block_crc16(self, prologue, data, poly=0x8408, crc=0xFFFF):
        # Calculate prologue checksum
        for i in prologue:
            crc ^= i
            for bit in range(8):
                crc = (crc >> 1) ^ poly if crc & 0x1 else crc >> 1

        # Calculate data checksum
        for i in data:
            crc ^= i
            for bit in range(8):
                crc = (crc >> 1) ^ poly if crc & 0x1 else crc >> 1
        crc ^= 0xFFFF
        return ((crc & 0xFF) << 8) | ((crc >> 8) & 0xFF)

    def _block_write(self, buf, delay=0):
        size = self._block_size(buf)
        self.bus.write(buf[0:size])

    def _block_print(self, txrx, *args):
        if len(args) == 1:
            buf = args[0]
            nad, pcb, bsize = buf[_NAD_OFFSET : _LEN_OFFSET + 1]
            crc = buf[_LEN_OFFSET + bsize + 1] << 8 | buf[_LEN_OFFSET + bsize + 2]
        else:
            nad, pcb, bsize, crc, buf = args
        btype = self._block_type(pcb)
        bname = self.block_name[btype]
        boffs = _INF_OFFSET if len(args) == 1 else 0
        seq = (pcb >> _I_BLOCK_N) & 1 if btype == _I_BLOCK else (pcb >> _R_BLOCK_N) & 1
        if log_enabled(logging.DEBUG):
            logging.debug(f"{'Tx' if txrx else 'Rx'}: {bname} NAD: 0x{nad:X} " f"PCB: 0x{pcb:X} LEN: {bsize} SEQ: {seq} CRC: 0x{crc:X}")
            buf_hex = "".join(f"{b:02X}" for b in buf[boffs : boffs + bsize])
            logging.debug(f"RAW: {nad:02X}{pcb:02X}{bsize:02X}{buf_hex}{crc:04X}")

    def _block_new(self, buf, btype, **kwargs):
        data = kwargs.get("data", None)
        bsize = 0 if data is None else len(data)
        buf[_NAD_OFFSET] = self.sad | self.dad
        buf[_PCB_OFFSET] = btype
        buf[_LEN_OFFSET] = bsize
        if btype == _S_BLOCK:
            buf[_PCB_OFFSET] |= kwargs["request"]
        elif btype == _I_BLOCK:
            buf[_PCB_OFFSET] |= self.seq << _I_BLOCK_N
            buf[_PCB_OFFSET] |= kwargs["chained"] << _I_BLOCK_M
        elif btype == _R_BLOCK:
            buf[_PCB_OFFSET] |= self.seq << _R_BLOCK_N
            buf[_PCB_OFFSET] |= kwargs["error"] & _R_BLOCK_ERR
        if bsize:
            buf[_INF_OFFSET : _INF_OFFSET + bsize] = data
        # Calculate and set CRC
        crc = self._block_crc16(buf[0:_INF_OFFSET], buf[_INF_OFFSET : _INF_OFFSET + bsize])
        buf[_LEN_OFFSET + bsize + 1] = (crc >> 8) & 0xFF
        buf[_LEN_OFFSET + bsize + 2] = (crc >> 0) & 0xFF
        # Toggle I-Block sequence
        if btype == _I_BLOCK:
            self.seq = self.seq ^ 1
        return buf

    def _send_block(self, btype, arg, retry=25, backoff=1.2):
        r_offs = 0
        w_offs = 0
        retry_delay = 1 / 1000
        next_state = _STATE_SBLK if btype == _S_BLOCK else _STATE_IBLK

        while retry:
            if log_enabled(logging.DEBUG):
                logging.debug(f"STATE: {self.state_name[next_state]} retry: {retry}")
            if next_state == _STATE_SBLK:
                next_state = _STATE_SEND
                prev_state = _STATE_RECV
                block = self._block_new(self.w_buf, _S_BLOCK, request=arg)
            elif next_state == _STATE_IBLK:
                next_state = _STATE_SEND
                prev_state = _STATE_RECV
                remain = len(arg) - w_offs
                bsize = min(remain, self.atr["IFSC"])
                chained = int(remain > self.atr["IFSC"])
                block = self._block_new(self.w_buf, _I_BLOCK, chained=chained, data=arg[w_offs : w_offs + bsize])
                w_offs += bsize
            elif next_state == _STATE_SEND:
                try:
                    self._block_write(block)
                    next_state = prev_state
                    if log_enabled(logging.DEBUG):
                        self._block_print(True, block)
                except Exception:
                    retry -= 1
            elif next_state == _STATE_RECV:
                try:
                    # Read NAD, PCB, LEN, information (if present) and CRC.
                    nad, pcb, bsize = self.bus.read(self.s_buf[0:3])
                    if bsize:
                        self.bus.read(self.r_buf[r_offs : r_offs + bsize])
                    crc = int.from_bytes(self.bus.read(self.s_buf[3:5]), "big")
                except Exception:
                    retry -= 1
                    next_state = _STATE_WAIT
                    prev_state = _STATE_RECV
                    continue

                # Check NAD and CRC.
                exp = self._block_crc16(self.s_buf[0:3], self.r_buf[r_offs : r_offs + bsize])
                if nad != (self.sad >> 4) | (self.dad << 4) or crc != exp:
                    retry -= 1
                    next_state = _STATE_SEND
                    prev_state = _STATE_RECV
                    block = self._block_new(self.s_buf, _R_BLOCK, error=1)
                    continue

                if log_enabled(logging.DEBUG):
                    self._block_print(False, nad, pcb, bsize, crc, self.r_buf[r_offs : r_offs + bsize])

                # Process block.
                btype = self._block_type(pcb)
                if btype == _R_BLOCK:
                    # Retransmit last block if error, or continue block chain.
                    next_state = _STATE_SEND if pcb & _R_BLOCK_ERR else _STATE_IBLK
                    prev_state = _STATE_RECV
                    continue

                if btype == _I_BLOCK:
                    # Acknowledge I-Block in block chain with R(N(R)).
                    if pcb & (1 << _I_BLOCK_M):
                        next_state = _STATE_SEND
                        prev_state = _STATE_RECV
                        block = self._block_new(self.s_buf, _R_BLOCK, error=0)
                    else:
                        next_state = _STATE_DONE
                    # Add current I-Block INF size (could be 0).
                    r_offs += bsize
                    continue

                if btype == _S_BLOCK:
                    if pcb & _S_BLOCK_REQ == _RESYNC_REQ:
                        # Respond to a resync request.
                        self.seq = 0
                        next_state = _STATE_SEND
                        prev_state = _STATE_RECV
                        block = self._block_new(self.s_buf, _S_BLOCK, request=_RESYNC_REQ & 0x20)
                    elif pcb & _S_BLOCK_REQ == _WTX_REQ:
                        # Respond to a WTX request.
                        next_state = _STATE_SEND
                        prev_state = _STATE_WWTX
                        wtx_delay = self.r_buf[r_offs] * self.atr["BWT"] / 1000
                        block = self._block_new(self.s_buf, _S_BLOCK, request=_WTX_REQ & 0x20)
                    else:
                        # Add current S-Block INF size (could be 0).
                        r_offs += bsize
                        next_state = _STATE_DONE
                    continue
            elif next_state == _STATE_WWTX:
                sleep(wtx_delay)
                next_state = _STATE_RECV
            elif next_state == _STATE_WAIT:
                sleep(retry_delay)
                retry_delay *= backoff
                next_state = prev_state
            elif next_state == _STATE_DONE:
                return self.r_buf[0:r_offs]

        if retry == 0:
            raise RuntimeError("_send_block failed")

    def send_apdu(self, cla, ins, p1, p2, data=None, le=0):
        size = 4
        self.apdu_buf[0] = cla
        self.apdu_buf[1] = ins
        self.apdu_buf[2] = p1
        self.apdu_buf[3] = p2
        if data is not None:
            size = len(data)
            self.apdu_buf[4] = size
            self.apdu_buf[5 : 5 + size] = data
            self.apdu_buf[5 + size] = 0x00
            size += 5

        # Send APDU in I-Block
        resp = self._send_block(_I_BLOCK, self.apdu_buf[0:size])

        # Check response TPDU status
        status = int.from_bytes(resp[-2:], "big")
        if status != 0x9000:
            raise RuntimeError("APDU Error: " + self.apdu_status.get(status, f"Unknown 0x{status:X}"))

        # Return data bytes, if any, or the status.
        if len(resp) == 2:
            return status
        return resp[2 + (0 if resp[1] <= 0x7F else resp[1] & 0x0F) : -2]

    def reset(self):
        self.seq = 0
        atr_raw = self._send_block(_S_BLOCK, _SOFT_RESET_REQ)
        if self.atr is None:
            self.atr = self._parse_atrs(atr_raw)
            if log_enabled(logging.INFO):
                self._dump_atrs(self.atr)
        # Select applet
        self.send_apdu(_CLA_ISO7816, _INS_GP_SELECT, 0x04, 0x00, self.aid, le=True)

    def resync(self):
        self._send_block(_S_BLOCK, _RESYNC_REQ)
        self.seq = 0

    def _parse_atrs(self, atr_bytes):
        atr = {}
        # PVER - 1 byte
        atr["PVER"] = atr_bytes[0]
        # VID - 5 bytes
        atr["VID"] = atr_bytes[1:6].hex().upper()

        # Length of DLLP - 1 byte
        dllp_length = atr_bytes[6]
        atr["DLLP_LENGTH"] = dllp_length

        # DLLP - Variable length (Decode using struct)
        dllp = atr_bytes[7 : 7 + dllp_length]
        atr["DLLP"] = dllp.hex().upper()
        if dllp_length >= 4:
            atr["BWT"], atr["IFSC"] = struct.unpack(">HH", dllp[:4])

        # PLID - 1 byte
        atr["PLID"] = atr_bytes[7 + dllp_length]
        # Length of PLP - 1 byte
        plp_length = atr_bytes[8 + dllp_length]
        atr["PLP_LENGTH"] = plp_length

        # PLP - Variable length (Decode using struct)
        plp = atr_bytes[9 + dllp_length : 9 + dllp_length + plp_length]
        atr["PLP"] = plp.hex().upper()
        if plp_length >= 2:
            atr["MCF"] = struct.unpack(">H", plp[:2])[0]
        if plp_length >= 3:
            atr["CONFIGURATION"] = plp[2]
        if plp_length >= 4:
            atr["MPOT"] = plp[3]
        if plp_length >= 6:
            atr["SEGT"], atr["WUT"] = struct.unpack(">HH", plp[4:8])

        # Length of HB - 1 byte
        hb_length = atr_bytes[9 + dllp_length + plp_length]
        atr["HB_LENGTH"] = hb_length
        # HB - Variable length
        hb = atr_bytes[10 + dllp_length + plp_length : 10 + dllp_length + plp_length + hb_length]
        atr["HB"] = hb.hex().upper()
        return atr

    def _dump_atrs(self, atr):
        logging.info(f"PVER (Protocol Version): {atr['PVER']}")
        logging.info(f"VID (Vendor ID): {atr['VID']}")
        logging.info(f"Length of DLLP: {atr['DLLP_LENGTH']}")

        if "DLLP" in atr:
            logging.info(f"DLLP: {atr['DLLP']}")

        if "BWT" in atr and "IFSC" in atr:
            logging.info(f"BWT (Block Waiting Time): {atr['BWT']} ms")
            logging.info(f"IFSC (Maximum Information Field Size): {atr['IFSC']} bytes")

        logging.info(f"PLID (Physical Layer ID): {atr['PLID']}")
        logging.info(f"Length of PLP: {atr['PLP_LENGTH']}")

        if "PLP" in atr:
            logging.info(f"PLP: {atr['PLP']}")

        if "MCF" in atr:
            logging.info(f"MCF (Max I2C Clock Frequency): {atr['MCF']} kHz")

        if "CONFIGURATION" in atr:
            logging.info(f"Configuration: {atr['CONFIGURATION']:#04x}")

        if "MPOT" in atr:
            logging.info(f"MPOT (Minimum Polling Time): {atr['MPOT']} ms")

        if "SEGT" in atr and "WUT" in atr:
            logging.info(f"SEGT (Secure Element Guard Time): {atr['SEGT']} µs")
            logging.info(f"WUT (Wake-Up Time): {atr['WUT']} µs")

        logging.info(f"Length of HB (Historical Bytes): {atr['HB_LENGTH']}")
        if "HB" in atr:
            logging.info(f"HB (Historical Bytes): {atr['HB']}")
