import micropython

@micropython.native
def foo(self, arg):
    buf = self.linebuf # Cached object
    # code

