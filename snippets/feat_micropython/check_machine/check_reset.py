# board : ESP32
# ref : https://docs.micropython.org/en/latest/esp32/quickref.html
import machine

# put the device to deep sleep for 10 seconds

machine.reset()  # type: ignore
# detect that reset never returns
assert False, "reset never returns"
