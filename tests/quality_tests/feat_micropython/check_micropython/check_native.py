import micropython


@micropython.native
def foo(self, arg):
    buf = self.linebuf  # Cached object
    # code


@micropython.native
def bar(self, arg) -> int:
    # code
    return 1

try:
    reveal_type(foo)
    reveal_type(bar)
except Exception as e:
    pass
