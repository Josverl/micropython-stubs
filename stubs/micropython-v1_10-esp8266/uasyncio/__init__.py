"""
Module: 'uasyncio.__init__' on esp8266 v1.10
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.10-8-g8b7039d7d on 2019-01-26', machine='ESP module with ESP8266')
# Stubber: 1.0.2


class CancelledError(Exception):
    """"""


DEBUG = 0


class EventLoop:
    """"""

    def call_at_(self, *args) -> Any:
        pass

    def call_later(self, *args) -> Any:
        pass

    def call_later_ms(self, *args) -> Any:
        pass

    def call_soon(self, *args) -> Any:
        pass

    def close(self, *args) -> Any:
        pass

    def create_task(self, *args) -> Any:
        pass

    def run_forever(self, *args) -> Any:
        pass

    def run_until_complete(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass

    def time(self, *args) -> Any:
        pass

    def wait(self, *args) -> Any:
        pass


class IORead:
    """"""

    def handle(self, *args) -> Any:
        pass


class IOReadDone:
    """"""

    def handle(self, *args) -> Any:
        pass


class IOWrite:
    """"""

    def handle(self, *args) -> Any:
        pass


class IOWriteDone:
    """"""

    def handle(self, *args) -> Any:
        pass


class PollEventLoop:
    """"""
