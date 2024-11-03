# TODO: rp2.PIO - The functions defined in the asm_pio decorator are not recognized by pyright.
# ignore for now : other issues to solve first
from typing import Callable, no_type_check


def asm_pio(set_init: int) -> Callable[[Callable], Callable]: ...


# the no_type_check decorator is used to disable type checking for the decorated function
# the function is written in assembly language and the type checker will not be able to check it
# unless the type checker is able to understand the assembly language


def my_deco(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper


@no_type_check
@my_deco
def foo(x= ""):
    print(f"foo {x}")
    return 1




# """
# Sample from micropython documentation

# # programmable IO
# # ref : https://docs.micropython.org/en/latest/rp2/quickref.html#programmable-io-pio
# """
# @no_type_check
# @asm_pio(set_init=0)
# def blink_1hz():
#     # Cycles: 1 + 7 + 32 * (30 + 1) = 1000
#     set(pins, 1)
#     set(x, 31)[6]
#     label("delay_high")
#     nop()[29]
#     jmp(x_dec, "delay_high")

#     # Cycles: 1 + 7 + 32 * (30 + 1) = 1000
#     set(pins, 0)
#     set(x, 31)[6]
#     label("delay_low")
#     nop()[29]
#     jmp(x_dec, "delay_low")


foo()
print("Done.")