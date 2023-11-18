import machine
from typing_extensions import assert_type


id = machine.unique_id()

# Bytes or bytearray ?
assert_type(id, bytes)

