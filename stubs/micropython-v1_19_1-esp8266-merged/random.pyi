from typing import Optional, Any
from _typeshed import Incomplete as Incomplete

def seed(n: Incomplete | None = ...) -> None:
    """
    Initialise the random number generator module with the seed *n* which should
    be an integer.  When no argument (or ``None``) is passed in it will (if
    supported by the port) initialise the PRNG with a true random number
    (usually a hardware generated random number).

    The ``None`` case only works if ``MICROPY_PY_URANDOM_SEED_INIT_FUNC`` is
    enabled by the port, otherwise it raises ``ValueError``.
    """

def getrandbits(n) -> int:
    """
    Return an integer with *n* random bits (0 <= n <= 32).
    """
