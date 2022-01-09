import re

# In Pycopy's ure, "." matches newline by default, effectively
# as if DOTALL flag was used.

def compile(pattern, flags=0):
    return re.compile(pattern, flags | re.DOTALL)

def match(pattern, string):
    return re.match(pattern, string, re.DOTALL)

def search(pattern, string):
    return re.search(pattern, string, re.DOTALL)

def sub(pattern, repl, string, count=0, flags=0):
    return re.sub(pattern, repl, string, count, flags | re.DOTALL)
