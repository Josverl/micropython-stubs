from typing import Any

CLIENT_ID: Any

class MQTTClient:
    def _recv_len() -> None: ...
    def _send_str() -> None: ...
    def check_msg() -> None: ...
    def connect() -> None: ...
    def disconnect() -> None: ...
    def ping() -> None: ...
    def publish() -> None: ...
    def set_callback() -> None: ...
    def set_last_will() -> None: ...
    def subscribe() -> None: ...
    def wait_msg() -> None: ...

class Pin:
    IN: int
    IRQ_FALLING: int
    IRQ_RISING: int
    OPEN_DRAIN: int
    OUT: int
    PULL_UP: int
    def init() -> None: ...
    def irq() -> None: ...
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...

SERVER: str
TOPIC: Any
button: Any
machine: Any

def main() -> None: ...

time: Any
ubinascii: Any