import io

# from typing import IO, Any, Optional

alloc_size = 512

buffer_1 = io.StringIO(alloc_size)  # stubs-ignore: version<=1.18.0 or linter == "mypy"
buffer_2 = io.BytesIO(alloc_size)  # stubs-ignore: version<=1.18.0 or linter == "mypy"

stream = open("file")

buf = io.BufferedWriter(stream, 8)  # stubs-ignore:  linter == "mypy"
print(buf.write(bytearray(16)))


stream.close()
# FIXED:  file of type "BufferedWriter" cannot be used with "with" because it does not implement __enter__


with open("foo.bar", "wb") as f:  # stubs-ignore:  version < 1.24.0
    f.write(b"deadbeef")
