import importlib
from _typeshed import Incomplete

_import_hook: Incomplete
_import_exts: Incomplete

class ImphookFileLoader(importlib._bootstrap_external.FileLoader):
    def create_module(self, spec): ...
    def exec_module(self, mod) -> None: ...

def setimphook(hook, exts): ...
