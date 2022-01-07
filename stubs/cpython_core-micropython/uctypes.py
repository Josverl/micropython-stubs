import ctypes


def bytearray_at(addr, sz):
    # TODO: Currently just copies contents as bytes, not mutable inplace
    return ctypes.string_at(addr, sz)
