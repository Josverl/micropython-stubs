import io

from _mpy_shed import IOBase_mp
from typing_extensions import assert_type

alloc_size = 512


buffer_1 = io.StringIO("hello world")
buffer_2 = io.BytesIO(b"some initial binary data: \x00\x01")
buffer_3 = io.StringIO(alloc_size)
buffer_4 = io.BytesIO(alloc_size)

assert_type(buffer_1.write("x"), int)
assert_type(buffer_1.getvalue(), str)
assert_type(buffer_1.read(), str)
assert_type(buffer_2.write(b"x"), int)
assert_type(buffer_2.getvalue(), bytes)
assert_type(buffer_2.read(), bytes)
buffer_1.seek(0)
buffer_2.seek(0)
buffer_1.close()
buffer_2.close()


def accepts_micropython_stream(stream: IOBase_mp) -> None:
    pass


accepts_micropython_stream(buffer_1)
accepts_micropython_stream(buffer_2)

stream = open("file")

buffer_5 = io.BufferedWriter(stream, 8)
print(buffer_5.write(bytearray(16)))


stream.close()
