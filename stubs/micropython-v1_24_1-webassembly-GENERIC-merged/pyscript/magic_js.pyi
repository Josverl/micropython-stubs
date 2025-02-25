"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""

import sys
from typing import Any

from _pyscript import PyWorker, js_import  # type: ignore[import]

RUNNING_IN_WORKER = ...
config = ...
if "MicroPython" in sys.version:
    ...
else:
    ...

class JSModule:
    def __init__(self, name) -> None: ...
    def __getattr__(self, field) -> Any | None: ...

if RUNNING_IN_WORKER:
    PyWorker = ...
    window = ...
    document = ...
    js_import = ...
    sync = ...
    def current_target(): ...

else:
    window = ...
    document = ...
    sync = ...
    def current_target(): ...
