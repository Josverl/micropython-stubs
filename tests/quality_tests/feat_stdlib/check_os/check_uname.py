# SD card
import os
from typing import Union

from typing_extensions import assert_type, reveal_type

# test is able to access uname named tuple
if (
    os.uname().release == "1.13.0"  # stubs-ignore: port in ["samd"]
    and os.uname().version < "v1.13-103"  # stubs-ignore: port in ["samd"]
):
    raise NotImplementedError("MicroPython 1.13.0 cannot be stubbed")

# Check all uname fields
os_uname = os.uname()  # stubs-ignore: port in ["samd"]
print(os_uname.sysname)
print(os_uname.nodename)
print(os_uname.release)
print(os_uname.machine)
print(os_uname.version)

assert_type(os_uname.sysname, str)  # stubs-ignore: port in ["samd"]
assert_type(os_uname.nodename, str)  # stubs-ignore: port in ["samd"]
assert_type(os_uname.release, str)  # stubs-ignore: port in ["samd"]
assert_type(os_uname.machine, str)  # stubs-ignore: port in ["samd"]
assert_type(os_uname.version, str)  # stubs-ignore: port in ["samd"]

# reveal_type(os_uname)
