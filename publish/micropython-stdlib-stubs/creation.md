


1. copy typeshed/stdlib (from pyright fallback)
2, rename the stubs that are used internally, but are not part of micropython
    - [ ] codecs
    - [ ] contextlib
    - [ ] contextvars
    - [ ] dataclasses
    - [ ] decimal
    - [ ] enum
    - [ ] fractions
    - [ ] functools
    - [ ] numbers
    - [ ] queue
    - [ ] selectors
    - [ ] sre_compile
    - [ ] sre_constants
    - [ ] sre_parse

3. remove all stubs and stub-only packages that are not in micropython
    - database stubs 
    - email 
    - http
    - .........

4. make some customisations ( is this still needed?) 
    - sys.pyi - Add to the end of the file:
    ``` python
    # MicroPython specific functions
    # Copyright (c) 2023 Jos Verlinde

    from typing import Optional
    from _typeshed import Incomplete
    def atexit(func:Optional[Callable[[],Any]]) -> Optional[Callable[[],Any]]: 
        """\
        Register func to be called upon termination. func must be a callable that takes no arguments, 
        or None to disable the call. The atexit function will return the previous value set by this function, 
        which is initially None.

        Ports: Unix, Windows
        """
        ...

    def print_exception(exc, file=sys.stdout, /):
        """Print exception with a traceback to a file-like object file (or sys.stdout by default)."""
        ...
    ```






