"""
Module: 'usb.device.cdc' from micropython-lib

location: micropython/usb/usb-device-cdc/usb/device/cdc.py
"""

import io

from _typeshed import Incomplete
from micropython import const as const

from .core import Buffer as Buffer
from .core import Interface as Interface
from .core import split_bmRequestType as split_bmRequestType

_EP_IN_FLAG: Incomplete
_STAGE_IDLE: int
_STAGE_SETUP: int
_STAGE_DATA: int
_STAGE_ACK: int
_REQ_TYPE_STANDARD: int
_REQ_TYPE_CLASS: int
_REQ_TYPE_VENDOR: int
_REQ_TYPE_RESERVED: int
_DEV_CLASS_MISC: int
_CS_DESC_TYPE: int
_INTERFACE_CLASS_CDC: int
_INTERFACE_SUBCLASS_CDC: int
_PROTOCOL_NONE: int
_CDC_FUNC_DESC_HEADER: int
_CDC_FUNC_DESC_CALL_MANAGEMENT: int
_CDC_FUNC_DESC_ABSTRACT_CONTROL: int
_CDC_FUNC_DESC_UNION: int
_SET_LINE_CODING_REQ: int
_GET_LINE_CODING_REQ: int
_SET_CONTROL_LINE_STATE: int
_SEND_BREAK_REQ: int
_LINE_CODING_STOP_BIT_1: int
_LINE_CODING_STOP_BIT_1_5: int
_LINE_CODING_STOP_BIT_2: int
_LINE_CODING_PARITY_NONE: int
_LINE_CODING_PARITY_ODD: int
_LINE_CODING_PARITY_EVEN: int
_LINE_CODING_PARITY_MARK: int
_LINE_CODING_PARITY_SPACE: int
_LINE_STATE_DTR: int
_LINE_STATE_RTS: int
_PARITY_BITS_REPR: str
_STOP_BITS_REPR: Incomplete
_CDC_VERSION: int
_CDC_CONTROL_EP_NUM: int
_CDC_DATA_EP_NUM: int
_CDC_ITF_DATA_CLASS: int
_CDC_ITF_DATA_SUBCLASS: int
_CDC_ITF_DATA_PROT: int
_BULK_EP_LEN: int
_MP_EINVAL: int
_MP_ETIMEDOUT: int
_MP_STREAM_FLUSH: int
_MP_STREAM_POLL: int
_MP_STREAM_POLL_WR: int
_MP_STREAM_POLL_RD: int
_MP_STREAM_POLL_HUP: int

class CDCInterface(io.IOBase, Interface):
    break_cb: Incomplete
    line_state_cb: Incomplete
    line_coding_cb: Incomplete
    _line_state: int
    _line_coding: Incomplete
    ep_c_in: Incomplete
    _c_itf: Incomplete
    def __init__(self, **kwargs) -> None: ...
    _timeout: Incomplete
    _wb: Incomplete
    _rb: Incomplete
    def init(
        self,
        baudrate: int = 9600,
        bits: int = 8,
        parity: str = "N",
        stop: int = 1,
        timeout: int = 1000,
        txbuf: int = 256,
        rxbuf: int = 256,
        flow: int = 0,
    ) -> None: ...
    @property
    def rts(self): ...
    @property
    def dtr(self): ...
    @property
    def baudrate(self): ...
    @property
    def stop_bits(self): ...
    @property
    def parity(self): ...
    @property
    def data_bits(self): ...
    def __repr__(self) -> str: ...
    def set_break_cb(self, cb) -> None: ...
    def set_line_state_cb(self, cb) -> None: ...
    def set_line_coding_cb(self, cb) -> None: ...
    ep_d_out: Incomplete
    ep_d_in: Incomplete
    def desc_cfg(self, desc, itf_num, ep_num, strs) -> None: ...
    def num_itfs(self): ...
    def num_eps(self): ...
    def on_open(self) -> None: ...
    def on_interface_control_xfer(self, stage, request): ...
    def _wr_xfer(self) -> None: ...
    def _wr_cb(self, ep, res, num_bytes) -> None: ...
    def _rd_xfer(self) -> None: ...
    def _rd_cb(self, ep, res, num_bytes) -> None: ...
    def write(self, buf): ...
    def read(self, size): ...
    def readinto(self, b): ...
    def _readinto(self, b, start): ...
    def ioctl(self, req, arg): ...
    def flush(self) -> None: ...
