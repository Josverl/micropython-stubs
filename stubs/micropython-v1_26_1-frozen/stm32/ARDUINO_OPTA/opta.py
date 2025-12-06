# This file is part of the blueprint package.
# Copyright (c) 2024 Arduino SA
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import struct
import logging
from time import sleep_ms
from machine import I2C
from machine import Pin
from micropython import const

_MIN_ADDRESS = 0x0B
_TMP_ADDRESS = 0x0A
_MAX_ADDRESS = const(0x0B + 0x0A)

# Header and CRC length.
_CMD_HDR_LEN = 0x03
_CMD_CRC_LEN = 0x01

# Command direction (SET == 1, GET == 2)
_CMD_DIR_SET = 0x01
_CMD_DIR_GET = 0x02

# Commands are encoded as follows:
# [direction, command opcode, response length, ack required]
_CMD_CHIP_RESET = (_CMD_DIR_SET, 0x01, 0, False)
_CMD_SET_ADDRESS = (_CMD_DIR_SET, 0x02, 0, False)
_CMD_GET_ADDRESS = (_CMD_DIR_GET, 0x03, 2, False)

# Misc commands such as product ID, firmware etc...
_CMD_GET_PRODUCT_ID = (_CMD_DIR_GET, 0x25, 33, False)
_CMD_GET_FW_VERSION = (_CMD_DIR_GET, 0x16, 3, False)
_CMD_SET_BOOTLOADER = (_CMD_DIR_SET, 0xF3, 0, False)

# Flash commands.
_CMD_SET_FLASH_WRITE = (_CMD_DIR_SET, 0x17, 0, False)
_CMD_GET_FLASH_READ = (_CMD_DIR_GET, 0x18, 32, False)

# Digital pins commands.
_CMD_SET_DIGITAL_PIN = (_CMD_DIR_SET, 0x06, 0, False)
_CMD_GET_DIGITAL_BUS = (_CMD_DIR_GET, 0x04, 2, False)
_CMD_SET_DIGITAL_DEF = (_CMD_DIR_SET, 0x08, 0, False)
_CMD_SET_DIGITAL_BUS_OA = (_CMD_DIR_SET, 0x15, 0, True)

# Analog channels commands.
_CMD_CFG_ANALOG_ADC = (_CMD_DIR_SET, 0x09, 0, True)
_CMD_CFG_ANALOG_DIN = (_CMD_DIR_SET, 0x11, 0, True)
_CMD_CFG_ANALOG_PWM = (_CMD_DIR_SET, 0x13, 0, True)
_CMD_CFG_ANALOG_DAC = (_CMD_DIR_SET, 0x0C, 0, True)
_CMD_CFG_ANALOG_RTD = (_CMD_DIR_SET, 0x0E, 0, True)
_CMD_CFG_ANALOG_HIZ = (_CMD_DIR_SET, 0x24, 0, True)
_CMD_SET_ANALOG_DAC = (_CMD_DIR_SET, 0x0D, 0, True)
_CMD_SET_ANALOG_RTD_TIM = (_CMD_DIR_SET, 0x10, 0, True)

# Read analog channels (Analog pin, ADC, RTD, Digital In)
_CMD_GET_ANALOG_PIN = (_CMD_DIR_GET, 0x05, 2, False)
_CMD_GET_ANALOG_PIN_ALL = (_CMD_DIR_GET, 0x07, 32, False)
_CMD_GET_ANALOG_ADC = (_CMD_DIR_GET, 0x0A, 3, False)
_CMD_GET_ANALOG_ADC_ALL = (_CMD_DIR_GET, 0x0B, 16, False)
_CMD_GET_ANALOG_RTD = (_CMD_DIR_GET, 0x0F, 5, False)
_CMD_GET_ANALOG_DIN = (_CMD_DIR_GET, 0x12, 1, False)

# Default analog channels values and timeout.
_CMD_SET_ANALOG_PWM_DEF = (_CMD_DIR_SET, 0x33, 0, True)
_CMD_SET_ANALOG_DAC_DEF = (_CMD_DIR_SET, 0x3D, 0, True)
_CMD_SET_ANALOG_TIMEOUT = (_CMD_DIR_SET, 0x31, 0, True)

_CHANNEL_MODES = (None, "voltage", "current")
_CHANNEL_TYPES = ("adc", "dac", "rtd", "pwm", "hiz", "din")


class Expansion:
    def __init__(self, opta, type, addr, name):
        self.opta = opta
        self.type = type
        self.addr = addr
        self.name = name
        self.channels = {}

    def product_id(self):
        """
        Returns the product ID bytes of the expansion.
        """
        return self.opta._cmd(self.addr, _CMD_GET_PRODUCT_ID)

    def firmware_version(self):
        """
        Returns the firmware version of the expansion.
        """
        return self.opta._cmd(self.addr, _CMD_GET_FW_VERSION)

    def _flash(self, address, size=0, data=None):
        """
        Reads from or writes to the flash memory at the specified address.

        NOTE: This should be used for production purposes only!

        Parameters:
            - address : The memory address to read from or write to.
            - size : Number of bytes to read from the flash memory.
            - data : Bytes to write to the flash memory.

        Returns:
            Data read from the flash memory as bytes, if reading. Returns None if writing.
        """
        size = size if data is None else len(data)
        if size < 0 or size > 32:
            raise RuntimeError("Maximum flash read/write size is 32")
        if data is None:
            resp = self.opta._cmd(self.addr, _CMD_GET_FLASH_READ, "<HB", address, size)
            return struct.unpack("<HB32s", resp)[-1][0:size]
        self.opta._cmd(self.addr, _CMD_SET_FLASH_WRITE, f"<HB{size}s", address, size, data)

    def digital(self, pins=None, timeout=None, default=0):
        """
        Reads or writes digital pins.

        Parameters:
            - pins : Digital pins mask to set. If None, returns the state of all pins.
            - timeout : The timeout in milliseconds, after which pins revert to the default state.
            - default : The default state to which the pins will revert to after the timeout expires.

        Note:
            - For Opta Analog, this functions supports writing digital LEDs only.

        Returns: The current state of the digital pins if reading, or None if setting the pins.
        """
        if self.type == "analog":
            if pins is None:
                raise RuntimeError("Function is not supported on analog expansions")
            return self.opta._cmd(self.addr, _CMD_SET_DIGITAL_BUS_OA, "B", pins)
        if pins is None and timeout is None:
            return struct.unpack("<H", self.opta._cmd(self.addr, _CMD_GET_DIGITAL_BUS))[0]
        if pins is not None:
            self.opta._cmd(self.addr, _CMD_SET_DIGITAL_PIN, "B", pins)
        if timeout is not None:
            return self.opta._cmd(self.addr, _CMD_SET_DIGITAL_DEF, "<BH", default, timeout)

    def analog(self, channel=None, channel_type=None, channel_mode=None, timeout=None, **kwargs):
        """
        Configures or reads analog channels.

        Parameters:
            - timeout : Set timeout in milliseconds after which analog channels revert to their default
                        states set previously with analog(). Note if this is set, all other args are ignored.
            - channel : The channel number to configure, read, or write. If None, reads all ADC channels.
            - channel_type : Channel type can be "adc", "dac", "pwm", "rtd", "hiz", "din".
            - channel_mode : "voltage" or "current" (default="voltage" for ADC channels).

        kwargs :
            hiz configuration:
            - no args.

            adc configuration:
            - average : Number of points for moving average (0-255, default=0).
            - rejection : Enable rejection (default=False).
            - diagnostic : Enable diagnostic (default=False).
            - pulldown : Enable pulldown (default=True for voltage, False for current).
            - secondary : This ADC channel is shared with another function (default=False).

            dac configuration:
            - use_slew : Enable slew rate control (default=False).
            - slew_rate : Slew rate if `use_slew` is True (default=0).
            - limit_current : Limit current (default=False).
            - value : Value to write to a DAC channel.
            - default_value: The default value to revert to, after the timeout set with timeout() expires.

            pwm configuration:
            - period: PWM period in uS (for example 1000uS).
            - duty:  high duty cycle in % (for example 50%).
            - default_period: The default value to revert to, after the timeout set with timeout() expires.
            - default_duty: The default value to revert to, after the timeout set with timeout() expires.

            rtd configuration:
            - use_3_wire: 3-Wire RTD (default = False).
            - current_ma: RTD current in mA (default = 1.2mA).
            - update_time: The update time of all RDT channels.

            din (digital input) configuration:
            - comparator : Enable comparator (default=True).
            - filtered : Select the filtered input to the comparator (default=True).
            - inverted : Invert the output from the digital input comparator (default=False).
            - scale : Comparator voltage scale (default=False).
            - threshold : Comparator voltage threshold (default 9).
            - sink : Sets the sink current in digital input logic mode (0-31, default 1)
            - debounce_mode : Debounce mode ("simple", "integrator" or None to disable debounce, default="simple")
            - debounce_time : Debounce time (0-31, default 24)

        Returns: ADC value(s) if reading, or None if configuring a channel or setting the analog timeout.
        """
        if channel is not None:
            if self.type == "analog" and (channel < 0 or channel > 7):
                raise ValueError("Invalid channel specified")
            if self.type == "digital" and (channel < 0 or channel > 16):
                raise ValueError("Invalid channel specified")

        # Set default analog channels timeout.
        if timeout is not None:
            if self.type != "analog":
                raise RuntimeError("Function is not supported on digital expansions")
            return self.opta._cmd(self.addr, _CMD_SET_ANALOG_TIMEOUT, "<H", timeout)

        # Read a all analog channels.
        if channel is None:
            fmt = "<HHHHHHHH" if self.type == "analog" else "<HHHHHHHHHHHHHHHH"
            cmd = _CMD_GET_ANALOG_ADC_ALL if self.type == "analog" else _CMD_GET_ANALOG_PIN_ALL
            return struct.unpack(fmt, self.opta._cmd(self.addr, cmd))

        # Read a single analog channel.
        if channel_type is None:
            channel_type = self.channels.get(channel, None)
            if self.type == "digital":
                return struct.unpack("<H", self.opta._cmd(self.addr, _CMD_GET_ANALOG_PIN, "B", channel))[-1]
            elif channel_type == "rtd":
                return struct.unpack("<Bf", self.opta._cmd(self.addr, _CMD_GET_ANALOG_RTD, "B", channel))[-1]
            elif channel_type == "adc":
                return struct.unpack("<BH", self.opta._cmd(self.addr, _CMD_GET_ANALOG_ADC, "B", channel))[-1]
            elif channel_type == "din":
                return (struct.unpack("B", self.opta._cmd(self.addr, _CMD_GET_ANALOG_DIN))[-1] & channel) == channel
            else:
                raise RuntimeError("Channel is not configured or not readable")

        # Configure a new channel
        if channel_type not in _CHANNEL_TYPES:
            raise ValueError("Invalid channel type.")
        if channel_mode not in _CHANNEL_MODES:
            raise ValueError("Invalid channel mode.")

        def get_bool(k, d):
            # True is 1 and False is 2.
            return 1 if kwargs.get(k, d) else 2

        if channel_type == "hiz":
            self.opta._cmd(self.addr, _CMD_CFG_ANALOG_HIZ, "<B", channel)
        elif channel_type == "rtd":
            self.opta._cmd(
                self.addr,
                _CMD_CFG_ANALOG_RTD,
                "<BBf",
                channel,
                get_bool("use_3_wire", False),
                kwargs.get("current_ma", 1.2),
            )
            self.opta._cmd(self.addr, _CMD_SET_ANALOG_RTD_TIM, "<H", kwargs.get("update_time", 800))
        elif channel_type == "adc":
            self.opta._cmd(
                self.addr,
                _CMD_CFG_ANALOG_ADC,
                "BBBBBBB",
                channel,
                channel_mode == "current",
                get_bool("pulldown", channel_mode == "voltage"),
                get_bool("rejection", False),
                get_bool("diagnostic", False),
                kwargs.get("average", 0),
                get_bool("secondary", False),
            )
        elif channel_type == "dac":
            if "value" not in kwargs:
                raise ValueError("DAC requires a value argument")
            # Configure DAC channel and update the output value.
            self.opta._cmd(
                self.addr,
                _CMD_CFG_ANALOG_DAC,
                "BBBBB",
                channel,
                channel_mode == "current",
                get_bool("limit_current", channel_mode == "voltage"),
                get_bool("slew_rate", False),
                kwargs.get("slew_rate", 0),
            )
            self.opta._cmd(self.addr, _CMD_SET_ANALOG_DAC, "<BHB", channel, kwargs["value"], 1)
            if "default_value" in kwargs:
                value = kwargs["default_value"]
                self.opta._cmd(self.addr, _CMD_SET_ANALOG_DAC_DEF, "<BHB", channel, value, 1)
            sleep_ms(250)  # DAC requires at leas 250ms to update after a write.
        elif channel_type == "din":
            deb_mode = kwargs.get("debounce_mode", "simple")
            self.opta._cmd(
                self.addr,
                _CMD_CFG_ANALOG_DIN,
                "BBBBBBBBB",
                channel,
                get_bool("filtered", True),
                get_bool("inverted", False),
                get_bool("comparator", True),
                1 if (deb_mode is None or deb_mode == "simple") else 2,
                get_bool("scale", False),
                kwargs.get("threshold", 9),
                kwargs.get("sink", 1),
                kwargs.get("debounce_time", 0 if deb_mode is None else 24),
            )
        elif channel_type == "pwm":
            if channel > 4:
                raise ValueError("Invalid PWM channel specified")
            if "period" not in kwargs:
                raise ValueError("PWM requires a period argument")
            period = kwargs["period"]
            duty = int(kwargs.get("duty", 50) / 100 * period)
            self.opta._cmd(self.addr, _CMD_CFG_ANALOG_PWM, "<BII", channel, period, duty)
            if "default_period" in kwargs:
                period = kwargs["default_period"]
                duty = int(kwargs.get("default_duty", 50) / 100 * period)
                self.opta._cmd(self.addr, _CMD_SET_ANALOG_PWM_DEF, "<BII", channel, period, duty)

        # Save channel type for later.
        self.channels[channel] = channel_type


class Opta:
    def __init__(self, bus_id, freq=400_000, det=None):
        """
        Initializes an Opta controller.

        Parameters:
            - bus_id : The I2C bus identifier.
            - freq : I2C bus frequency (default=400_000).
            - det : GPIO pin used for bus detection (default is a PULL_UP input pin named "BUS_DETECT").
        """
        self.bus = I2C(bus_id, freq=freq)
        self.cmd_buf = memoryview(bytearray(256 + 2))
        self.det = Pin("BUS_DETECT", Pin.IN, Pin.PULL_UP) if det is None else det
        self.exp_types = {
            0x02: ("digital", "Opta Digital Mechanical"),
            0x03: ("digital", "Opta Digital Solid State"),
            0x04: ("analog", "Opta Analog"),
            0x05: ("digital", "UNO R4 MINIMA"),
        }

    def _log_debug(self, msg):
        # Blue protocol prints in blue
        logging.debug(f"\033[94m{msg}\033[0m")

    def _log_enabled(self, level):
        return logging.getLogger().isEnabledFor(level)

    def _bus_read(self, addr, buf):
        self.bus.readfrom_into(addr, buf)
        if self._log_enabled(logging.DEBUG):
            self._log_debug("Recv: " + " ".join(["%02X" % (a) for a in buf]))

    def _bus_write(self, addr, buf):
        if self._log_enabled(logging.DEBUG):
            self._log_debug("Send: " + " ".join(["%02X" % (a) for a in buf]))
        self.bus.writeto(addr, buf)

    def _crc8(self, buf, poly=0x07, crc=0x00):
        for byte in buf:
            crc ^= byte
            for bit in range(8):
                crc = (crc << 1) ^ poly if crc & 0x80 else crc << 1
        return crc & 0xFF

    def _cmd(self, addr, cmd, fmt=None, *args):
        plen = 0 if fmt is None else struct.calcsize(fmt)
        struct.pack_into("BBB", self.cmd_buf, 0, cmd[0], cmd[1], plen)
        # Pack args (if any)
        if fmt is not None:
            struct.pack_into(fmt, self.cmd_buf, 3, *args)
        self.cmd_buf[_CMD_HDR_LEN + plen] = self._crc8(self.cmd_buf[0 : _CMD_HDR_LEN + plen])
        self._bus_write(addr, self.cmd_buf[0 : _CMD_HDR_LEN + _CMD_CRC_LEN + plen])
        if cmd[2] == 0 and not cmd[3]:
            return
        # Command has a response payload or an ACK.
        plen = 0 if cmd[3] else cmd[2]
        # Expected CMD and DIR
        exp_cmd = 0x20 if cmd[3] else cmd[1]
        exp_dir = 0x03 if cmd[0] == _CMD_DIR_GET else 0x04

        # Read and check response
        self._bus_read(addr, self.cmd_buf[0 : _CMD_HDR_LEN + _CMD_CRC_LEN + plen])
        # Check CMD, ARG and LEN
        if self.cmd_buf[0] != exp_dir or self.cmd_buf[1] != exp_cmd or self.cmd_buf[2] != plen:
            raise ValueError("Unexpected response: " + "".join("%02X" % b for b in self.cmd_buf[0:3]))

        # Check CRC
        if self.cmd_buf[_CMD_HDR_LEN + plen] != self._crc8(self.cmd_buf[0 : _CMD_HDR_LEN + plen]):
            raise ValueError("Invalid CRC")
        if not cmd[3]:
            return self.cmd_buf[_CMD_HDR_LEN : _CMD_HDR_LEN + plen]

    def _reset_bus(self, addr):
        self._cmd(addr, _CMD_CHIP_RESET, "B", 0x56)
        sleep_ms(2000)

    def _set_address(self, addr, addr_new=None):
        if addr_new is not None:
            if self._log_enabled(logging.DEBUG):
                self._log_debug(f"set address: 0x{addr:02X} new_address: 0x{addr_new:02X}")
            return self._cmd(addr, _CMD_SET_ADDRESS, "B", addr_new)
        return self._cmd(addr, _CMD_GET_ADDRESS)

    def enum_devices(self):
        """
        Initializes the bus, resets all expansions, and returns a list of detected expansions.
        Returns: A list of detected expansions on the bus.
        """
        detected = False
        expansion_list = []

        # Reset the first, last or temp device on the bus.
        for addr in [_MIN_ADDRESS, _MAX_ADDRESS, _TMP_ADDRESS]:
            try:
                self._reset_bus(addr)
                detected = True
                break
            except Exception as e:
                logging.debug(e)

        if not detected:
            raise RuntimeError("No expansions detected on the bus")

        addr = _MAX_ADDRESS
        # Assign temp I2C addresses to expansions.
        while not self.det.value():
            self._set_address(0x0A, addr_new=addr)
            sleep_ms(100)
            try:
                xaddr, xtype = self._set_address(addr)
                if xaddr == addr:
                    addr += 1
                if self._log_enabled(logging.DEBUG):
                    self._log_debug(f"phase 1 type: 0x{xtype:02X} address: 0x{xaddr:02X}")
            except Exception as e:
                logging.debug(e)

        # Assign final I2C addresses to expansions.
        for addr_new in range(_MIN_ADDRESS, _MIN_ADDRESS + addr - _MAX_ADDRESS):
            self._set_address(addr - 1, addr_new)
            sleep_ms(100)
            try:
                xaddr, xtype = self._set_address(addr_new)
                addr -= 1
                if self._log_enabled(logging.DEBUG):
                    self._log_debug(f"phase 2 type: 0x{xtype:02X} address: 0x{xaddr:02X}")
                if xtype not in self.exp_types:
                    raise RuntimeError("Unsupported expansion type %d" % xtype)
                expansion_list.append(Expansion(self, self.exp_types[xtype][0], xaddr, self.exp_types[xtype][1]))

            except Exception as e:
                logging.debug(e)

        return expansion_list
