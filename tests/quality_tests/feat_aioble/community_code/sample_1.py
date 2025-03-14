# https://github.com/micropython/micropython/issues/15269
# author: vladkvit

import micropython
from micropython import const
import asyncio

# import aiorepl
import aioble

from time import ticks_us

from machine import Pin
from machine import Timer

import bluetooth

# For exceptions in interrupt subroutines
micropython.alloc_emergency_exception_buf(100)

test_value = 0

# BT setup
GATT_UUID = "079b8c5b-2961-4287-ac4a-9c8bc70f7a6c"
_ENV_SENSE_UUID = bluetooth.UUID(GATT_UUID)
_ENV_SENSE_TEMP_UUID = bluetooth.UUID(GATT_UUID)
_ADV_APPEARANCE_GENERIC_THERMOMETER = const(768)
_ADV_INTERVAL_MS = 250_000

# Register GATT server.
temp_service = aioble.Service(_ENV_SENSE_UUID)
temp_characteristic = aioble.Characteristic(
    temp_service, _ENV_SENSE_TEMP_UUID, read=True, notify=True
)
aioble.register_services(temp_service)

debug_pin1 = Pin(1, Pin.OUT)
debug_pin2 = Pin(2, Pin.OUT)


def timer_isr(timer):
    debug_pin2.on()
    test_value = ticks_us()  # give MP something to do
    debug_pin2.off()


tim = Timer(0)
tim.init(freq=20000, callback=timer_isr)


async def timer_task_f(event):
    while True:
        await asyncio.sleep_ms(4)
        event.set()


async def sensor_task(event):
    my_buf = bytearray(100 + 4)

    while True:
        debug_pin1.on()
        temp_characteristic.write(my_buf, send_update=True)
        debug_pin1.off()

        await event.wait()
        event.clear()


async def peripheral_task():
    while True:
        async with await aioble.advertise(
            _ADV_INTERVAL_MS,
            name="mpy-temp",
            services=[_ENV_SENSE_UUID],
            appearance=_ADV_APPEARANCE_GENERIC_THERMOMETER,
        ) as connection:
            print("Connection from", connection.device)
            await connection.disconnected(timeout_ms=None)


async def main():
    # repl = asyncio.create_task(aiorepl.task())

    timer_event = asyncio.Event()
    timer_task = asyncio.create_task(timer_task_f(timer_event))
    t1 = asyncio.create_task(sensor_task(timer_event))
    t2 = asyncio.create_task(peripheral_task())
    await asyncio.gather(t1, t2, timer_task)


asyncio.run(main())
