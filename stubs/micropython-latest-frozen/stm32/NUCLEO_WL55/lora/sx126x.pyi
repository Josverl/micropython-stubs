from .async_modem import AsyncModem as AsyncModem
from .modem import BaseModem as BaseModem, ConfigError as ConfigError, RxPacket as RxPacket, _clamp as _clamp, _flag as _flag
from .sync_modem import SyncModem as SyncModem
from _typeshed import Incomplete

_DEBUG: Incomplete
_REG_RXGAINCR: Incomplete
_REG_LSYNCRH: Incomplete
_REG_LSYNCRL: Incomplete
_CMD_CFG_DIO_IRQ: Incomplete
_CMD_CLR_ERRORS: Incomplete
_CMD_CLR_IRQ_STATUS: Incomplete
_CMD_GET_ERROR: Incomplete
_CMD_GET_IRQ_STATUS: Incomplete
_CMD_GET_RX_BUFFER_STATUS: Incomplete
_CMD_GET_STATUS: Incomplete
_CMD_GET_PACKET_STATUS: Incomplete
_CMD_READ_REGISTER: Incomplete
_CMD_READ_BUFFER: Incomplete
_CMD_SET_BUFFER_BASE_ADDRESS: Incomplete
_CMD_SET_MODULATION_PARAMS: Incomplete
_CMD_SET_PACKET_PARAMS: Incomplete
_CMD_SET_PACKET_TYPE: Incomplete
_CMD_SET_PA_CONFIG: Incomplete
_CMD_SET_RF_FREQUENCY: Incomplete
_CMD_SET_RX: Incomplete
_CMD_SET_SLEEP: Incomplete
_CMD_SET_STANDBY: Incomplete
_CMD_SET_DIO3_AS_TCXO_CTRL: Incomplete
_CMD_SET_DIO2_AS_RF_SWITCH_CTRL: Incomplete
_CMD_SET_TX: Incomplete
_CMD_SET_TX_PARAMS: Incomplete
_CMD_WRITE_BUFFER: Incomplete
_CMD_WRITE_REGISTER: Incomplete
_CMD_CALIBRATE: Incomplete
_CMD_CALIBRATE_IMAGE: Incomplete
_STATUS_MODE_MASK: Incomplete
_STATUS_MODE_SHIFT: Incomplete
_STATUS_MODE_STANDBY_RC: Incomplete
_STATUS_MODE_STANDBY_HSE32: Incomplete
_STATUS_MODE_FS: Incomplete
_STATUS_MODE_RX: Incomplete
_STATUS_MODE_TX: Incomplete
_STATUS_CMD_MASK: Incomplete
_STATUS_CMD_SHIFT: Incomplete
_STATUS_CMD_DATA_AVAIL: Incomplete
_STATUS_CMD_TIMEOUT: Incomplete
_STATUS_CMD_ERROR: Incomplete
_STATUS_CMD_EXEC_FAIL: Incomplete
_STATUS_CMD_TX_COMPLETE: Incomplete
_CFG_SF_MIN: Incomplete
_CFG_SF_MAX: Incomplete
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
_REG_IQ_POLARITY_SETUP: Incomplete
_REG_RX_GAIN: Incomplete
_REG_RTC_CTRL: Incomplete
_REG_EVT_CLR: Incomplete
_REG_EVT_CLR_MASK: Incomplete
_IRQ_DRIVER_RX_MASK: Incomplete
_CMD_BUSY_TIMEOUT_BASE_US: Incomplete
_CALIBRATE_TYPICAL_TIME_US: Incomplete
_CALIBRATE_TIMEOUT_US: Incomplete
_CONTINUOUS_TIMEOUT_VAL: Incomplete

class _SX126x(BaseModem):
    _IRQ_RX_COMPLETE: Incomplete
    _IRQ_TX_COMPLETE = _IRQ_TX_DONE
    _spi: Incomplete
    _cs: Incomplete
    _busy: Incomplete
    _sleep: bool
    _dio1: Incomplete
    _busy_timeout: Incomplete
    _buf: Incomplete
    _output_power: int
    _bw: int
    _ramp_val: int
    def __init__(self, spi, cs, busy, dio1, dio2_rf_sw, dio3_tcxo_millivolts, dio3_tcxo_start_time_us, reset, lora_cfg, ant_sw) -> None: ...
    def sleep(self, warm_start: bool = ...) -> None: ...
    def _standby(self) -> None: ...
    def is_idle(self): ...
    def _wakeup(self) -> None: ...
    def _decode_status(self, raw_status, check_errors: bool = ...): ...
    def _get_status(self): ...
    def _check_error(self): ...
    def _clear_errors(self) -> None: ...
    _last_irq: Incomplete
    def _clear_irq(self, clear_bits: int = ...) -> None: ...
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
    def start_recv(self, timeout_ms: Incomplete | None = ..., continuous: bool = ..., rx_length: int = ...): ...
    def poll_recv(self, rx_packet: Incomplete | None = ...): ...
    def _rx_flags_success(self, flags): ...
    def _read_packet(self, rx_packet, flags): ...
    def prepare_send(self, packet) -> None: ...
    _tx: bool
    def start_send(self): ...
    def _wait_not_busy(self, timeout_us) -> None: ...
    def _cmd(self, fmt, *write_args, n_read: int = ..., write_buf: Incomplete | None = ..., read_buf: Incomplete | None = ...): ...
    def _reg_read(self, addr): ...
    def _reg_write(self, addr, val): ...

class _SX1262(_SX126x):
    def __init__(
        self,
        spi,
        cs,
        busy,
        dio1: Incomplete | None = ...,
        dio2_rf_sw: bool = ...,
        dio3_tcxo_millivolts: Incomplete | None = ...,
        dio3_tcxo_start_time_us: int = ...,
        reset: Incomplete | None = ...,
        lora_cfg: Incomplete | None = ...,
        ant_sw: Incomplete | None = ...,
    ) -> None: ...
    def _tx_hp(self): ...
    def _get_pa_tx_params(self, output_power, tx_ant): ...

class _SX1261(_SX126x):
    def __init__(
        self,
        spi,
        cs,
        busy,
        dio1: Incomplete | None = ...,
        dio2_rf_sw: bool = ...,
        dio3_tcxo_millivolts: Incomplete | None = ...,
        dio3_tcxo_start_time_us: int = ...,
        reset: Incomplete | None = ...,
        lora_cfg: Incomplete | None = ...,
        ant_sw: Incomplete | None = ...,
    ) -> None: ...
    def _tx_hp(self): ...
    def _get_pa_tx_params(self, output_power, tx_ant): ...

class SX1261(_SX1261, SyncModem): ...
class SX1262(_SX1262, SyncModem): ...
class AsyncSX1261(_SX1261, AsyncModem): ...
class AsyncSX1262(_SX1262, AsyncModem): ...
