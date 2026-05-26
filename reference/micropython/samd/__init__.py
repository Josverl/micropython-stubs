# MCU: {'variant': '', 'build': '', 'arch': 'armv7emsp', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'board_id': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.3', 'ver': '1.28.0', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'version': '1.28.0'}
# Stubber: v1.28.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import TypeAlias

from machine.Pin import _PinLike
from _mpy_shed import _BlockDeviceProtocol

_PinInfo_21: TypeAlias = tuple[str, int, int, int, int, int, int]
_PinInfo_51: TypeAlias = tuple[str, int, int, int, int, int, int, int, int]

# TODO: differentiate based on CPU 'cpu': 'SAMD51P19A' ?
def pininfo(pin_obj: _PinLike, /) -> _PinInfo_21 | _PinInfo_51:
    """Return SAMD pin assignment data.

    Args:
        pin: machine.Pin instance or a valid pin identifier accepted by Pin().

    Returns:
        tuple[str, int, ...] with pin assignment data. 

        The content depends on the SAMD family: 
            On SAMD21 -> (gpio_name, irq, adc0, serial1, serial2, pwm1_tc, pwm2)
            On SAMD51 -> (gpio_name, irq, adc0, adc1, serial1, serial2, tc, pwm1, pwm2)

    Notes:
        Integer value 255 means "not available" ("-").
        serial*/pwm*/tc entries are encoded as device/pad or device/output in one byte:
        (value >> 4, value & 0x0F).
    """
    ...


class Flash(_BlockDeviceProtocol):
    ...