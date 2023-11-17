# -----------------------
# flashing led
# -----------------------
import time
from machine import I2C, Pin, freq

# blue led on pin 2
blue = Pin(5, Pin.OUT)

for x in range(20):
    blue.value(0)
    time.sleep_ms(100)
    blue.value(1)
    time.sleep_ms(100)

blue.value(0)

# ---------------------------
# Toggle pin(value)
# ---------------------------
for x in range(20):
    blue.value((not blue.value()))
    time.sleep_ms(100)

# -----------------------
# PWM Pulse Width Modulation
# -----------------------

import machine

BlueLED = machine.PWM(machine.Pin(26), freq=1, duty=50)

BlueLED.deinit()

# Fade LED
import time
import machine

BlueLED = machine.PWM(machine.Pin(26), freq=5000, duty=0)
for j in range(100):
    for i in range(100):
        BlueLED.duty(i)
        time.sleep(0.01)
    for i in range(100, 0, -1):
        BlueLED.duty(i)
        time.sleep(0.01)


# -----------------------
# run (another) script in the global scope
# The Python functions eval and exec invoke the compiler at runtime,
# which requires significant amounts of RAM
# NOTE: In most cases it is better to use a well formed module
# and import that module, and call any required functions.
# -----------------------
# TODO: support `.read` on open('somescript.py').read()
exec(open("somescript.py").read(), globals())  # type:ignore
exec(open("createstubs.py").read(), globals())  # type:ignore

# -----------------------
# set M5Stack speaker to off
# to avoid electonic whine when using pin 26 on PWM
# https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/pin
# -----------------------
from machine import Pin

# set speaker = Pin 25, output to 0 (silence)
speaker = Pin(25, Pin.OUT, value=0)


# -----------
# Snippet WiFI
# Start WiFi
# -----------
import network, time

wifi_ssid = "Bootcamp"
wifi_psk = "MicroPython"
wlan = network.WLAN(network.STA_IF)
tmo = 50
if not wlan.isconnected():
    print("connecting to network...")
    wlan.active(True)
    wlan.connect(wifi_ssid, wifi_psk)
    # Wait for WiFi connection
    while not wlan.isconnected():
        if tmo == 0:
            break
        # BlinkLed(led)
        print(".", end="")
        tmo -= 1
        time.sleep_ms(200)
    print()
if tmo != 0:
    print("network config:", wlan.ifconfig())
else:
    print("could not connect to WiFi")
    wlan.active(False)  # get the interface's IP/netmask/gw/DNS addresses


# ------------------------
# decode bytearray
# ------------------------

b = b"!A7B3\n"
b.decode("utf8")

import binascii


def decode(a: bytearray):
    "bytearray to string"
    return binascii.hexlify(a).decode()


# ----------
# Snippet: UniqueID
# retrieve The machines unique ID
# -----------
import machine, binascii

id_hex = machine.unique_id()
id_b = binascii.hexlify(id_hex)
# optional - decode to string, takes 2x memory
print("Unique ID: {}".format(decode(machine.unique_id())))


import machine, binascii

id_hex = machine.unique_id()
id_b = binascii.hexlify(id_hex)
# optional - decode to string, takes 2x memory
id_s = id_b.decode("utf-8")
print("Unique ID: {}".format(id_s))

# ------------------------
# Scan for accesspoints
# ------------------------
import network

nic = network.WLAN(network.STA_IF)
_ = nic.active(True)
# networks = nic.scan()
# sort on signal strength
networks = sorted(nic.scan(), key=lambda x: x[3], reverse=True)

_f = "{0:<32} {2:>8} {3:>8} {4:>8} {5:>8}"

print(_f.format("SSID", "bssid", "Channel", "Signal", "Authmode", "Hidden"))
for row in networks:
    print(_f.format(*row))

del _f

# ------------------------------
# String formatting
# https://pyformat.info/#simple
# -----------------------------

# basic New
"{} {}".format("one", "two")
# basic Old
"%s %s" % ("one", "two")

# print information from a list ( one star )
mylist = "Jos", "Verlinde"
print("{} {}".format(*mylist))


# print information from a dict ( two star , use named )
data = {"first": "Jos", "last": "Verlinde"}
print("{first} {last}".format(**data))
# or
"{first} {last}".format(first="Hodor", last="Hodor!")

# Padding and alligning strings
# Align right:
"{:>10}".format("test")

# Align left:
"{:10}".format("test")
# or
"{:<10}".format("test")

# format as type
"{:X}".format(511)

# Type	Meaning
# 'b'	Binary format. Outputs the number in base 2.
# 'c'	Character. Converts the integer to the corresponding unicode character before printing.
# 'd'	Decimal Integer. Outputs the number in base 10.
# 'o'	Octal format. Outputs the number in base 8.
# 'x'	Hex format. Outputs the number in base 16, using lower-case letters for the digits above 9.
# 'X'	Hex format. Outputs the number in base 16, using upper-case letters for the digits above 9.
# 'n'	Number. This is the same as 'd', except that it uses the current locale setting to insert the appropriate number separator characters.
# None	The same as 'd'.

# Padding numbers
# Similar to strings numbers can also be constrained to a specific width.
"{:4d}".format(42)


# For floating points the padding value represents the length of the complete output. In the example below we want our output to have at least 6 characters with 2 after the decimal point.
"{:6.2f}".format(3.141592653589793)
# leading zero
"{:06.2f}".format(3.141592653589793)


# For integer values providing a precision doesn't make much sense and is actually forbidden in the new style (it will result in a ValueError).
"{:04d}".format(42)

# Signed
"{:+4d}".format(42)

# Use a space character to indicate that negative numbers should be prefixed with a minus symbol and a leading space should be used for positive ones.
"{: d}".format((-23))


# try:
#     #main code
#     ...
# except e as identifier:
#     #handle error
#     ...

# raise an error
if 0:
    raise ValueError("A very specific bad thing happened.")

# Best practice in handling errors and logging:
import logging

logger = logging.getLogger(__name__)

try:
    # do_something_in_app_that_breaks_easily()
    a = 1 / 0
except Exception as error:
    logger.error(error)
    raise  # just this!

# -----------------------------------------
# handle specific OSErrors using e.args[0]
# -----------------------------------------
import errno
import os

# ensure a folder exists
try:
    os.mkdir("existing")
except OSError as e:
    if e.args[0] != errno.EEXIST:
        print(e, "unexpected error creating folder")


# ------------------------------
# mount SDCard MicroPython 1.11
# SDCard configuration
#  - Lolin32/TTGO 8 v1.8    SDCard(slot=1, width=4),                                        # SD mode 4 bit
#  - M5Stack Core           SDCard(slot=2, width=1, sck=18, miso=19, mosi=23, cs=4), "/sd") # SPI 1 bit
# https://docs.micropython.org/en/latest/library/machine.SDCard.html#esp32
# ------------------------------

import machine
import uos as os

# Mount SD to /sd
try:
    # Some boards have pulldown and/or LED on GPIO2, pullup avoids issues on TTGO 8 v1.8
    # machine.Pin(2,mode=machine.Pin.IN, pull=machine.Pin.PULL_UP)
    # os.mount(machine.SDCard(slot=1, width=4), "/sd")  # SD mode 4 bit

    # # SPI 1 bit M5Stack Core
    os.mount(machine.SDCard(slot=2, width=1, sck=18, miso=19, mosi=23, cs=4), "/sd")  # SPI 1 bit M5Stack Core
    print("SD Card mounted")
except OSError as e:
    if e.args[0] == 16:
        print("No SD Card found")


print(os.listdir("/"))
print(os.listdir("/sd"))


# ------------------------------
# convert a binary string to usable data
# For more information on format strings and endiannes, refer to
# https://docs.python.org/3.5/library/struct.html
# ------------------------------

import struct

# Packing values to bytes
# The first parameter is the format string. Here it specifies the data is structured
# with a single four-byte integer followed by two characters.
# The rest of the parareadings are the values for each item in order
binary_data = struct.pack("icc", 8499000, b"A", b"Z")
print(binary_data)


# When unpacking, you receive a tuple of all data in the same order
tuple_of_data = struct.unpack("icc", binary_data)
print(tuple_of_data)

##
import logging

x = "something"

logging.basicConfig(level=logging.DEBUG)
# log = logging.getLogger(__name__)
# in modules the __name__ variable can be used
log = logging.getLogger("<keyword>")

log.critical("critical debug message")
log.error("debug message")
log.warning("debug message")
log.info("debug message")
log.debug("debug value{}".format(x))





# example use
with SkeletonFixture() as fixture:
    fixture.method()


# --------------------------------------
# offline download modules
# --------------------------------------

# import the network module


# --------------------------------------
# Connect to the network (ESP32 / ESP8622)
# --------------------------------------




# -------------------------------------------------------------
#  Identifying the slowest section of code
# -------------------------------------------------------------
# This is a process known as profiling and is covered in textbooks and (for standard Python) supported by various software tools.
# For the type of smaller embedded application likely to be running on MicroPython platforms the slowest function or method can usually
# be established by judicious use of the timing ticks group of functions documented in utime. Code execution time can be measured in ms, us, or CPU cycles.
#
# The following enables any function or method to be timed by adding an @timed_function decorator:
import utime


def timed_function(f, *args, **kwargs):
    "enables any function or method to be timed by adding an @timed_function decorator"
    myname = str(f).split(" ")[1]

    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        print("Function {} Time = {:6.3f}ms".format(myname, delta / 1000))
        return result

    return new_func


@timed_function
def foo():
    pass


# -------------------------------------------------------------
# simple function result caching
# Ref: https://dbader.org/blog/python-memoization
# -------------------------------------------------------------
# decorator to ret
#


def memoize(func):
    "basic moemoization, will eat memory"
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


# example of  fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# exampleof speeded up fibonacci, ( just add decorator)
@memoize
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# -------------------------------------------------------------
# take a number of itemes from an iterable list / database / thing
# ref : https://anandology.com/python-practice-book/iterators.html#generators
# -------------------------------------------------------------


def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result


# -------------------------------------------------------------
#
# -------------------------------------------------------------
def isMicroPython() -> bool:
    "runtime test to determine full or micropython"
    # pylint: disable=unused-variable,eval-used
    try:
        # both should fail on micropython, just to be sure
        # a) https://docs.micropython.org/en/latest/genrst/syntax.html#spaces
        # b) https://docs.micropython.org/en/latest/genrst/builtin_types.html#bytes-with-keywords-not-implemented
        a = eval("1and 0")
        b = bytes("abc", encoding="utf8")
        return False
    except (NotImplementedError, SyntaxError):
        return True


print("MicroPython" if isMicroPython() else "python")

# -------------------------------------------------------------
#
# -------------------------------------------------------------
# M5 stick scan internal I2C bus
from machine import I2C, Pin

i2c = I2C(0, freq=400000, scl=Pin(22), sda=Pin(21))
i2c.scan()
