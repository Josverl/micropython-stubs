# SD card
import os
from typing import Union

from typing_extensions import assert_type, reveal_type

# test is able to access uname named tuple
if os.uname().release == "1.13.0" and os.uname().version < "v1.13-103":
    raise NotImplementedError("MicroPython 1.13.0 cannot be stubbed")

# Check all uname fields
os_uname = os.uname()
print(os_uname.sysname)
print(os_uname.nodename)
print(os_uname.release)
print(os_uname.machine)
print(os_uname.version)

assert_type(os_uname.sysname, str)
assert_type(os_uname.nodename, str)
assert_type(os_uname.release, str)
assert_type(os_uname.machine, str)
assert_type(os_uname.version, str)
reveal_type(os_uname)
