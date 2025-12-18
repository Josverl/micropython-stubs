# This file is part of the se05x package.
# Copyright (c) 2024 Arduino SA
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
# NXP SE05x EdgeLock device driver.

import struct
import logging
from time import sleep_ms
from machine import I2C
from machine import Pin
from .iso7816 import SmartCard
from micropython import const

_RESULT_OK = 1
_APPLET_NAD = 0x5A
_APPLET_AID = const(b"\xa0\x00\x00\x03\x96\x54\x53\x00\x00\x00\x01\x03\x00\x00\x00\x00")
_CLA_KSE05X = 0x80

_INS_WRITE = 0x01
_INS_READ = 0x02
_INS_CRYPTO = 0x03
_INS_MGMT = 0x04
_INS_PROCESS = 0x05
_INS_IMPORT_EXTERNAL = 0x06
_INS_TRANSIENT = 0x80
_INS_AUTH_OBJECT = 0x40
_INS_ATTEST = 0x20

_P1_DEFAULT = 0x00
_P1_EC = 0x01
_P1_AES = 0x03
_P1_DES = 0x04
_P1_HMAC = 0x05
_P1_BINARY = 0x06
_P1_USERID = 0x07
_P1_CURVE = 0x0B
_P1_SIGNATURE = 0x0C
_P1_MAC = 0x0D
_P1_CIPHER = 0x0E
_P1_KEY_PRIVATE = 0x40
_P1_KEY_PUBLIC = 0x20

_P2_DEFAULT = 0x00
_P2_GENERATE = 0x03
_P2_CREATE = 0x04
_P2_SIZE = 0x07
_P2_SIGN = 0x09
_P2_VERIFY = 0x0A
_P2_SESSION_CREATE = 0x1B
_P2_SESSION_CLOSE = 0x1C
_P2_VERSION = 0x20
_P2_LIST = 0x25
_P2_EXIST = 0x27
_P2_DELETE_OBJECT = 0x28
_P2_SESSION_USERID = 0x2C
_P2_DH = 0x0F
_P2_ENCRYPT_ONESHOT = 0x37
_P2_DECRYPT_ONESHOT = 0x38
_P2_SCP = 0x52
_P2_ONESHOT = 0x0E

_TLV_TAG1 = 0x41
_TLV_TAG2 = 0x42
_TLV_TAG3 = 0x43
_TLV_TAG4 = 0x44
_TLV_TAG5 = 0x45
_TLV_TAG6 = 0x46
_TLV_TAG7 = 0x47
_TLV_TAG8 = 0x48
_TLV_TAG9 = 0x49
_TLV_TAG10 = 0x4A
_TLV_TAG11 = 0x4B
_TLV_TAG_SESSION_ID = 0x10
_TLV_TAG_POLICY = 0x11
_TLV_TAG_MAX_ATTEMPTS = 0x12
_TLV_TAG_IMPORT_AUTH_DATA = 0x13
_TLV_TAG_IMPORT_AUTH_KEY_ID = 0x14
_TLV_TAG_POLICY_CHECK = 0x15

_SIG_ECDSA_SHA_1 = 0x11
_SIG_ECDSA_SHA_224 = 0x25
_SIG_ECDSA_SHA_256 = 0x21
_SIG_ECDSA_SHA_384 = 0x22
_SIG_ECDSA_SHA_512 = 0x26


class I2CBus:
    def __init__(self, addr, freq):
        self.addr = addr
        self.bus = None
        # Scan the first 3 I2C buses
        for i in range(3):
            try:
                bus = I2C(i, freq=freq)
                if self.addr in bus.scan():
                    logging.info(f"SE05x detected on bus: {i} addr: 0x{addr:02X}")
                    self.bus = bus
                    break
            except Exception:
                pass
        if self.bus is None:
            raise RuntimeError("Failed to detect SE05x on I2C bus")

    def read(self, buf):
        self.bus.readfrom_into(self.addr, buf)
        return buf

    def write(self, buf):
        self.bus.writeto(self.addr, buf)


class SE05X:
    def __init__(self, addr=0x48, freq=400_000, rst=Pin("SE05X_EN", Pin.OUT_PP, Pin.PULL_UP)):
        self.rst = rst
        self.scard = None
        self.reset()
        self.bus = I2CBus(addr, freq)
        self.scard = SmartCard(self.bus, _APPLET_NAD, _APPLET_AID)
        self.scard.reset()
        self.ecdsa_algo = {
            160: _SIG_ECDSA_SHA_1,
            224: _SIG_ECDSA_SHA_224,
            256: _SIG_ECDSA_SHA_256,
            384: _SIG_ECDSA_SHA_384,
            512: _SIG_ECDSA_SHA_512,
        }
        self.tlv_offs = 0
        self.tlv_buf = memoryview(bytearray(254))

    def _tlv_pack(self, fmt, *args):
        struct.pack_into(fmt, self.tlv_buf, self.tlv_offs, *args)
        self.tlv_offs += struct.calcsize(fmt)

    def _tlv_flush(self):
        mv = self.tlv_buf[0 : self.tlv_offs]
        self.tlv_offs = 0
        return mv

    def _ecdsa_algo(self, hash_size):
        if hash_size * 8 not in self.ecdsa_algo:
            raise ValueError("Invalid SHA digest size")
        return self.ecdsa_algo[hash_size * 8]

    def reset(self, reset_card=True):
        self.rst.low()
        sleep_ms(10)
        self.rst.high()
        sleep_ms(10)
        if self.scard is not None:
            self.scard.reset()

    def version(self):
        resp = self.scard.send_apdu(_CLA_KSE05X, _INS_MGMT, _P1_DEFAULT, _P2_VERSION)
        major, minor, patch = struct.unpack(">BBB", resp)
        return major, minor, patch

    def read(self, obj_id, size=0):
        if not self.exists(obj_id):
            raise RuntimeError(f"Object with id 0x{obj_id:X} doesn't exist.")
        if size == 0:
            self._tlv_pack(">BBI", _TLV_TAG1, 0x4, obj_id)
            resp = self.scard.send_apdu(_CLA_KSE05X, _INS_READ, _P1_DEFAULT, _P2_DEFAULT, self._tlv_flush())
            return bytes(resp)
        offset = 0
        buf = bytearray()
        maxblk = 254 - struct.calcsize("BBIBBHBBH")
        while size:
            bsize = min(size, maxblk)
            self._tlv_pack(">BBI", _TLV_TAG1, 0x4, obj_id)
            self._tlv_pack(">BBH", _TLV_TAG2, 0x2, offset)
            self._tlv_pack(">BBH", _TLV_TAG3, 0x2, bsize)
            resp = self.scard.send_apdu(_CLA_KSE05X, _INS_READ, _P1_DEFAULT, _P2_DEFAULT, self._tlv_flush())
            buf.extend(resp)
            offset += bsize
            size -= bsize
        return bytes(buf)

    def write(self, obj_id, obj_type, **kwargs):
        if self.exists(obj_id):
            raise RuntimeError(f"Object with id 0x{obj_id:X} already exists.")

        ins = _INS_WRITE | kwargs.get("ins_flags", 0)
        if obj_type == _P1_EC:
            p1 = _P1_EC
            key = kwargs.get("key", (None, None))
            curve_id = kwargs.get("curve", 0x3)
            self._tlv_pack(">BBI", _TLV_TAG1, 0x4, obj_id)
            self._tlv_pack(">BBB", _TLV_TAG2, 0x1, curve_id)
            if key[0] is not None:
                p1 |= _P1_KEY_PRIVATE
                self._tlv_pack(f"BB{len(key[0])}s", _TLV_TAG3, len(key[0]), key[0])
            if key[1] is not None:
                p1 |= _P1_KEY_PUBLIC
                self._tlv_pack(f"BB{len(key[1])}s", _TLV_TAG4, len(key[1]), key[1])
            if key[0] is None and key[1] is None:
                p1 |= _P1_KEY_PRIVATE | _P1_KEY_PUBLIC
            self.scard.send_apdu(_CLA_KSE05X, ins, p1, _P2_DEFAULT, self._tlv_flush())
        elif obj_type == _P1_BINARY:
            offset = 0
            binary = kwargs["binary"]
            maxblk = 254 - struct.calcsize("BBIBBHBBHBBH")
            remain = len(binary)
            while remain:
                bsize = min(remain, maxblk)
                data = binary[offset : offset + bsize]
                self._tlv_pack(">BBI", _TLV_TAG1, 0x4, obj_id)
                self._tlv_pack(">BBH", _TLV_TAG2, 0x2, offset)
                if offset == 0:
                    self._tlv_pack(">BBH", _TLV_TAG3, 0x2, remain)
                self._tlv_pack(f">BBH{bsize}s", _TLV_TAG4, 0x82, bsize, data)
                self.scard.send_apdu(_CLA_KSE05X, ins, _P1_BINARY, _P2_DEFAULT, self._tlv_flush())
                offset += bsize
                remain -= bsize

    def delete(self, obj_id):
        if not self.exists(obj_id):
            raise RuntimeError(f"Object with id 0x{obj_id:X} doesn't exist.")
        self._tlv_pack(">BBI", _TLV_TAG1, 0x4, obj_id)
        self.scard.send_apdu(_CLA_KSE05X, _INS_MGMT, _P1_DEFAULT, _P2_DELETE_OBJECT, self._tlv_flush())

    def exists(self, obj_id):
        self._tlv_pack(">BBI", _TLV_TAG1, 0x4, obj_id)
        resp = self.scard.send_apdu(_CLA_KSE05X, _INS_MGMT, _P1_DEFAULT, _P2_EXIST, self._tlv_flush())
        return resp[0] == _RESULT_OK

    def sign(self, obj_id, data):
        if not self.exists(obj_id):
            raise RuntimeError(f"Object with id 0x{obj_id:X} doesn't exist.")
        hash_size = len(data)
        hash_algo = self._ecdsa_algo(hash_size)
        self._tlv_pack(">BBIBBB", _TLV_TAG1, 0x4, obj_id, _TLV_TAG2, 0x1, hash_algo)
        self._tlv_pack(f"BB{hash_size}s", _TLV_TAG3, hash_size, data)
        resp = self.scard.send_apdu(_CLA_KSE05X, _INS_CRYPTO, _P1_SIGNATURE, _P2_SIGN, self._tlv_flush())
        return bytes(resp)

    def verify(self, obj_id, data, sign):
        if not self.exists(obj_id):
            raise RuntimeError(f"Object with id 0x{obj_id:X} doesn't exist.")
        hash_size = len(data)
        sign_size = len(sign)
        hash_algo = self._ecdsa_algo(hash_size)
        self._tlv_pack(">BBI", _TLV_TAG1, 0x4, obj_id)
        self._tlv_pack(">BBB", _TLV_TAG2, 0x1, hash_algo)
        self._tlv_pack(f"BB{hash_size}s", _TLV_TAG3, hash_size, data)
        self._tlv_pack(f"BB{sign_size}s", _TLV_TAG5, sign_size, sign)
        resp = self.scard.send_apdu(_CLA_KSE05X, _INS_CRYPTO, _P1_SIGNATURE, _P2_VERIFY, self._tlv_flush())
        return resp[0] == _RESULT_OK
