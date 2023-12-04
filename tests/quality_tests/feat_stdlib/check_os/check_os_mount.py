# board : ESP32
# ref : https://docs.micropython.org/en/latest/esp32/quickref.html

import os

sd = bytearray(10 * 1024)

os.mount(sd, "/sd")  # mount
os.listdir("/sd")  # list directory contents
os.umount("/sd")  # eject
