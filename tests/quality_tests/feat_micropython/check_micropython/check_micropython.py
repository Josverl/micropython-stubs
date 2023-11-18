"""
Code snippet used to validate the micropython stubs
modules: 
    Micropython 
"""

# const
import micropython
from micropython import const

ROWS = const(33)
_COLS = const(0x10)
a = ROWS
b = _COLS


@micropython.viper
def foo(arg: int) -> int:
    return arg << 2


@micropython.native
def bar(arg: int) -> int:
    return arg << 2


x = micropython.opt_level()
micropython.opt_level(x)


micropython.alloc_emergency_exception_buf(512)

micropython.mem_info()
micropython.qstr_info()
micropython.stack_use()
micropython.heap_lock()
micropython.heap_unlock()

micropython.kbd_intr("0x03")


# supply params to the function
def func(a):
    print(a)


arg = "foo"

micropython.schedule(func, arg)
