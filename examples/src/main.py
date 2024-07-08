from machine import Pin
import time

led = Pin(2, Pin.OUT)
MORSE_CODE_DICT = {
    "H": "....",
    "E": ".",
    "L": ".-..",
    "O": "---",
    "W": ".--",
    "R": ".-.",
    "D": "-..",
}


def morse_code(text):
    for letter in text:
        code = MORSE_CODE_DICT.get(letter.upper(), None)
        if code:
            for c in code:
                print(c)
                if c == ".":
                    led.on()
                    time.sleep(0.1)
                    led.off()
                    time.sleep(0.1)
                elif c == "-":
                    led.on()
                    time.sleep(0.3)
                    led.off()
                    time.sleep(0.1)
            time.sleep(0.2)


morse_code("Hello, World")
