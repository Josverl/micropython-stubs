"""Run an async REPL and log data received on an extra USB serial port."""

import asyncio
import logging

import aiorepl
import usb.device
import usb.device.cdc

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("demo")


async def receive_usb(cdc):
    while True:
        if cdc.is_open():
            data = cdc.read(64)
            if data:
                log.info("USB received: %r", data)
        await asyncio.sleep_ms(100)


async def main():
    cdc = usb.device.cdc.CDCInterface()
    cdc.init(timeout=0)

    # Keep the built-in USB REPL and add a second serial port.
    usb.device.get().init(cdc, builtin_driver=True)
    log.info("USB configured; reconnect your serial terminal if needed.")
    log.info("Send text to the extra USB serial port to log it here.")

    await asyncio.gather(
        receive_usb(cdc),
        aiorepl.task(globals()),
    )


if __name__ == "__main__":
    asyncio.run(main())
