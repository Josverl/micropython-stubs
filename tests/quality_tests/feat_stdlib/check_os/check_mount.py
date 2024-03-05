# SD card
import os

# Slot 2 uses pins sck=18, cs=5, miso=19, mosi=23
# sd = machine.SDCard(slot=2)
# Mount SD to /sd
sdcard = object()

os.mount(sdcard, "/sd") 
print("SD Card mounted")

sd = 1
os.mount(sd, "/sd")  

os.listdir("/sd")  # list directory contents

os.umount("/sd") 


