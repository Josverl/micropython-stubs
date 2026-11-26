
# ref: https://github.com/Josverl/micropython-stubber/issues/336
from sys import print_exception  
import sys

exc = Exception("boom")
print_exception(exc)
# sys.stdout and sys.stderr are typed as TextIO, and are valid destinations
print_exception(exc, sys.stdout)
print_exception(exc, sys.stderr)
