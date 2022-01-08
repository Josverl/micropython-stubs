import re

# In MicroPython's ure, "." matches newline by default, effectively
# as if DOTALL flag was used.

def sub(pattern, repl, string, count=0, flags=0):
    return re.sub(pattern, repl, string, count, flags | re.DOTALL)
