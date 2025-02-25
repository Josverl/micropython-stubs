# SD card
import os
from typing import Union

from typing_extensions import assert_type, reveal_type

# test is able to access uname named tuple
if (
    os.uname().release == "1.13.0"  # stubs-ignore: port in ["samd","webassembly"]
    and os.uname().version < "v1.13-103"  # stubs-ignore: port in ["samd","webassembly"]
):
    raise NotImplementedError("MicroPython 1.13.0 cannot be stubbed")

# Check all uname fields
os_uname = os.uname()  # stubs-ignore: port in ["samd","webassembly"]

reveal_type(os_uname)

print(os_uname.sysname)
print(os_uname.nodename)
print(os_uname.release)
print(os_uname.machine)
print(os_uname.version)

# issue: https://github.com/Josverl/micropython-stubs/issues/790
# assert_type(os_uname.sysname, str)  # stubs-ignore: port in ["samd"] or version < 1.24.0
# assert_type(os_uname.nodename, str)  # stubs-ignore: port in ["samd"] or version < 1.24.0
# assert_type(os_uname.release, str)  # stubs-ignore: port in ["samd"] or version < 1.24.0
# assert_type(os_uname.machine, str)  # stubs-ignore: port in ["samd"] or version < 1.24.0
# assert_type(os_uname.version, str)  # stubs-ignore: port in ["samd"] or version < 1.24.0
