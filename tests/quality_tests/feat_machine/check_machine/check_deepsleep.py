# board : ESP32
# ref : https://docs.micropython.org/en/latest/esp32/quickref.html
import machine

# Deep-sleep mode


# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:  # stubs-ignore: port in ['samd','rp2']
    print("woke from a deep sleep")

# put the device to deep sleep for 10 seconds

#  samd has no machine.deepsleep() method
machine.deepsleep(10000)  # stubs-ignore: port=='samd'
# detect that deep sleep never returns
assert False, "Deep sleep never returns"
