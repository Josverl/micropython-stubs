# PWM

from machine import Pin, PWM

pwm0 = PWM(Pin(0))  # create PWM object from a pin
pwm0.freq()  # get current frequency
pwm0.freq(1000)  # set frequency
pwm0.duty_u16()  # get current duty cycle, range 0-65535
pwm0.duty_u16(200)  # set duty cycle, range 0-65535
pwm0.deinit()  # turn off PWM on the pin


