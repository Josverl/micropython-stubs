PING_MSG = b"ping"
channel = 5

check = PING_MSG + b"x"
check = PING_MSG + bytes([channel])  # type: ignore #TODO Operator "+" not supported for types "Literal[b"ping"]" and "bytes"
