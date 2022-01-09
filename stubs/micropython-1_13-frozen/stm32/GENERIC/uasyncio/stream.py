# MicroPython uasyncio module
# MIT license; Copyright (c) 2019-2020 Damien P. George

from . import core


class Stream:
    def __init__(self, s, e={}):
        self.s = s
        self.e = e
        self.out_buf = b""

    def get_extra_info(self, v):
        return self.e[v]

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    def close(self):
        pass

    async def wait_closed(self):
        # TODO yield?
        self.s.close()

    async def read(self, n):
        yield core._io_queue.queue_read(self.s)
        return self.s.read(n)

    async def readexactly(self, n):
        r = b""
        while n:
            yield core._io_queue.queue_read(self.s)
            r2 = self.s.read(n)
            if r2 is not None:
                if not len(r2):
                    raise EOFError
                r += r2
                n -= len(r2)
        return r

    async def readline(self):
        l = b""
        while True:
            yield core._io_queue.queue_read(self.s)
            l2 = self.s.readline()  # may do multiple reads but won't block
            l += l2
            if not l2 or l[-1] == 10:  # \n (check l in case l2 is str)
                return l

    def write(self, buf):
        self.out_buf += buf

    async def drain(self):
        mv = memoryview(self.out_buf)
        off = 0
        while off < len(mv):
            yield core._io_queue.queue_write(self.s)
            ret = self.s.write(mv[off:])
            if ret is not None:
                off += ret
        self.out_buf = b""


# Stream can be used for both reading and writing to save code size
StreamReader = Stream
StreamWriter = Stream


# Create a TCP stream connection to a remote host
async def open_connection(host, port):
    from uerrno import EINPROGRESS
    import usocket as socket

    ai = socket.getaddrinfo(host, port)[0]  # TODO this is blocking!
    s = socket.socket()
    s.setblocking(False)
    ss = Stream(s)
    try:
        s.connect(ai[-1])
    except OSError as er:
        if er.args[0] != EINPROGRESS:
            raise er
    yield core._io_queue.queue_write(s)
    return ss, ss


# Class representing a TCP stream server, can be closed and used in "async with"
class Server:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        self.close()
        await self.wait_closed()

    def close(self):
        self.task.cancel()

    async def wait_closed(self):
        await self.task

    async def _serve(self, cb, host, port, backlog):
        import usocket as socket

        ai = socket.getaddrinfo(host, port)[0]  # TODO this is blocking!
        s = socket.socket()
        s.setblocking(False)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(ai[-1])
        s.listen(backlog)
        self.task = core.cur_task
        # Accept incoming connections
        while True:
            try:
                yield core._io_queue.queue_read(s)
            except core.CancelledError:
                # Shutdown server
                s.close()
                return
            try:
                s2, addr = s.accept()
            except:
                # Ignore a failed accept
                continue
            s2.setblocking(False)
            s2s = Stream(s2, {"peername": addr})
            core.create_task(cb(s2s, s2s))


# Helper function to start a TCP stream server, running as a new task
# TODO could use an accept-callback on socket read activity instead of creating a task
async def start_server(cb, host, port, backlog=5):
    s = Server()
    core.create_task(s._serve(cb, host, port, backlog))
    return s


################################################################################
# Legacy uasyncio compatibility


async def stream_awrite(self, buf, off=0, sz=-1):
    if off != 0 or sz != -1:
        buf = memoryview(buf)
        if sz == -1:
            sz = len(buf)
        buf = buf[off : off + sz]
    self.write(buf)
    await self.drain()


Stream.aclose = Stream.wait_closed
Stream.awrite = stream_awrite
Stream.awritestr = stream_awrite  # TODO explicitly convert to bytes?
