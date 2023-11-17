# ADC
from machine import ADC, Pin

adc = ADC(Pin(26))  # create ADC object on ADC pin
adc.read_u16()  # read value, 0-65535 across voltage range 0.0v - 3.3v
