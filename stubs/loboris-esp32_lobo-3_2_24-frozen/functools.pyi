# make_stub_files: Tue 23 Apr 2019 at 22:52:00

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def partial(func: Any, *args, **kwargs) -> Any:
    #   0: return func(*args+more_args,None=kw)
    # ? 0: return func(*args+more_args, None=kw)
    #   1: return _partial
    # ? 1: return _partial
    def _partial(*more_args, **more_kwargs) -> Any: ...
        #   0: return func(*args+more_args,None=kw)
        # ? 0: return func(*args+more_args, None=kw)
def update_wrapper(wrapper: Any, wrapped: Any) -> Any: ...
    #   0: return wrapper
    # ? 0: return wrapper
def wraps(wrapped: Any) -> Any: ...
    #   0: return lambda x: x
    # ? 0: return lambda x: x
def reduce(function: Any, iterable: Any, initializer: Any=None) -> Any: ...
    #   0: return value
    # ? 0: return value
