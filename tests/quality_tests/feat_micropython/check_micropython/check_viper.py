import micropython

# https://docs.micropython.org/en/v1.20.0/reference/speed_python.html?highlight=viper#the-viper-code-emitter
# Casting operators are currently: int, bool, uint, ptr, ptr8, ptr16 and ptr32.
# todo: micropython.viper - add support for casting operators


@micropython.viper
def foo(self, arg: int) -> int:
    buf = ptr8(self.linebuf)  # type: ignore 
    for x in range(20, 30):
        bar = buf[x]  # Access a data item through the pointer
        # code omitted

    return len(buf)  # Return an integer value
