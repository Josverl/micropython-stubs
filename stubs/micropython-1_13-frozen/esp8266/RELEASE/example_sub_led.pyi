from typing import Any

led: Any
SERVER: str
CLIENT_ID: Any
TOPIC: bytes
state: int

def sub_cb(topic, msg) -> None: ...
def main(server=...) -> None: ...
