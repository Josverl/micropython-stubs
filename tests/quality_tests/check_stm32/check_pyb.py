# https://docs.micropython.org/en/latest/pyboard/quickref.html

import time
import pyb
from pyb import LED
from pyb import Switch
from pyb import Pin
from pyb import Servo
from pyb import ExtInt
from pyb import RTC
from pyb import Timer
from pyb import ADC
from pyb import DAC
from pyb import UART
from pyb import SPI
from pyb import CAN
from pyb import Accel

# samples need a buffer to store the data
buf = b"00000000"


pyb.repl_uart(pyb.UART(3, 9600))  # duplicate REPL on UART(1)
pyb.wfi()  # pause CPU, waiting for interrupt
pyb.freq()  # get CPU and bus frequencies
pyb.freq(60000000)  # set CPU freq to 60MHz

if False:
    pyb.stop()  # stop CPU, waiting for external interrupt


# Internal LEDs
# See pyb.LED.

led = LED(1)  # 1=red, 2=green, 3=yellow, 4=blue
led.toggle()
led.on()
led.off()

# LEDs 3 and 4 support PWM intensity (0-255)
LED(4).intensity()  # get intensity
LED(4).intensity(128)  # set intensity to half

# Internal switch
# See pyb.Switch.


sw = Switch()
sw.value()  # returns True or False
sw.callback(lambda: pyb.LED(1).toggle())

# Pins and GPIO
# See pyb.Pin.


p_out = Pin("X1", Pin.OUT_PP)
p_out.high()
p_out.low()

p_in = Pin("X2", Pin.IN, Pin.PULL_UP)
p_in.value()  # get value, 0 or 1


# Servo control
# See pyb.Servo.


s1 = Servo(1)  # servo on position 1 (X1, VIN, GND)
s1.angle(45)  # move to 45 degrees
s1.angle(-60, 1500)  # move to -60 degrees in 1500ms
s1.speed(50)  # for continuous rotation servos


# External interrupts¶
# See pyb.ExtInt.


callback = lambda e: print("intr")
ext = ExtInt(Pin("Y1"), ExtInt.IRQ_RISING, Pin.PULL_NONE, callback)


# RTC (real time clock)
# See pyb.RTC


rtc = RTC()
rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0))  # set a specific date and time
rtc.datetime()  # get date and time


# PWM (pulse width modulation)¶
# See pyb.Pin and pyb.Timer.


p = Pin("X1")  # X1 has TIM2, CH1
tim = Timer(2, 1000)
ch = tim.channel(1, Timer.PWM, pin=p)
ch.pulse_width_percent(50)

# ADC (analog to digital conversion)¶
# See pyb.Pin and pyb.ADC.


adc = ADC(Pin("X19"))
adc.read()  # read value, 0-4095

# DAC (digital to analog conversion)¶
# See pyb.Pin and pyb.DAC.


dac = DAC(Pin("X5"))
dac.write(120)  # output between 0 and 255

# UART (serial bus)
# See pyb.UART.


uart = UART(3, 9600)
uart.write("hello")
uart.read(5)  # read up to 5 bytes

# SPI bus


spi = SPI(1, SPI.CONTROLLER, baudrate=200000, polarity=1, phase=0)
spi.send("hello")
spi.recv(5)  # receive 5 bytes on the bus
spi.send_recv("hello")  # send and receive 5 bytes


# CAN bus (controller area network)¶
# See pyb.CAN.


can = CAN(1, CAN.LOOPBACK)
can.setfilter(0, CAN.LIST16, 0, (123, 124, 125, 126)) # stubs-ignore : version<=1.18.0
can.send("message!", 123)  # send a message with id 123
can.recv(0)  # receive message on FIFO 0

# Internal accelerometer¶
# See pyb.Accel.


accel = Accel()
print(accel.x(), accel.y(), accel.z(), accel.tilt())
