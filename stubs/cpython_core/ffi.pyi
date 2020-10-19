
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Func:
    def __init__(self, f: Any, restype: Any) -> None: ...
    def __call__(self, *args) -> Any:
        #   0: return x.encode()
        # ? 0: return x.encode()
        #   1: return ctypes.addressof(a)
        # ? 1: return ctypes.addressof(str)
        #   2: return x
        # ? 2: return x
        #   3: return res
        # ? 3: return res
        def conv_arg(x: Any) -> Any: ...
            #   0: return x.encode()
            # ? 0: return x.encode()
            #   1: return ctypes.addressof(a)
            # ? 1: return ctypes.addressof(str)
            #   2: return x
            # ? 2: return x
class Var:
    def __init__(self, v: Any) -> None: ...
    def get(self) -> Any: ...
        #   0: return self.v.value
        # ? 0: return self.v.value
class DynMod:
    def __init__(self, name: str) -> None: ...
    def func(self, ret: Any, name: str, params: Any) -> Any: ...
        #   0: return Func(f,ret)
        # ? 0: return Func(f, ret)
    def var(self, type: Any, name: str) -> Any: ...
        #   0: return Var(v)
        # ? 0: return Var(v)
def open(name: str) -> Any: ...
    #   0: return DynMod(name)
    # ? 0: return DynMod(str)
def func(ret: Any, addr: Any, params: Any) -> Any: ...
    #   0: return ftype(addr)
    # ? 0: return ftype(addr)
def callback(ret: Any, func: Any, params: Any) -> Any: ...
    #   0: return ftype(func)
    # ? 0: return ftype(func)
