(rp2_asm)=
# Type check PIO code using the @rp2_asm decorator  


## enable type checking for RP2 PIO code
The @rp2.asm_pio decorator allows you to define custom PIO programs in MicroPython, making it easier to control low-level I/O operations on RP2-based boards. By placing your assembly code within this decorator, you can write PIO instructions in Python format and leverage the PIO state machines for tasks like precise timing and parallel data handling, all without leaving the comfort of Python.

PIO instructions do not follow standard Python syntax, so most type checkers cannot parse them by default. This assembly-like approach is specific to the PIO hardware and relies on features not recognized by typical Python tools.

To enable type checking for PIO code, you can the following block  before the first `@rp2.asm_pio` function.  

```py 
# -----------------------------------------------
# add type hints for the rp2.asm_pio PIO Instructions
try: 
    from typing_extensions import TYPE_CHECKING # type: ignore
except ImportError:
    TYPE_CHECKING = False
if TYPE_CHECKING:
    from rp2.asm_pio import *
# -----------------------------------------------
```

This block of code does the following:

 - Tries to import TYPE_CHECKING from typing_extensions. when the code runs , this will fail , and sets TYPE_CHECKING to False. 
 - If TYPE_CHECKING is True, that means that a type-checker is assessing the code , and it imports all the necessary types from rp2.asm_pio.
   This ensures that type checkers can understand the PIO instructions, even though they do not follow standard Python syntax. 
   This is useful for catching errors in your PIO code before running it on your RP2 board.

the current instructions are for the `RP2040` processor, used by the `RPI_PICO`. 
They do not (yet) include instructions for the `RP2350` processor, used by the `RPI_PICO2`.


There are a number of  side effects such as the introduction of a number of keywords in the global scope , that do not actually exist.
I have not found a way to have the type checkers enable it by default, or to reduce the scope to just the asm_pio methods.


## Disable typechecker warnings for RP2 PIO code

As  RP2 ASM PIO code is not exactly valid Python code, typecheckes will show multiple warnings for those code sections. 
It is possible to disable these warnings for the specific sections of code by using the `@no_type_check` decorator.

    When applied to a function, `@no_type_check` indicates that static type
    checkers should suppress all type-related errors within that function. From the
    perspective of a caller, all of the function's parameters and return type are
    always assumed to be Any, even if they are otherwise annotated or the type
    checker would normally infer the return type.

```python
from typing import no_type_check

@no_type_check
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


## PyCharm specific Configuration


### Disable Pycharm warnings for RP2 PIO code

There is also a pycharm specific way to disable warnings for specific sections of code.
To disable these warnings, add the following line to the top of the file or to the top of the function:

`# noinspection PyStatementEffect,PyArgumentList`

This will suppress the PyCharm warnings for that specific function

*Complete sample:*

```python
# noinspection PyStatementEffect,PyArgumentList
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



### Disable Pycharm warnings for RP2 PIO code

There is also a pycharm specific way to disable warnings for specific sections of code.
To disable these warnings, add the following line to the top of the file or to the top of the function:

`# noinspection PyStatementEffect,PyArgumentList`

This will suppress the PyCharm warnings for that specific function

*Complete sample:*

```python
# noinspection PyStatementEffect,PyArgumentList
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
