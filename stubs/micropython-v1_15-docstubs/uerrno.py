"""
system error codes. See: https://docs.micropython.org/en/v1.15/library/uerrno.html

|see_cpython_module| :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""

# source version: v1.15
# origin module:: micropython/docs/library/uerrno.rst
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union
#     Error codes, based on ANSI C/POSIX standard. All error codes start with
#     "E". As mentioned above, inventory of the codes depends on
#     :term:`MicroPython port`. Errors are usually accessible as ``exc.args[0]``
#     where ``exc`` is an instance of `OSError`. Usage example::
# 
#         try:
#             uos.mkdir("my_dir")
#         except OSError as exc:
#             if exc.args[0] == uerrno.EEXIST:
#                 print("Directory already exists")
EEXIST : Any
#     Error codes, based on ANSI C/POSIX standard. All error codes start with
#     "E". As mentioned above, inventory of the codes depends on
#     :term:`MicroPython port`. Errors are usually accessible as ``exc.args[0]``
#     where ``exc`` is an instance of `OSError`. Usage example::
# 
#         try:
#             uos.mkdir("my_dir")
#         except OSError as exc:
#             if exc.args[0] == uerrno.EEXIST:
#                 print("Directory already exists")
EAGAIN : Any
#     Dictionary mapping numeric error codes to strings with symbolic error
#     code (see above)::
# 
#         >>> print(uerrno.errorcode[uerrno.EEXIST])
#         EEXIST
errorcode : Dict
