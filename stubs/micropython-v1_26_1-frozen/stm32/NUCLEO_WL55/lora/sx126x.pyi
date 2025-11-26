from .async_modem import AsyncModem as AsyncModem
from .modem import BaseModem as BaseModem, ConfigError as ConfigError, RxPacket as RxPacket, _clamp as _clamp, _flag as _flag
from .sync_modem import SyncModem as SyncModem
from _typeshed import Incomplete

_DEBUG: bool
_REG_RXGAINCR: int
_REG_LSYNCRH: int
_REG_LSYNCRL: int
_CMD_CFG_DIO_IRQ: int
_CMD_CLR_ERRORS: int
_CMD_CLR_IRQ_STATUS: int
_CMD_GET_ERROR: int
_CMD_GET_IRQ_STATUS: int
_CMD_GET_RX_BUFFER_STATUS: int
_CMD_GET_STATUS: int
_CMD_GET_PACKET_STATUS: int
_CMD_READ_REGISTER: int
_CMD_READ_BUFFER: int
_CMD_SET_BUFFER_BASE_ADDRESS: int
_CMD_SET_MODULATION_PARAMS: int
_CMD_SET_PACKET_PARAMS: Incomplete
_CMD_SET_PACKET_TYPE: int
_CMD_SET_PA_CONFIG: int
_CMD_SET_RF_FREQUENCY: int
_CMD_SET_RX: int
_CMD_SET_SLEEP: int
_CMD_SET_STANDBY: int
_CMD_SET_DIO3_AS_TCXO_CTRL: int
_CMD_SET_DIO2_AS_RF_SWITCH_CTRL: int
_CMD_SET_TX: int
_CMD_SET_TX_PARAMS: int
_CMD_WRITE_BUFFER: int
_CMD_WRITE_REGISTER: int
_CMD_CALIBRATE: int
_CMD_CALIBRATE_IMAGE: int
_STATUS_MODE_MASK: Incomplete
_STATUS_MODE_SHIFT: int
_STATUS_MODE_STANDBY_RC: int
_STATUS_MODE_STANDBY_HSE32: int
_STATUS_MODE_FS: int
_STATUS_MODE_RX: int
_STATUS_MODE_TX: int
_STATUS_CMD_MASK: int
_STATUS_CMD_SHIFT: int
_STATUS_CMD_DATA_AVAIL: int
_STATUS_CMD_TIMEOUT: int
_STATUS_CMD_ERROR: int
_STATUS_CMD_EXEC_FAIL: int
_STATUS_CMD_TX_COMPLETE: int
_CFG_SF_MIN: int
_CFG_SF_MAX: int
_IRQ_TX_DONE: Incomplete
_IRQ_RX_DONE: Incomplete
_IRQ_PREAMBLE_DETECTED: Incomplete
_IRQ_SYNC_DETECTED: Incomplete
_IRQ_HEADER_VALID: Incomplete
_IRQ_HEADER_ERR: Incomplete
_IRQ_CRC_ERR: Incomplete
_IRQ_CAD_DONE: Incomplete
_IRQ_CAD_DETECTED: Incomplete
_IRQ_TIMEOUT: Incomplete
_REG_IQ_POLARITY_SETUP: int
_REG_RX_GAIN: int
_REG_RTC_CTRL: int
_REG_EVT_CLR: int
_REG_EVT_CLR_MASK: int
_IRQ_DRIVER_RX_MASK: Incomplete
_CMD_BUSY_TIMEOUT_BASE_US: int
_CALIBRATE_TYPICAL_TIME_US: int
_CALIBRATE_TIMEOUT_US: int
_CONTINUOUS_TIMEOUT_VAL: int

class _SX126x(BaseModem):
    _IRQ_RX_COMPLETE = _IRQ_RX_DONE | _IRQ_TIMEOUT
    _IRQ_TX_COMPLETE = _IRQ_TX_DONE
    _spi: Incomplete
    _cs: Incomplete
    _busy: Incomplete
    _sleep: bool
    _dio1: Incomplete
    _busy_timeout: Incomplete
    _buf_view: Incomplete
    _output_power: int
    _bw: int
    _ramp_val: int
    _configured: bool
    def __init__(self, spi, cs, busy, dio1, dio2_rf_sw, dio3_tcxo_millivolts, dio3_tcxo_start_time_us, reset, lora_cfg, ant_sw) -> None: ...
    def sleep(self, warm_start: bool = True) -> None: ...
    def _standby(self) -> None: ...
    def is_idle(self): ...
    def _wakeup(self) -> None: ...
    def _decode_status(self, raw_status, check_errors: bool = True): ...
    def _get_status(self): ...
    def _check_error(self): ...
    def _clear_errors(self) -> None: ...
    _last_irq: Incomplete
    def _clear_irq(self, clear_bits: int = 65535) -> None: ...
    def _set_tx_ant(self, tx_ant) -> None: ...
    def _symbol_offsets(self): ...
    _preamble_len: Incomplete
    _invert_iq: Incomplete
    _rf_freq_hz: Incomplete
    _sf: Incomplete
    _coding_rate: Incomplete
    def configure(self, lora_cfg) -> None: ...
    def _invert_workaround(self, enable) -> None: ...
    def _get_irq(self): ...
    def calibrate(self) -> None: ...
    def calibrate_image(self) -> None: ...
    def start_recv(self, timeout_ms=None, continuous: bool = False, rx_length: int = 255): ...
    def poll_recv(self, rx_packet=None): ...
    def _rx_flags_success(self, flags): ...
    def _read_packet(self, rx_packet, flags): ...
    def prepare_send(self, packet) -> None: ...
    _tx: bool
    def start_send(self): ...
    def _wait_not_busy(self, timeout_us) -> None: ...
    def _cmd(self, fmt, *write_args, n_read: int = 0, write_buf=None, read_buf=None): ...
    def _reg_read(self, addr): ...
    def _reg_write(self, addr, val): ...

class _SX1262(_SX126x):
    def __init__(
        self,
        spi,
        cs,
        busy,
        dio1=None,
        dio2_rf_sw: bool = True,
        dio3_tcxo_millivolts=None,
        dio3_tcxo_start_time_us: int = 1000,
        reset=None,
        lora_cfg=None,
        ant_sw=None,
    ) -> None: ...
    def _tx_hp(self): ...
    def _get_pa_tx_params(self, output_power, tx_ant): ...

class _SX1261(_SX126x):
    def __init__(
        self,
        spi,
        cs,
        busy,
        dio1=None,
        dio2_rf_sw: bool = True,
        dio3_tcxo_millivolts=None,
        dio3_tcxo_start_time_us: int = 1000,
        reset=None,
        lora_cfg=None,
        ant_sw=None,
    ) -> None: ...
    def _tx_hp(self): ...
    def _get_pa_tx_params(self, output_power, tx_ant): ...

class SX1261(_SX1261, SyncModem): ...
class SX1262(_SX1262, SyncModem): ...
class AsyncSX1261(_SX1261, AsyncModem): ...
class AsyncSX1262(_SX1262, AsyncModem): ...
