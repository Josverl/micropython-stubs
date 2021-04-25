def const(x):
    return x

def native(x):
    return x

def viper(x):
    return x


# Override standard CPython modules/builtins with MicroPython semantics

import builtins

import uio
builtins.open = uio.open


import gc

def mem_free():
    return 1000000

def mem_alloc():
    return 1000000

gc.mem_free = mem_free
gc.mem_alloc = mem_alloc
