# board : ESP32
# ref : https://docs.micropython.org/en/latest/esp32/quickref.html
# Deep-sleep mode
import machine
from typing_extensions import TYPE_CHECKING, assert_never, assert_type

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    assert_type(machine.reset_cause(), int)
    print("woke from a deep sleep")

machine.lightsleep(10000)


# put the device to sleep for 10 seconds
def deepsleep(msec: int) -> None:
    machine.deepsleep(msec)
    assert_never(msec)
    # mpyp issue https://github.com/python/mypy/issues/15467
