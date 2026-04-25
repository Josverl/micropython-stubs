"""
IRQ object types, used in the machine, bluetooth, _rp2 and rp2 modules

_IRQ is a union of ESP-specific IRQ types and the generic mp_irq_type-based IRQ type
to allow the same stubs to support of the different ports of MicroPython.

"""

from typing import Type

from _typeshed import Incomplete
from typing_extensions import TypeAlias

class _IRQ_ESP32:
    def trigger(self) -> int: ...
    # ESP32 uses custom machine_pin_irq_type (no flags, enable, disable, init)

class _IRQ_ESP8266:
    def trigger(self) -> int: ...
    # ESP8266 uses custom pin_irq_type (no flags, enable, disable, init)

class _IRQ_GENERIC:
    # Generic mp_irq_type (ports/cc3200/misc/mpirq.c)
    # Python-facing methods: init, enable, disable, flags
    def init(self) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def flags(self) -> int: ...

# Backward compatibility aliases for existing references.
# Keep RP2 alias explicitly for compatibility with older stubs/type-checker caches.
# _IRQ_RP2 = _IRQ_GENERIC
# _IRQ_PYB = _IRQ_GENERIC
# _IRQ_ALIF = _IRQ_GENERIC
# _IRQ_SAMD = _IRQ_GENERIC
# _IRQ_MIMXRT = _IRQ_GENERIC


_IRQ: TypeAlias = Type[_IRQ_ESP32] | Type[_IRQ_ESP8266] | Type[_IRQ_GENERIC] | Incomplete
