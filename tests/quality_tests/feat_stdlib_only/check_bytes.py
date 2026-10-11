from typing_extensions import LiteralString, assert_type

PING_MSG = b"ping"
channel = 5

check = PING_MSG + b"x"
check = PING_MSG + bytes([channel])

username = b"foo"
password = b"secret"
assert_type(b"{}:{}".format(username, password), bytes)
assert_type("{}:{}".format("foo", "secret"), LiteralString)
