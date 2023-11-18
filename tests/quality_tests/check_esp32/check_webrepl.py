# https://docs.micropython.org/en/latest/esp32/quickref.html#webrepl-web-browser-interactive-prompt
#
import webrepl_setup

# and following on-screen instructions. After reboot, it will be available for connection. If you disabled automatic start-up on boot, you may run configured daemon on demand using:

import webrepl

webrepl.start()

# or, start with a specific password
webrepl.start(password="mypass")
