"""
WiPy specific features. See: https://docs.micropython.org/en/v1.18/library/wipy.html

The ``wipy`` module contains functions to control specific features of the
WiPy, such as the heartbeat LED.
"""

# source version: v1_18
# origin module:: micropython/docs/library/wipy.rst
from typing import Any, Optional


def heartbeat(enable: Optional[Any]) -> bool:
    """
    Get or set the state (enabled or disabled) of the heartbeat LED. Accepts and
    returns boolean values (``True`` or ``False``).
    """
    ...
