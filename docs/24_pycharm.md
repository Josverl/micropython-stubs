# PyCharm

## Configure PyCharm to use the selected stub folders

PyCharm supports Python stub files, so the simplest option to enable it to 'understand' MicroPython is to install the micropython-stubs for your port/board from PyPi.  


![Code completions](img/pycharm-completion-2.png)  
ref: https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html#stub-type-hints

## Install the stubs from PyPi.

Install the stubs as documented in [using the stubs](20_using.md)

Example: `pip install -U micropython-stm32-stubs==1.19.1.*`

If you have a `requirements-dev.txt` file you can add the stubs to it, and PyCharm will offer to install them automatically.

```text
micropython-stm32-stubs==1.19.1.*
```

After this Pycharm will use the stubs to validate your code and provide hints.

Note that Pycharm's rendering of the docstrings is limited (compared to VSCode), but is still quite useful.

## Check library imports

To check if the correct types are used for your imports you can 'hover' the mouse over the module of an import statement. 
Pycharm will show the module's docstring that will allow you to identify which stub is being used.

![import](img/pycharm-import.png)

### Disable Pycharm warnings for RP2 PIO code

As the RP2 PIO code is not valid Python code, PyCharm will show multiple warnings for those code sections. 

Fortunatly PyCharm allows these to be silenced for these sections.
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

    # Cycles: 1 + 7 + 32 * (30 + 1) = 1000
    set(pins, 0)
    set(x, 31)                              [6]
    label("delay_low")
    nop()                                   [29]
    jmp(x_dec, "delay_low")
```



### Verify the paths

You can verify the paths used in your project by 

File > Settings > Project Settings 

> Project Structure 

This should list the selected folders with stubs as Source Folders  

![PyCharm Settings](img/pycharm-settings.png)
