import io
from typing import IO, Any, Optional

alloc_size = 512


buffer_1 = io.StringIO("hello world") 
buffer_2 = io.BytesIO(b"some initial binary data: \x00\x01")

stream = open("file")

buffer_3 = io.BufferedWriter(stream, 8) # stubs-ignore : linter == "mypy"
print(buffer_3.write(bytearray(16)))


stream.close()
