This folder is used to store packages for distribution using [`mpremote mip` or `mip``](https://docs.micropython.org/en/latest/reference/packages.html#installing-packages-with-mpremote) to the MCU.


## How to use

you only need to add this once (per project) 

```bash
mpremote mip install github:josverl/micropython-stubs/mip/typings.py@mip/typings

```

### `typing.py`

When using typing in Python or MicroPython, you often end up using types that are defined in the CPython typing module.
As python static typing is 'optimised out' when the source is compiled to byte-code and then to machine code, the typing module is not available in MicroPython.

However there is one remaining issue, and this is with the `import typing` or `from typing import ...` 
If yo try to run an fully typed script in MicroPython, you will get an error like this:

```python
>>> import example
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "example.py", line 2, in <module>
ImportError: no module named 'typing'
```
A solution is to add a `typing.py` file to the project, and if the module is executed on the MCU, this will be used instead of the CPython typing module.

Author: Andrew leech
Ref: https://github.com/micropython/micropython-lib/pull/584


### `typing_extensions.py`
In CPython the `typing_extensions` module provide backported type hints from newer versions and enable use of new type system features on older Python versions. 
For example, typing.TypeGuard is new in Python 3.10, but typing_extensions allows users on previous Python versions to use it too.

As MicroPython has no native typing implementation, the `typing_extensions.py` module is identical to the `typing.py` module.
