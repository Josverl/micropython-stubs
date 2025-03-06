import sys 
from typing_extensions import assert_type

sys_implementation = sys.implementation
assert_type(sys_implementation.name, str)
# assert_type(sys_implementation.version, tuple)
# assert_type(sys_implementation._machine, str) 
# assert_type(sys_implementation._mpy, str) 
# assert_type(sys_implementation._build, str) 


