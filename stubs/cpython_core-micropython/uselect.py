import selectors


POLLIN = selectors.EVENT_READ
POLLOUT = selectors.EVENT_WRITE


class poll:

    def __init__(self):
        self.sel = selectors.DefaultSelector()

    def register(self, stream, events, userdata=None):
        try:
            self.sel.register(stream, events, userdata)
            return True
        except KeyError:
            self.sel.modify(stream, events, userdata)
            return False

    def ipoll(self, timeout=-1):
        if timeout == -1:
            timeout = None
        else:
            timeout /= 1000
        for key, events in self.sel.select(timeout):
            yield (key.fileobj, events, key.data)
