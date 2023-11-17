# ref: https://learn.adafruit.com/Memory-saving-tips-for-CircuitPython/ram-saving-tips

import gc

# add other imports

gc.collect()
start_mem = gc.mem_free()
print("Point 1 Available memory: {} bytes".format(start_mem))

# add code here to be measured for memory use

gc.collect()
end_mem = gc.mem_free()

print("Point 2 Available memory: {} bytes".format(end_mem))
print("Code section 1-2 used {} bytes".format(start_mem - end_mem))

# https://docs.micropython.org/en/latest/reference/constrained.html#the-heap
gc.collect()
gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())  # stubs-ignore: port=='samd'
# TODO : micropython.gc - samd has no gc.threshold() method


# https://docs.micropython.org/en/latest/reference/constrained.html#reporting

# import gc
import micropython

gc.collect()
micropython.mem_info()
print("-----------------------------")
print("Initial free: {} allocated: {}".format(gc.mem_free(), gc.mem_alloc()))


def func():
    a = bytearray(10000)


gc.collect()
print("Func definition: {} allocated: {}".format(gc.mem_free(), gc.mem_alloc()))
func()
print("Func run free: {} allocated: {}".format(gc.mem_free(), gc.mem_alloc()))
gc.collect()
print("Garbage collect free: {} allocated: {}".format(gc.mem_free(), gc.mem_alloc()))
print("-----------------------------")
micropython.mem_info(1)
