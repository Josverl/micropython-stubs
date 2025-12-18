from _typeshed import Incomplete
from micropython import const as const

_MSG_TYPE_REQUEST: int
_MSG_TYPE_RESPONSE: int
_MSG_TYPE_NOTIFY: int

def log_level_enabled(level): ...

class Future:
    msgid: Incomplete
    msgbuf: Incomplete
    fname: Incomplete
    fargs: Incomplete
    def __init__(self, msgid, msgbuf, fname, fargs) -> None: ...
    def join(self, timeout: int = 0): ...

class MsgPackIO:
    stream: Incomplete
    def __init__(self) -> None: ...
    def feed(self, data) -> None: ...
    def readable(self): ...
    def truncate(self) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...

class MsgPackRPC:
    epts: Incomplete
    msgid: int
    msgbuf: Incomplete
    msgio: Incomplete
    callables: Incomplete
    def __init__(self, streaming: bool = False) -> None:
        """
        Create a MsgPack RPC object.
        streaming: If True, messages can span multiple buffers, otherwise a buffer contains
        exactly one full message. Note streaming mode is slower, so it should be disabled
        if it's not needed.
        """
    def _bind_callback(self, src, name) -> None: ...
    def _recv_callback(self, src, data) -> None: ...
    def _process_unpacked_obj(self, obj) -> None: ...
    def _send_msg(self, msgid, msgtype, fname, fargs, **kwargs): ...
    def _dispatch(self, msgid, fname, fargs) -> None: ...
    def bind(self, name, obj) -> None:
        """
        Bind a callable or an object to a name.
        name: The name to which the callable or object is bound.
        obj: A callable or an object to bind to the name. If an object is passed, all of its
        public methods will be bound to their respective qualified names.
        """
    rproc: Incomplete
    def start(self, firmware=None, num_channels: int = 2, timeout: int = 3000) -> None:
        """
        Initializes OpenAMP, loads the remote processor's firmware and starts.
        firmware: A path to an elf file stored in the filesystem, or an address to an entry point in flash.
        num_channels: The number of channels to wait for the remote processor to
        create before starting to communicate with it.
        timeout: How long to wait for the remote processor to start, 0 means forever.
        """
    def call(self, fname, *args, **kwargs):
        """
        Synchronous call. The client is blocked until the RPC is finished.
        """
    def call_async(self, fname, *args, **kwargs):
        """
        Asynchronous call. The client returns a Future object immediately.
        """
