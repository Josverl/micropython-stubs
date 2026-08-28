"""
Type hints for the ``rp2.asm_pio`` DSL **as exposed on RP2350** (PIO version 1).

This stub is a thin **overlay** on top of :mod:`rp2.asm_pio_rp2040` (the
RP2040-compatible PIO version 0 baseline). Importing it inside a
``TYPE_CHECKING`` block enables the additional instructions, sources,
modifiers and constants that exist on RP2350's PIO v1 hardware:

* ``irq(prev, …)`` / ``irq(next, …)`` — target a neighbouring PIO instance.
* ``wait(1, jmppin, n)`` — stall on the JMP-pin GPIO.
* ``wait(1, irq_prev, n)`` / ``wait(1, irq_next, n)`` — cross-PIO IRQ wait.
* ``in_(pindirs, n)`` and ``mov(pindirs, src)`` — read/write the PINDIRS register.
* Wider side-set / set / out pin counts (driven by ``@asm_pio`` configuration).

Reference: https://github.com/micropython/micropython/pull/18975

Usage in a PIO program file
---------------------------

The PIO target **must be specified explicitly** at the top of the file. Pick
*one* of the three imports below — they cannot be combined:

.. code-block:: python

    try:
        from typing_extensions import TYPE_CHECKING  # type: ignore
    except ImportError:
        TYPE_CHECKING = False

    if TYPE_CHECKING:
        # Default (RP2040 / PIO v0):
        from rp2.asm_pio import *

        # Explicit RP2040 / PIO v0:
        # from rp2.asm_pio_rp2040 import *

        # RP2350 / PIO v1 (uncomment instead of one of the lines above):
        # from rp2.asm_pio_rp2350 import *

This module re-exports every symbol from :mod:`rp2.asm_pio_rp2040`, so a
single ``from rp2.asm_pio_rp2350 import *`` is sufficient — there is no
need to also import the baseline.
"""

from typing import Final
from typing_extensions import TYPE_CHECKING

# Re-export the RP2040 baseline (constants, helpers, instruction functions,
# directives). All of those remain valid on RP2350.
from rp2.asm_pio_rp2040 import *  # noqa: F401,F403
from rp2.asm_pio_rp2040 import _PIOInstr  # re-export the chainable instruction Protocol

if TYPE_CHECKING:
    # ------------------------------------------------------------------
    # RP2350 PIO v1 additions — constants
    # ------------------------------------------------------------------

    # ``irq`` target modifiers (PIO v1 only).
    # Used as the first positional argument to ``irq``:
    #   irq(prev, 0)        # raise flag 0 on the previous PIO instance
    #   irq(next, 4)        # raise flag 4 on the next PIO instance
    #   irq(clear | prev, 1)
    prev: Final[int]
    next: Final[int]

    # ``wait`` source extensions (PIO v1 only).
    # Used as the second positional argument to ``wait``:
    #   wait(1, jmppin, 0)
    #   wait(1, irq_prev, 0)
    #   wait(1, irq_next, 0)
    jmppin: Final[int]
    irq_prev: Final[int]
    irq_next: Final[int]

    # ------------------------------------------------------------------
    # RP2350 PIO v1 additions — instruction extensions
    # ------------------------------------------------------------------
    # The instruction *names* (``in_``, ``out``, ``mov``, ``wait``, ``irq``)
    # are unchanged from RP2040 and are inherited via the wildcard import
    # above. PIO v1 only widens the set of accepted ``src``/``dest``/modifier
    # arguments — those are encoded as plain ``int`` values, so the existing
    # signatures already accept them. The constants above (``prev``, ``next``,
    # ``jmppin``, ``irq_prev``, ``irq_next``) are what gives editors the
    # right autocomplete inside a PIO v1 program.
    #
    # If MicroPython adds genuinely new instruction *names* on PIO v1 in the
    # future, declare them here returning ``_PIOInstr`` (or ``None`` for
    # directives) — for example::
    #
    #     def some_new_instr(arg: int, /) -> _PIOInstr: ...
