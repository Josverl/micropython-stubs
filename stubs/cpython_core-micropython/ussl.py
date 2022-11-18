import micropython
import uio
import ssl


_ctx = ssl.create_default_context()


def wrap_socket(*args, **kw):
    s = _ctx.wrap_socket(*args, **kw)
    return uio.UioStream(s.makefile("rwb", buffering=0), is_bin=True)
