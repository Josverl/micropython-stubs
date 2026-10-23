import io

import deflate
from typing_extensions import assert_type

with deflate.DeflateIO(io.BytesIO(b""), deflate.ZLIB) as stream:
    assert_type(stream, deflate.DeflateIO)
    stream.read()
