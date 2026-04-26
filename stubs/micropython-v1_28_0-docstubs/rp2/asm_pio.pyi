"""
Default PIO assembler typing surface — re-exports :mod:`rp2.asm_pio_rp2040`.

This module exists for backward compatibility with the historical idiom

.. code-block:: python

    if TYPE_CHECKING:
        from rp2.asm_pio import *

…which has always meant *"give me the RP2040 / PIO v0 DSL"*. The actual
declarations now live in :mod:`rp2.asm_pio_rp2040`; this stub simply
re-exports them so existing PIO programs keep type-checking unchanged.

PIO target selection
--------------------

Pick *one* of the three imports below in your PIO program file — they
cannot be combined:

.. code-block:: python

    if TYPE_CHECKING:
        # Default (RP2040 / PIO v0) — equivalent to importing rp2.asm_pio_rp2040:
        from rp2.asm_pio import *

        # Explicit RP2040 / PIO v0:
        # from rp2.asm_pio_rp2040 import *

        # RP2350 / PIO v1 (adds prev, next, jmppin, irq_prev, irq_next):
        # from rp2.asm_pio_rp2350 import *

See https://github.com/micropython/micropython/pull/18975 for the RP2350
PIO v1 additions.
"""

# Re-export the full RP2040 PIO v0 surface (constants, helpers, instruction
# functions, directives, and the chainable ``_PIOInstr`` Protocol).
from rp2.asm_pio_rp2040 import *  # noqa: F401,F403
from rp2.asm_pio_rp2040 import _PIOInstr  # re-export the Protocol explicitly
