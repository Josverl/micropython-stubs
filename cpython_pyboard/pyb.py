# pyb adapted from micropython-pyb by Daryl Schults
# pylint: disable=unused-argument, redefined-outer-name, redefined-builtin, too-many-lines
def delay(ms):
    """
    Delay for the given number of milliseconds.
    """
    ...

def udelay(us):
    """
    Delay for the given number of microseconds.
    """
    ...

def millis():
    """
    Returns the number of milliseconds since the board was last reset.
    """
    ...

def micros():
    """
    Returns the number of microseconds since the board was last reset.
    """
    ...

def elapsed_millis(start):
    """
    Returns the number of milliseconds which have elapsed since ``start``.
    """
    ...

def elapsed_micros(start):
    """
    Returns the number of microseconds which have elapsed since ``start``.
    """
    ...

def hard_reset():
    """
    Resets the pyboard in a manner similar to pushing the external RESET
    button.
    """

def bootloader():
    #pylint: disable=anomalous-backslash-in-string
    """
    Activate the bootloader without BOOT\* pins.
    """
    ...

def disable_irq():
    """
    Disable interrupt requests.
    """
    ...


def enable_irq(state=True):
    """
    Enable interrupt requests.
    """
    ...

def freq(sysclk, hclk, pclk1, pclk2):
    """
    If given no arguments, returns a tuple of clock frequencies.
    """
    ...

def wfi():
    """
    Wait for an internal or external interrupt.
    """
    ...

def stop():
    """
    Put the pyboard in a "sleeping" state.
    """

def standby():
    """
    Put the pyboard into a "deep sleep" state.
    """
    ...

def info(dump_alloc_table):
    """
    Print out lots of information about the board.
    """
    ...

def main(filename):
    """
    Set the filename of the main script to run after boot.py is finished.
    """
    ...

def mount(device, mountpoint, readonly=False, mkfs=False):
    """
    Mount a block device and make it available as part of the filesystem.
    """
    ...

def repl_uart(uart):
    """
    Get or set the UART object where the REPL is repeated on.
    """
    ...

def rng():
    """
    Return a 30-bit hardware generated random number.
    """
    ...

def sync():
    """
    Sync all file systems.
    """
    ...

def unique_id():
    """
    Returns a string of 12 bytes (96 bits), which is the unique ID of the MCU.
    """
    ...

def usb_mode(modestr, vid=0xf055, pid=0x9801, hid=0):
    """
    If called with no arguments, return the current USB mode as a string.
    If called with modestr provided, attempts to set USB mode.
    """
    ...

class Accel:

    def filtered_xyz(self):
        """
        Get a 3-tuple of filtered x, y and z values.
        """
        ...

    def tilt(self):
        """
        Get the tilt register.
        """
        ...

    def x(self):
        """
        Get the x-axis value.
        """
        ...

    def y(self):
        """
        Get the y-axis value.
        """
        ...

    def z(self):
        """
        Get the z-axis value.
        """
        ...

    def write(self, register, value):
        ...

    def read(self, register):
        ...

class ADC:

    def __init__(self, pin):
        """
        Create an ADC object associated with the given pin.
        This allows you to then read analog values on that pin.
        """
        ...

    def read_timed_stop(self):
        ...

    def read(self):
        """
        Read the value on the analog pin and return it.  The returned value
        will be between 0 and 4095.
        """
        ...

    def read_timed(self, buf, timer):
        """
        Read analog values into ``buf`` at a rate set by the ``timer`` object.
        """
        ...

class CAN:

    NORMAL = "NORMAL"
    LOOPBACK = "LOOPBACK"
    SILENT = "SILENT"
    SILENT_LOOPBACK = "SILENT_LOOPBACK"

    LIST16 = "LIST16"
    MASK16 = "MASK16"
    LIST32 = "LIST32"
    MASK32 = "MASK32"

    def __init__(self, bus, mode=None, extframe=False, prescaler=100, sjw=1, bs1=6, bs2=8):
        """
        Construct a CAN object on the given bus.
        """
        ...

    @classmethod
    def initfilterbanks(cls, nr):
        """
        Reset and disable all filter banks and assign how many banks should be available for CAN(1).
        """
        ...

    def init(self, mode, extframe=False, prescaler=100, sjw=1, bs1=6, bs2=8):
        """
        Initialise the CAN bus with the given parameters
        """
        ...

    def deinit(self):
        """
        Turn off the CAN bus.
        """
        ...

    def setfilter(self, bank, mode, fifo, params, rtr):
        """
        Configure a filter bank
        """
        ...

    def clearfilter(self, bank):
        """
        Clear and disables a filter bank.
        """
        ...

    def any(self, fifo):
        """
        Return True if any message waiting on the FIFO, else False.
        """
        ...

    def recv(self, fifo, timeout=5000):
        """
        Receive data on the bus.
        """
        ...

    def send(self, data, id, timeout=0, rtr=False):
        """
        Send a message on the bus.
        """
        ...

    def rxcallback(self, fifo, fun):
        """
        Register a function to be called when a message is accepted into a empty fifo:
        """
        ...

class DAC:

    NORMAL = "NORMAL"
    CIRCULAR = "CIRCULAR"

    def __init__(self, port, bits=8):
        """
        Construct a new DAC object.
        """
        ...

    def init(self, bits=8):
        """
        Reinitialise the DAC.  ``bits`` can be 8 or 12.
        """
        ...

    def deinit(self):
        """
        De - initialise the DAC making its pin available for other uses.
        """

    def noise(self, freq):
        """
        Generate a pseudo-random noise signal.
        """
        ...

    def triangle(self, freq):
        """
        Generate a triangle wave.
        """
        ...

    def write(self, value):
        """
        Direct access to the DAC output.
        """
        ...

    def write_timed(self, data, freq, mode=NORMAL):
        """
        Initiates a burst of RAM to DAC using a DMA transfer.
        """
        ...

class ExtInt:

    IRQ_FALLING = "IRQ_FALLING"
    IRQ_RISING = "IRQ_RISING"
    IRQ_RISING_FALLING = "IRQ_RISING_FALLING"

    def __init__(self, pin, mode, pull, callback):
        """
        Create an ExtInt object
        """
        ...

    @classmethod
    def regs(cls):
        """
        Dump the values of the EXTI registers.
        """

    def disable(self, ):
        """
        Disable the interrupt associated with the ExtInt object.
        This could be useful for debouncing.
        """
        ...

    def enable(self, ):
        """
        Enable a disabled interrupt.
        """
        ...

    def line(self, ):
        """
        Return the line number that the pin is mapped to.
        """
        ...

    def swint(self, ):
        """
        Trigger the callback from software.
        """
        ...

class I2C:

    MASTER = "MASTER"
    SLAVE = "SLAVE"

    def __init__(self, *args, **kwargs):
        """
        Construct an I2C object on the given bus.
        """
        ...

    def deinit(self):
        """
        Turn off the I2C bus.
        """
        ...

    def init(self, mode, addr=0x12, baudrate=400000, gencall=False):
        """
        Initialise the I2C bus with the given parameters.
        """
        ...

    def is_ready(self, addr):
        """
        Check if an I2C device responds to the given address.  Only valid when in master mode.
        """
        ...

    def mem_read(self, data, addr, memaddr, timeout=5000, addr_size=8):
        """
        Read from the memory of an I2C device.
        """
        ...

    def mem_write(self, data, addr, memaddr, timeout=5000, addr_size=8):
        """
        Write to the memory of an I2C device.
        """
        ...

    def recv(self, recv, addr=0x00, timeout=5000):
        """
        Receive data on the bus.
        """
        ...

    def send(self, send, addr=0x00, timeout=5000):
        """
        Send data on the bus.
        """
        ...

    def scan(self):
        """
        Scan all I2C addresses from 0x01 to 0x7f and return a list of those that respond.
        """
        ...

class LCD:

    def __init__(self, skin_position):
        """
        Construct an LCD object in the given skin position.  ``skin_position`` can be 'X' or 'Y', and
        should match the position where the LCD pyskin is plugged in.
        """
        ...

    def command(self, instr_data, buf):
        """
        Send an arbitrary command to the LCD.  ... 0 for ``instr_data`` to send an
        instruction, otherwise ... 1 to send data.  ``buf`` is a buffer with the
        instructions/data to send.
        """

    def contrast(self, value):
        """
        Set the contrast of the LCD.  Valid values are between 0 and 47.
        """
        ...

    def fill(self, colour):
        """
        Fill the screen with the given colour (0 or 1 for white or black).
        """
        ...

    def get(self, x, y):
        """
        Get the pixel at the position ``(x, y)``.  Returns 0 or 1.
        """
        ...

    def light(self, value):
        """
        Turn the backlight on/off.  True or 1 turns it on, False or 0 turns it off.
        """
        ...

    def pixel(self, x, y, colour):
        """
        Set the pixel at ``(x, y)`` to the given colour (0 or 1).
        """
        ...

    def show(self, ):
        """
        Show the hidden buffer on the screen.
        """
        ...

    def text(self, str, x, y, colour):
        """
        Draw the given text to the position ``(x, y)`` using the given colour (0 or 1).
        """
        ...

    def write(self, str):
        """
        Write the string ``str`` to the screen.  It will appear immediately.
        """
        ...


class LED:
    def __init__(self, id):
        """
        Create an LED object associated with the given LED
        """
        ...

    def intensity(self, value):
        """
        Get or set the LED intensity.  Intensity ranges between 0 (off) and 255 (full on).
        """

    def off(self, ):
        """
        Turn the LED off.
        """
        ...

    def on(self, ):
        """
        Turn the LED on, to maximum intensity.
        """
        ...

    def toggle(self, ):
        """
        Toggle the LED between on (maximum intensity) and off.
        """
        ...

class _board(object):
    """ object has any attribute, returns 1 for requested attribute's value """
    def __getattr__(self, *args, **kwargs):
        return 1

class Pin:

    AF_OD = "AF_OD"
    AF_PP = "AF_PP"
    ANALOG = "ANALOG"
    IN = "IN"
    OUT = "OUT"
    OUT_OD = "OUT_OD"
    OUT_PP = "OUT_PP"
    PULL_DOWN = "PULL_DOWN"
    PULL_NONE = "PULL_NONE"
    PULL_UP = "PULL_UP"
    board = _board()
    cpu = _board()


    def __init__(self, *args, **kwargs):
        """
        Create a new Pin object associated with the id.
        """
        ...

    @classmethod
    def debug(cls, state):
        """
        Get or set the debugging state (``True`` or ``False`` for on or off).
        """
        ...

    @classmethod
    def dict(cls, dict):
        """
        Get or set the pin mapper dictionary.
        """
        ...

    @classmethod
    def mapper(cls, fun):
        """
        Get or set the pin mapper function.
        """
        ...

    def init(self, mode, pull=PULL_NONE, af=-1):
        """
        Initialise the pin:
        """
        ...

    def value(self, value):
        """
        Get or set the digital logic level of the pin.
        """
        ...

    def __str__(self):
        """
        Return a string describing the pin object.
        """
        ...

    def af(self):
        """
        Returns the currently configured alternate-function of the pin.
        """
        ...

    @classmethod
    def af_list(cls):
        """
        Returns an array of alternate functions available for this pin.
        """
        ...

    def gpio(self):
        """
        Returns the base address of the GPIO block associated with this pin.
        """
        ...

    def mode(self):
        """
        Returns the currently configured mode of the pin.
        """
        ...

    def name(self):
        """
        Get the pin name.
        """
        ...

    def names(self):
        """
        Returns the cpu and board names for this pin.
        """
        ...

    def pin(self):
        """
        Get the pin number.
        """
        ...

    def port(self):
        """
        Get the pin port.
        """
        ...

    def pull(self):
        """
        Returns the currently configured pull of the pin.
        """
        ...

class PinAF:

    def __str__(self):
        """
        Return a string describing the alternate function.
        """
        ...

    def index(self):
        """
        Return the alternate function index.
        """
        ...

    def name(self):
        """
        Return the name of the alternate function.
        """
        ...

    def reg(self):
        """
        Return the base register associated with the peripheral assigned to this
        alternate function.
        """
        ...

class RTC:

    def __init__(self):
        """
        Create an RTC object.
        """
        ...

    def datetime(self, datetimetuple):
        """
        Get or set the date and time of the RTC.
        """
        ...

    def wakeup(self, timeout, callback=None):
        """
        Set the RTC wakeup timer to trigger repeatedly at every ``timeout``
        milliseconds.
        """
        ...

    def info(self):
        """
        Get information about the startup time and reset source.
        """
        ...

    def calibration(self, cal):
        """
        Get or set RTC calibration.
        """
        ...

class Servo:

    def __init__(self, id):
        """
        Create a servo object.  ``id`` is 1-4, and corresponds to pins X1 through X4.
        """
        ...

    def angle(self, angle, time=0):
        """
        If no arguments are given, this function returns the current angle.
        """
        ...

    def speed(self, speed, time=0):
        """
        If no arguments are given, this function returns the current speed.
        """
        ...

    def pulse_width(self, value):
        """
        If no arguments are given, this function returns the current raw pulse-width
        value.
        """
        ...

    def calibration(self, pulse_min, pulse_max, pulse_centre, pulse_angle_90, pulse_speed_100):
        """
        If no arguments are given, this function returns the current calibration
        data, as a 5-tuple.
        """
        ...

class SPI:

    MASTER = "MASTER"
    SLAVE = "SLAVE"
    LSB = "LSB"
    MSB = "MSB"

    def __init__(self, bus):
        """
        Construct an SPI object on the given bus.
        """
        ...

    def deinit(self):
        """
        Turn off the SPI bus.
        """
        ...

    def init(self, mode, prescaler, baudrate=328125, polarity=1, phase=0, bits=8, firstbit=MSB, ti=False, crc=None):
        """
        Initialise the SPI bus with the given parameters:
        """
        ...

    def recv(self, recv, timeout=5000):
        """
        Receive data on the bus:
        """
        ...

    def send(self, send, timeout=5000):
        """
        Send data on the bus:
        """
        ...

    def send_recv(self, send, recv=None, timeout=5000):
        """
        Send and receive data on the bus at the same time:
        """
        ...

class Switch:

    def __init__(self):
        """
        Create and return a switch object.
        """
        ...

    def __call__(self):
        """
        Call switch object directly to get its state: True if pressed down, False otherwise.
        """
        ...

    def callback(self, fun):
        """
        Register the given function to be called when the switch is pressed down.
        """
        ...

class Timer:

    def __init__(self, *args, **kwargs):
        """
        Construct a new timer object of the given id.
        """
        ...

    def init(self, freq, prescaler, period):
        """
        Initialise the timer.
        """
        ...

    def deinit(self):
        """
        Deinitialises the timer.
        """
        ...

    def callback(self, fun):
        """
        Set the function to be called when the timer triggers.
        """
        ...

    def channel(self, channel, mode):
        """
        If only a channel number is ...ed, then a previously initialized channel
        object is returned (or ``None`` if there is no previous channel).
        """
        ...

    def counter(self, value):
        """
        Get or set the timer counter.
        """

    def freq(self, value):
        """
        Get or set the frequency for the timer (changes prescaler and period if set).
        """
        ...

    def period(self, value):
        """
        Get or set the period of the timer.
        """
        ...

    def prescaler(self, value):
        """
        Get or set the prescaler for the timer.
        """
        ...

    def source_freq(self):
        """
        Get the frequency of the source of the timer.
        """
        ...

class TimerChannel:

    def callback(self, fun):
        """
        Set the function to be called when the timer channel triggers.
        """
        ...

    def capture(self, value):
        """
        Get or set the capture value associated with a channel.
        """
        ...

    def compare(self, value):
        """
        Get or set the compare value associated with a channel.
        """
        ...

    def pulse_width(self, value):
        """
        Get or set the pulse width value associated with a channel.
        """

    def pulse_width_percent(self, value):
        """
        Get or set the pulse width percentage associated with a channel.
        """
        ...

class UART:

    RTS = "RTS"
    CTS = "CTS"

    def __init__(self, bus):
        """
        Construct a UART object on the given bus.
        """
        ...

    def init(self, baudrate, bits=8, parity=None, stop=1, timeout=1000, flow=None, timeout_char=0, read_buf_len=64):
        """
        Initialise the UART bus with the given parameters:
        """
        ...

    def deinit(self):
        """
        Turn off the UART bus.
        """
        ...

    def any(self):
        """
        Return ``True`` if any characters waiting, else ``False``.
        """
        ...

    def writechar(self, char):
        """
        Write a single character on the bus.
        """
        ...

    def read(self, nbytes):
        """
        Read characters.
        """
        ...

    def readchar(self):
        """
        Receive a single character on the bus.
        """
        ...

    def readinto(self, buf, nbytes):
        """
        Read bytes into the ``buf``.
        """
        ...

    def readline(self):
        """
        Read a line, ending in a newline character.
        """
        ...

    def write(self, buf):
        """
        Write the buffer of bytes to the bus.
        """
        ...

    def sendbreak(self):
        """
        Send a break condition on the bus.
        """
        ...

class USB_HID:
    """
    Create a new USB_HID object.
    """

    def recv(self, data, timeout=5000):
        """
        Receive data on the bus.
        """
        ...

    def send(self, data):
        """
        Send data over the USB HID interface:
        """
        ...

class USB_VCP:

    def __init__(self):
        """
        Create a new USB_VCP object.
        """
        ...

    def setinterrupt(self, chr):
        """
        Set the character which interrupts running Python code.
        """
        ...

    def isconnected(self):
        """
        Return ``True`` if USB is connected as a serial device, else ``False``.
        """
        ...

    def any(self):
        """
        Return ``True`` if any characters waiting, else ``False``.
        """
        ...

    def close(self):
        """
        This method does nothing. It exists so the USB_VCP object can act as a file.
        """
        ...

    def read(self, nbytes):
        """
        Read at most ``nbytes`` from the serial device and return them as a bytes object.
        """
        ...

    def readinto(self, buf, maxlen):
        """
        Read bytes from the serial device and store them into ``buf``, which
        should be a buffer-like object.
        """
        ...

    def readline(self):
        """
        Read a whole line from the serial device.
        """
        ...

    def readlines(self):
        """
        Read as much data as possible from the serial device, breaking it into lines.
        """
        ...

    def write(self, buf):
        """
        Write the bytes from ``buf`` to the serial device.
        """
        ...

    def recv(self, data, timeout=5000):
        """
        Receive data on the bus.
        """
        ...

    def send(self, data, timeout=5000):
        """
        Send data over the USB VCP.
        """
        ...
