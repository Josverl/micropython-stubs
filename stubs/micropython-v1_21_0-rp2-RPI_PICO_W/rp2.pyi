from _typeshed import Incomplete as Incomplete

def asm_pio(*args, **kwargs) -> Incomplete: ...
def asm_pio_encode(*args, **kwargs) -> Incomplete: ...
def bootsel_button(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...

class PIOASMEmit:
    def wrap(self, *args, **kwargs) -> Incomplete: ...
    def wait(self, *args, **kwargs) -> Incomplete: ...
    def jmp(self, *args, **kwargs) -> Incomplete: ...
    def word(self, *args, **kwargs) -> Incomplete: ...
    def in_(self, *args, **kwargs) -> Incomplete: ...
    def delay(self, *args, **kwargs) -> Incomplete: ...
    def start_pass(self, *args, **kwargs) -> Incomplete: ...
    def out(self, *args, **kwargs) -> Incomplete: ...
    def side(self, *args, **kwargs) -> Incomplete: ...
    def wrap_target(self, *args, **kwargs) -> Incomplete: ...
    def label(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def set(self, *args, **kwargs) -> Incomplete: ...
    def mov(self, *args, **kwargs) -> Incomplete: ...
    def push(self, *args, **kwargs) -> Incomplete: ...
    def pull(self, *args, **kwargs) -> Incomplete: ...
    def nop(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class PIOASMError(Exception): ...
