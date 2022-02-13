"""
system error codes. See: https://docs.micropython.org/en/latest/library/errno.html

|see_cpython_module| :mod:`python:errno` https://docs.python.org/3/library/errno.html .

This module provides access to symbolic error codes for `OSError` exception.
A particular inventory of codes depends on :term:`MicroPython port`.
"""

# source version: latest
# origin module:: micropython/docs/library/errno.rst
from typing import Any, Dict

#     Error codes, based on ANSI C/POSIX standard. All error codes start with
#     "E". As mentioned above, inventory of the codes depends on
#     :term:`MicroPython port`. Errors are usually accessible as ``exc.errno``
#     where ``exc`` is an instance of `OSError`. Usage example::
#
#         try:
#             os.mkdir("my_dir")
#         except OSError as exc:
#             if exc.errno == errno.EEXIST:
#                 print("Directory already exists")
EEXIST: Any = ...
#     Error codes, based on ANSI C/POSIX standard. All error codes start with
#     "E". As mentioned above, inventory of the codes depends on
#     :term:`MicroPython port`. Errors are usually accessible as ``exc.errno``
#     where ``exc`` is an instance of `OSError`. Usage example::
#
#         try:
#             os.mkdir("my_dir")
#         except OSError as exc:
#             if exc.errno == errno.EEXIST:
#                 print("Directory already exists")
EAGAIN: Any = ...
#     Dictionary mapping numeric error codes to strings with symbolic error
#     code (see above)::
#
#         >>> print(errno.errorcode[errno.EEXIST])
#         EEXIST
errorcode: Dict
