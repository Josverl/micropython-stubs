import uio

# from typing import Any, IO, Optional

alloc_size = 512

buffer_1 = uio.StringIO(alloc_size)  # stubs-ignore:  linter == "mypy"
buffer_2 = uio.BytesIO(alloc_size)  # stubs-ignore:  linter == "mypy"

stream = open("file")
buf = io.BufferedWriter(stream, 8)  # type: ignore # TODO stdlib.io "TextIOWrapper" is incompatible with "RawIOBase"
print(buf.write(bytearray(16)))

stream.close()
