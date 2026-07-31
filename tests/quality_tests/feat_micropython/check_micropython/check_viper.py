import micropython


@micropython.viper
def unsigned_word() -> uint:
    return 0xFFFFFFFF


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
    return unsigned
