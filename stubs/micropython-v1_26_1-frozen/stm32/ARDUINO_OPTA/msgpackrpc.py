# This file is part of the msgpack-rpc module.
# Copyright (c) 2023 Arduino SA
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
# MessagePack RPC protocol implementation for MicroPython.
# https://github.com/msgpack-rpc/msgpack-rpc/blob/master/spec.md

import logging
import openamp
import msgpack
from micropython import const
from io import BytesIO
from time import sleep_ms, ticks_ms, ticks_diff

_MSG_TYPE_REQUEST = 0
_MSG_TYPE_RESPONSE = 1
_MSG_TYPE_NOTIFY = 2


def log_level_enabled(level):
    return logging.getLogger().isEnabledFor(level)


class Future:
    def __init__(self, msgid, msgbuf, fname, fargs):
        self.msgid = msgid
        self.msgbuf = msgbuf
        self.fname = fname
        self.fargs = fargs

    def join(self, timeout=0):
        if log_level_enabled(logging.DEBUG):
            logging.debug(f"join {self.fname}()")

        if timeout > 0:
            t = ticks_ms()

        while self.msgid not in self.msgbuf:
            if timeout > 0 and ticks_diff(ticks_ms(), t) > timeout:
                raise OSError(f"Timeout joining function {self.fname}")
            sleep_ms(100)

        obj = self.msgbuf.pop(self.msgid)
        if obj[2] is not None:
            raise (OSError(obj[2]))

        if log_level_enabled(logging.DEBUG):
            logging.debug(f"call {self.fname}({self.fargs}) => {obj}")
        return obj[3]


class MsgPackIO:
    def __init__(self):
        self.stream = BytesIO()

    def feed(self, data):
        offset = self.stream.tell()
        self.stream.write(data)
        self.stream.seek(offset)

    def readable(self):
        if self.stream.read(1):
            offset = self.stream.tell()
            self.stream.seek(offset - 1)
            return True
        return False

    def truncate(self):
        if self.readable():
            offset = self.stream.tell()
            self.stream = BytesIO(self.stream.getvalue()[offset:])

    def __iter__(self):
        return self

    def __next__(self):
        offset = self.stream.tell()
        try:
            obj = msgpack.unpack(self.stream)
            self.truncate()
            return obj
        except Exception:
            self.stream.seek(offset)
            raise StopIteration


class MsgPackRPC:
    def __init__(self, streaming=False):
        """
        Create a MsgPack RPC object.
        streaming: If True, messages can span multiple buffers, otherwise a buffer contains
        exactly one full message. Note streaming mode is slower, so it should be disabled
        if it's not needed.
        """
        self.epts = {}
        self.msgid = 0
        self.msgbuf = {}
        self.msgio = MsgPackIO() if streaming else None
        self.callables = {}

    def _bind_callback(self, src, name):
        if log_level_enabled(logging.INFO):
            logging.info(f'New service announcement src: {src} name: "{name}"')
        self.epts[name] = openamp.Endpoint(name, self._recv_callback, dest=src)
        self.epts[name].send(b"\x00")

    def _recv_callback(self, src, data):
        if log_level_enabled(logging.DEBUG):
            logging.debug(f"Received message on endpoint: {src} data: {bytes(data)}")

        if self.msgio is None:
            obj = msgpack.unpackb(data)
            self._process_unpacked_obj(obj)
        else:
            self.msgio.feed(data)
            for obj in self.msgio:
                self._process_unpacked_obj(obj)

    def _process_unpacked_obj(self, obj):
        if obj[0] == _MSG_TYPE_RESPONSE:
            self.msgbuf[obj[1]] = obj
        elif obj[0] == _MSG_TYPE_REQUEST:
            self._dispatch(obj[1], obj[2], obj[-1])
        if log_level_enabled(logging.DEBUG):
            logging.debug(f"Unpacked {type(obj)} val: {obj}")

    def _send_msg(self, msgid, msgtype, fname, fargs, **kwargs):
        timeout = kwargs.pop("timeout", 1000)
        endpoint = kwargs.pop("endpoint", "rpc")
        self.epts[endpoint].send(msgpack.packb([msgtype, msgid, fname, fargs]), timeout=timeout)
        if msgtype == _MSG_TYPE_REQUEST:
            self.msgid += 1
            return Future(msgid, self.msgbuf, fname, fargs)

    def _dispatch(self, msgid, fname, fargs):
        retobj = None
        error = None

        if fname in self.callables:
            retobj = self.callables[fname](*fargs)
        else:
            error = "Unbound function called %s" % (fname)

        self._send_msg(msgid, _MSG_TYPE_RESPONSE, error, retobj)

    def bind(self, name, obj):
        """
        Bind a callable or an object to a name.
        name: The name to which the callable or object is bound.
        obj: A callable or an object to bind to the name. If an object is passed, all of its
        public methods will be bound to their respective qualified names.
        """
        if callable(obj):
            # Bind a single callable to its name.
            self.callables[name] = obj
        else:
            # Bind all public methods of an object to their respective qualified names.
            for k, v in obj.__class__.__dict__.items():
                if callable(v) and not k.startswith("_"):
                    self.callables[name + "." + k] = getattr(obj, k)

    def start(self, firmware=None, num_channels=2, timeout=3000):
        """
        Initializes OpenAMP, loads the remote processor's firmware and starts.
        firmware: A path to an elf file stored in the filesystem, or an address to an entry point in flash.
        num_channels: The number of channels to wait for the remote processor to
        create before starting to communicate with it.
        timeout: How long to wait for the remote processor to start, 0 means forever.
        """
        # Initialize OpenAMP and set the New Service callback.
        openamp.new_service_callback(self._bind_callback)

        # Keep a reference to the remote processor object, to stop the GC from collecting
        # it, which would call the finaliser and shut down the remote processor while it's
        # still being used.
        self.rproc = openamp.RemoteProc(firmware)
        self.rproc.start()

        # Wait for remote processor to announce the end points.
        t = ticks_ms()
        while len(self.epts) != num_channels:
            if timeout > 0 and ticks_diff(ticks_ms(), t) > timeout:
                raise OSError("timeout waiting for the remote processor to start")
            sleep_ms(10)

        # Introduce a brief delay to allow the M4 sufficient time
        # to bind remote functions before invoking them.
        sleep_ms(100)

    def call(self, fname, *args, **kwargs):
        """
        Synchronous call. The client is blocked until the RPC is finished.
        """
        return self.call_async(fname, *args, *kwargs).join()

    def call_async(self, fname, *args, **kwargs):
        """
        Asynchronous call. The client returns a Future object immediately.
        """
        return self._send_msg(self.msgid, _MSG_TYPE_REQUEST, fname, list(args), *kwargs)
