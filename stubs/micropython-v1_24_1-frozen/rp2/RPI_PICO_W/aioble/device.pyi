from .core import ble as ble, log_error as log_error, register_irq_handler as register_irq_handler
from _typeshed import Incomplete
from micropython import const as const

_IRQ_MTU_EXCHANGED: int

class DeviceDisconnectedError(Exception): ...

def _device_irq(event, data) -> None: ...

class DeviceTimeout:
    _connection: Incomplete
    _timeout_ms: Incomplete
    _timeout_task: Incomplete
    _task: Incomplete
    def __init__(self, connection, timeout_ms) -> None: ...
    async def _timeout_sleep(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_traceback: types.TracebackType | None
    ) -> None: ...

class Device:
    addr_type: Incomplete
    addr: Incomplete
    _connection: Incomplete
    def __init__(self, addr_type, addr) -> None: ...
    def __eq__(self, rhs): ...
    def __hash__(self): ...
    def __str__(self) -> str: ...
    def addr_hex(self): ...
    async def connect(
        self,
        timeout_ms: int = 10000,
        scan_duration_ms: Incomplete | None = None,
        min_conn_interval_us: Incomplete | None = None,
        max_conn_interval_us: Incomplete | None = None,
    ): ...

class DeviceConnection:
    _connected: Incomplete
    device: Incomplete
    encrypted: bool
    authenticated: bool
    bonded: bool
    key_size: bool
    mtu: Incomplete
    _conn_handle: Incomplete
    _event: Incomplete
    _mtu_event: Incomplete
    _discover: Incomplete
    _characteristics: Incomplete
    _task: Incomplete
    _timeouts: Incomplete
    _pair_event: Incomplete
    _l2cap_channel: Incomplete
    def __init__(self, device) -> None: ...
    async def device_task(self) -> None: ...
    def _run_task(self) -> None: ...
    async def disconnect(self, timeout_ms: int = 2000) -> None: ...
    async def disconnected(self, timeout_ms: Incomplete | None = None, disconnect: bool = False) -> None: ...
    async def service(self, uuid, timeout_ms: int = 2000): ...
    def services(self, uuid: Incomplete | None = None, timeout_ms: int = 2000): ...
    async def pair(self, *args, **kwargs) -> None: ...
    def is_connected(self): ...
    def timeout(self, timeout_ms): ...
    async def exchange_mtu(self, mtu: Incomplete | None = None, timeout_ms: int = 1000): ...
    async def l2cap_accept(self, psm, mtu, timeout_ms: Incomplete | None = None): ...
    async def l2cap_connect(self, psm, mtu, timeout_ms: int = 1000): ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_traceback) -> None: ...
