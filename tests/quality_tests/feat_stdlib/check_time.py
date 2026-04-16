import time

# ref : https://github.com/Josverl/micropython-stubs/issues/771

local_time = (2024, 12, 29, 17, 33, 32, 6, 364)
seconds = time.mktime(local_time)  # stubs-ignore:  version < 1.24.0


# -------------------

from time import ticks_ms, ticks_diff, ticks_add
from sys import print_exception

def anything():
    timeout_at = ticks_add(ticks_ms(), 500)
    while ticks_diff((now:=ticks_ms()), timeout_at) < 0:
        # do stuff
        pass
    try:
        print('timeout', now)
    except Exception as e:              # thus throwing an…
        print_exception(e)              # …AttributeError


# -----------------------

from time import ticks_ms
start=ticks_ms()
while ticks_ms()-start<100: # type: ignore # will fail if the type: ignore is not required
    pass
    # if uart.any():  return uart.read().decode()
print('timeout', ticks_ms()-start) # type: ignore # will fail if the type: ignore is not required
# return uart.read().decode()

# -----------------------
cycle=1
gotcha=now0=was0=d0=0
was=ticks_ms()
while 1:
    now=ticks_ms()
    d=now-was       #  type: ignore #  will fail if the type: ignore is not required
    cycle+=1
    if d>100:
      if gotcha==0:  
        print( 'TIMEOUT  prev', now0, was0, d0, now, was, d, end=' ')
        gotcha=cycle
    if gotcha==cycle-1: 
        print('  post', now, was, d)
        break
    now0=now
    was0=was
    d0=d
