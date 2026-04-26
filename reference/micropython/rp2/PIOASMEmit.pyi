"""
Module: 'rp2.PIOASMEmit'
"""

# This stub file is manually maintained and copied from the reference
# stubs into the docstubs during the merge step.
#
# PIOASMEmit is the internal emitter used by the @asm_pio decorator. It is
# documented as "should not be instantiated directly, but used via the
# @asm_pio decorator." The PIO instruction / directive / modifier surface
# (set, out, jmp, wait, mov, irq, push, pull, nop, in_, word, side, delay,
# label, wrap, wrap_target, ...) lives in `rp2.asm_pio_rp2040` (re-exported
# via `rp2.asm_pio`) and is the single source of truth for the typing
# surface of the PIO assembler DSL.
#
# This stub deliberately keeps PIOASMEmit opaque: only `__init__` is
# declared, plus a `__getattr__` fallback so any leftover internal access
# does not produce false-positive "unknown attribute" errors.
#
# See: scratch/33_rp2_pio_stub_generator.md
#
from __future__ import annotations

from typing import List

from _typeshed import Incomplete

class PIOASMEmit:
    """
    Internal emitter used by the ``@asm_pio`` decorator. Not intended for
    direct use.

    PIO instructions, directives, and modifiers are exposed via
    :mod:`rp2.asm_pio` (which re-exports :mod:`rp2.asm_pio_rp2040`), and
    that module is the single source of truth for their typing surface.
    """

    def __init__(
        self,
        *,
        out_init: int | List | None = ...,
        set_init: int | List | None = ...,
        sideset_init: int | List | None = ...,
        side_pindir: bool = ...,
        in_shiftdir: int = ...,
        out_shiftdir: int = ...,
        autopush: bool = ...,
        autopull: bool = ...,
        push_thresh: int = ...,
        pull_thresh: int = ...,
        fifo_join: int = ...,
    ) -> None: ...
    def __getattr__(self, name: str) -> Incomplete: ...
