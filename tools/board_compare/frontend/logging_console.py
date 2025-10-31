from logging import *

# from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING, Handler
from pyscript import window


class PyscriptHandler(Handler):
    def emit(self, record):
        # print(f"Emitting record with levelno={record.levelno} and handler level={self.level}")
        if record.levelno >= ERROR:
            log_func = window.console.error
        elif record.levelno >= WARNING:
            log_func = window.console.warn
        elif record.levelno >= INFO:
            log_func = window.console.info
        elif record.levelno >= DEBUG:
            log_func = window.console.debug
        else:
            log_func = window.console.trace

        log_func(self.format(record) if self.formatter else record.message)

