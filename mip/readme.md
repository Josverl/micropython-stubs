# MicroPython's `typing.mpy` module

Why you may need typing.[m]py or typing_extensions.[m]py.

When making use of static typing in Python or MicroPython, you often end up using types that are defined in the CPython typing module.
As Python static typing is 'optimized out' when the source is compiled to byte-code and then to machine-code, there is virtually no runtime overhead.

However there is one remaining issue, and this is with the `import typing` or `from typing import ...`.
If you try to run an fully typed MicroPython module or script on a MCU, you will get an error like this:

```python
>>> import example
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 2, in <module>
ImportError: no module named 'typing'
```

A solution is to add a minimalistic `typing.py` file to the project, and when your module or script is executed on the MCU, that will be used in place of the CPython typing module.

## Install the `typing` modules to your MCU

To have the least amount of runtime overhead on your MCU, you should use the cross compiled version of the modules to your MCU.

```bash
mpremote mip install github:josverl/micropython-stubs/mip/typing.json
# or for the cross-compiled version:
mpremote mip install github:josverl/micropython-stubs/mip/typing_mpy.json
```

This will will output something like:

```text
Install github:josverl/micropython-stubs/mip/typing_mpy.json
Installing github:josverl/micropython-stubs/mip/typing_mpy.json to /lib
Installing: /lib/typing.mpy
Installing: /lib/typing_extensions.mpy
Installing __future__ (latest) from https://micropython.org/pi/v2 to /lib
Installing: /lib/__future__.mpy
Done
```

*Note:* The .mpy modules are cross compiled for MicroPython v1.25.0 ; mpy-cross emitting mpy v6.3.
*Note that by default mip will install the modules in the `/lib` folder of the MCU.*

## Add to your project source

To avoid needing to `mip install` the modules on every MCU, you can add the modules to your project source.
mpremote mip does not have a method to retrieve and store modules locally to your project, but it is simple to copy them from your MCU to your local project.

Assuming you have a project folder `src` and a `lib` folder in it, you can copy the modules from the MCU to your project with the following commands:

```bash
mpremote cp :lib/typing.mpy src/lib/typing.mpy
mpremote cp :lib/typing_extensions.mpy src/lib/typing_extensions.mpy
```

## Best portability

For best portability across MicroPython ports you can use the `typing.py` and `typing_extensions.py` modules. These modules are identical to the `typing.mpy` and `typing_extensions.mpy` modules, but are in source form.

Use the same commands as above, but replace the `.mpy` with `.py` in the commands.

## example code

```python
"""Example typed Micropython module."""
from typing import TYPE_CHECKING, Tuple


def foo(a: int, b: int) -> Tuple[int, str]:
    return a, str(b)

print("Hello, typed world!")
print(f"{foo(1, 2)=}")
```

### Using the `@no_type_check` decorator with `@asm_xxx`code

**`@asm_pio` functions**
As RP2 ASM PIO code is not exactly valid Python code, type checkers will show multiple warnings for those code sections.
It is possible to disable these warnings for the specific sections of code by using the `@no_type_check` decorator.

The `@typing.no_type_check` decorator may be supported by type checkers
for functions and classes.

If a type checker supports the `no_type_check` decorator for functions, it
should suppress all type errors for the `def` statement and its body including
any nested functions or classes. It should also ignore all parameter
and return type annotations and treat the function as if it were unannotated.

```python
import typing
import rp2

@typing.no_type_check
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink_1hz():
    # Cycles: 1 + 7 + 32 * (30 + 1) = 1000
    set(pins, 1)
    set(x, 31)                              [6]
    label("delay_high")
    nop()                                   [29]
    jmp(x_dec, "delay_high")
    # ...
```

Typechecking for rp2040 `@asm_pio` code, but has been integrated in the published type stubs for rp2 (`micropython-rp2-stubs`).

**The same can be used for `@micropython.asm_thumb` functions**

```python
import typing
import micropython

@typing.no_type_check
@micropython.asm_thumb
def convert2PWM(r0,r1,r2):
    #r3=32768
    mov(r3,1)
    mov(r4,15)
    lsl(r3,r4)
    # 8bits or 10 bit PWM
    mov(r4,255)
    cmp(r2,10)
    bne(PWM8BITS)
    #...
```

## About the modules

### `typing.py`

A minimalistic `typing.py` module for MicroPython.

:::{note}
*When that PR is merged, or MicroPython itself can provide this functionality, I'll update the above links to point to micropython-lib.*
:::

### `typing_extensions.py`

This module is provided to allow the use of older versions of Python (3.7+).

In CPython the `typing_extensions` module provide back-ported type hints from newer versions and enable use of new type system features on older Python versions.
For example, `typing.TypeGuard` is new in Python 3.10, but typing_extensions allows users on previous Python versions to use it too.

As MicroPython has no native typing implementation, the `typing_extensions.py` module provides identical functionality to the `typing.py` module.

## Cross Compiling

In order to create the smallest possible `.mpy` versions of the typing modules use:

```sh
cd mip
mpy-cross typing.py -O3
mpy-cross typing_extensions.py -O3
```

### Origin

The typing modules are the result of the collaboration of the MicroPython community around a PR to the micropython-lib repository.

PR: [micropython-lib:PR584](https://github.com/micropython/micropython-lib/pull/584)
Authors: [stinos](https://github.com/stinos) & [Andrew Leech](https://github.com/andrewleech)

### References

- Python: [typing — Support for type hints](https://docs.python.org/3/library/typing.html)
- PyPI: [typing_extensions — Type hints for Python](https://pypi.org/project/typing-extensions/)
- MicroPython: [`mpremote mip`](https://docs.micropython.org/en/latest/reference/packages.html#installing-packages-with-mpremote)
- [MicroPython-lib](https://github.com/micropython/micropython-lib)
