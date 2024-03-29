from typing import Any

class MQTTClient:
    def __init__(self, *argv, **kwargs) -> None: ...
    DEBUG: bool
    def connect(self, *args, **kwargs) -> Any: ...
    def disconnect(self, *args, **kwargs) -> Any: ...
    def log(self, *args, **kwargs) -> Any: ...
    DELAY: int
    def delay(self, *args, **kwargs) -> Any: ...
    reconnect: Any
    publish: Any
    wait_msg: Any
    def set_callback(self, *args, **kwargs) -> Any: ...
    def set_last_will(self, *args, **kwargs) -> Any: ...
    def ping(self, *args, **kwargs) -> Any: ...
    def subscribe(self, *args, **kwargs) -> Any: ...
    def check_msg(self, *args, **kwargs) -> Any: ...
