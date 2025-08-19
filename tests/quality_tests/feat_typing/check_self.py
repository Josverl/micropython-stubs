from typing import Callable, Self


class BaseClass:
    def register(self, callback: Callable[[Self], None]) -> None: ...


def cb(x):
    pass


base = BaseClass()
base.register(cb)
