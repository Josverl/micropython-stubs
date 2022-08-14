import importlib
from typing import Any

_import_hook: Any
_import_exts: Any

class ImphookFileLoader(importlib._bootstrap_external.FileLoader):
    def create_module(self, spec): ...
    def exec_module(self, mod) -> None: ...

def setimphook(hook, exts): ...
