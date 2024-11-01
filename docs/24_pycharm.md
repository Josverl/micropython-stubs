(pycharm_config)=
# PyCharm Configuration

## Configure PyCharm to use the selected stub folders

PyCharm supports Python stub files, so the simplest option to enable it to 'understand' MicroPython is to install the micropython-stubs for your port/board from PyPi.  

```{figure} img/pycharm-completion-2.png

Example of code completion in Pycharm
```
<!-- TODO : Add GIF with some additional samples -->
## Install the stubs from PyPi.

Install the stubs as documented in [](project:#install-stubs)

Example: `pip install -U micropython-stm32-stubs==1.19.1.*`

If you have a `requirements-dev.txt` file you can add the stubs to it, and PyCharm will offer to install them automatically into the project's environment

```text
# requirements-dev.txt
micropython-stm32-stubs==1.19.1.*
```

After this Pycharm will use the stubs it finds in the (virtual) environment to help validate your code and provide hints.

## Check library imports

To check if the correct types are used for your imports you can 'hover' the mouse over the module of an import statement. 
Pycharm will show the module's docstring that will allow you to identify which stub is being used.

```{figure} img/pycharm-import.png
Hover over the import statement to see the module's docstring.
```

:::{note}
Although Pycharm's rendering of the docstrings is somewhat limited compared to VSCode, it  is still quite useful.
<!-- todo: explain what the limitations are -->
:::


### Disable typechecker warnings for RP2 PIO code
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



### Verify the paths

You can verify the paths used in your project by 

File > Settings > Project Settings 

> Project Structure 

This should list the selected folders with stubs as Source Folders  

```{figure} img/pycharm-settings.png
PyCharm Settings
```	
