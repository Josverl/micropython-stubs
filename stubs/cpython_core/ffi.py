# (c) 2019 Paul Sokolovsky. MIT license.
import ctypes
import array


class Func:

    def __init__(self, f, restype):
        self.f = f
        self.restype = restype

    def __call__(self, *args):

        def conv_arg(x):
            if isinstance(x, str):
                return x.encode()
            if isinstance(x, (bytearray, array.array)):
                a = ctypes.c_byte.from_buffer(x)
                return ctypes.addressof(a)
            return x

        args = [conv_arg(x) for x in args]
        #print(args)
        res = self.f(*args)
        if self.restype == "s":
            res = res.decode("utf-8")
        return res


class Var:

    def __init__(self, v):
        self.v = v

    def get(self):
        return self.v.value


class DynMod:

    typemap = {
        "v": None,
        "s": ctypes.c_char_p,
        "S": ctypes.c_char_p,
        "i": ctypes.c_int,
        "I": ctypes.c_uint,
        "l": ctypes.c_long,
        "L": ctypes.c_ulong,
        "q": ctypes.c_longlong,
        "Q": ctypes.c_ulonglong,
        "p": ctypes.c_void_p,
        "P": ctypes.c_void_p,
        "C": ctypes.c_void_p,
    }

    def __init__(self, name):
        self.mod = ctypes.CDLL(name)

    def func(self, ret, name, params):
        f = getattr(self.mod, name)
        argtypes = []
        for p in params:
            argtypes.append(self.typemap[p])
        #print(name, argtypes)
        f.argtypes = argtypes
        f.restype = self.typemap[ret]
        return Func(f, ret)

    def var(self, type, name):
        ctype = self.typemap[type]
        v = ctype.in_dll(self.mod, name)
        return Var(v)


def open(name):
    return DynMod(name)


def func(ret, addr, params):
    types = [DynMod.typemap[ret]]
    for p in params:
        types.append(DynMod.typemap[p])
    ftype = ctypes.CFUNCTYPE(*types)
    return ftype(addr)


def callback(ret, func, params):
    types = [DynMod.typemap[ret]]
    for p in params:
        types.append(DynMod.typemap[p])
    ftype = ctypes.CFUNCTYPE(*types)
    return ftype(func)
