"""
system error codes. See: https://docs.micropython.org/en/v1.20.0/library/errno.html

|see_cpython_module| :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""

# source version: v1_20_0
# origin module:: repos/micropython/docs/library/errno.rst
from typing import Any, Dict

EEXIST: Any = ...
"""\
Error codes, based on ANSI C/POSIX standard. All error codes start with
"E". As mentioned above, inventory of the codes depends on
:term:`MicroPython port`. Errors are usually accessible as ``exc.errno``
where ``exc`` is an instance of `OSError`. Usage example::

try:
os.mkdir("my_dir")
except OSError as exc:
if exc.errno == errno.EEXIST:
print("Directory already exists")
"""
EAGAIN: Any = ...
"""\
Error codes, based on ANSI C/POSIX standard. All error codes start with
"E". As mentioned above, inventory of the codes depends on
:term:`MicroPython port`. Errors are usually accessible as ``exc.errno``
where ``exc`` is an instance of `OSError`. Usage example::

try:
os.mkdir("my_dir")
except OSError as exc:
if exc.errno == errno.EEXIST:
print("Directory already exists")
"""
errorcode: Dict
"""\
Dictionary mapping numeric error codes to strings with symbolic error
code (see above)::

>>> print(errno.errorcode[errno.EEXIST])
EEXIST
"""
