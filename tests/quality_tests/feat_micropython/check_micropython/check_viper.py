import micropython
from typing_extensions import assert_type

# The viper emitter accepts object, bool, int, uint, ptr, ptr8, ptr16 and ptr32 as
# parameter annotations; only object, bool, int and uint are valid return annotations.
# See py/nativeglue.c::mp_native_type_from_qstr and py/compile.c.


@micropython.viper
def unsigned_word() -> uint:
    return 0xFFFFFFFF


@micropython.viper
def is_set(flags: int) -> bool:
    return bool(flags & 1)


@micropython.viper
def signed_word(value: int) -> int:
    return value


@micropython.viper
def as_object(value: object) -> object:
    return value


@micropython.viper
def read_viper(buffer: bytearray, offset: int, address: ptr) -> uint:
    byte_pointer = ptr8(buffer)
    halfword_pointer = ptr16(buffer)
    word_pointer = ptr32(address)
    unsigned = uint(byte_pointer[offset])
    byte_pointer[offset] = unsigned
    halfword_pointer[offset] = unsigned
    word_pointer[offset] = unsigned
    value: int = byte_pointer[offset]
    value = unsigned
    assert_type(byte_pointer[offset], int)
    assert_type(halfword_pointer[offset], int)
    assert_type(word_pointer[offset], int)
    return unsigned


@micropython.viper
def plain_ptr_is_not_indexable(address: ptr) -> uint:
    # a plain `ptr` has no element size, so it must not be subscriptable
    return uint(address[0])  # type: ignore
