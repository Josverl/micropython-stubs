import sys
import threading

from typing_extensions import Never

_global_lock: threading.Lock  # type: ignore

class _LoopBoundMixin:
    if sys.version_info < (3, 11):
        def __init__(self, *, loop: Never = ...) -> None: ...
