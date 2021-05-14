
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class ImphookFileLoader(importlib._bootstrap_external.FileLoader):
    def create_module(self, spec: Any) -> Any: ...
        #   0: return m
        # ? 0: return m
    def exec_module(self, mod: Any) -> None: ...
def setimphook(hook: Any, exts: Any) -> Any: ...
    #   0: return old_hook
    # ? 0: return old_hook
