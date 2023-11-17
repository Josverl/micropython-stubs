# -------------------------------------------------------------
#  Identifying the slowest section of code
# -------------------------------------------------------------
# This is a process known as profiling and is covered in textbooks and (for standard Python) supported by various software tools.
# For the type of smaller embedded application likely to be running on MicroPython platforms the slowest function or method can usually
# be established by judicious use of the timing ticks group of functions documented in utime. Code execution time can be measured in ms, us, or CPU cycles.
#
# The following enables any function or method to be timed by adding an @timed_function decorator:
import utime


def timed_function(f, *args, **kwargs):
    "enables any function or method to be timed by adding an @timed_function decorator"
    myname = str(f).split(" ")[1]

    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        print("Function {} Time = {:6.3f}ms".format(myname, delta / 1000))
        return result

    return new_func


# Example usage:
@timed_function
def test_func():
    for i in range(100):
        a = i * i
