import io
from typing import IO, Any, Optional

alloc_size = 512


buffer_1 = io.StringIO("hello world") 
buffer_2 = io.BytesIO(b"some initial binary data: \x00\x01") # type: ignore # TODO 

stream = open("file")

buffer_3 = io.BufferedWriter(stream, 8)  # type: ignore # TODO stdlib.io "TextIOWrapper" is incompatible with "RawIOBase"
print(buffer_3.write(bytearray(16)))  # type: ignore # TODO  stdlib.io "bytearray" is incompatible with protocol "ReadableBuffer"


stream.close()
