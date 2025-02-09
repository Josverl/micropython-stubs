import micropython


@micropython.native
def foo(self, arg):
    buf = self.linebuf  # Cached object
    # code


@micropython.native
def bar(self, arg) -> int:
    # code
    return 1


reveal_type(foo) 
reveal_type(bar) 
