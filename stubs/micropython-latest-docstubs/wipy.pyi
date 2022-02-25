"""
WiPy specific features. See: https://docs.micropython.org/en/latest/library/wipy.html

The ``wipy`` module contains functions to control specific features of the
WiPy, such as the heartbeat LED.
"""

# source version: latest
# origin module:: micropython/docs/library/wipy.rst
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union

def heartbeat(enable: Optional[Any] = None) -> bool:
    """
    Get or set the state (enabled or disabled) of the heartbeat LED. Accepts and
    returns boolean values (``True`` or ``False``).
    """
    ...
