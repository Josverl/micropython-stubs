from _typeshed import Incomplete

led: Incomplete
SERVER: str
CLIENT_ID: Incomplete
TOPIC: bytes
state: int

def sub_cb(topic, msg) -> None: ...
def main(server=...) -> None: ...
