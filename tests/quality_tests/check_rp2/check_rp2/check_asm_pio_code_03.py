# TODO: rp2.PIO - The functions defined in the asm_pio decorator are not recognized by pyright.
# ignore for now : other issues to solve first
"""
Sample from micropython discussions

# Generating Sinewaves with PIO block
# ref : https://github.com/orgs/micropython/discussions/16368
"""

# -----------------------------------------------
# add type hints for the rp2.PIO Instructions
try:
    from typing_extensions import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False
if TYPE_CHECKING:
    from rp2.asm_pio import *
# -----------------------------------------------

import _thread
from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from collections import deque

_UART_BAUD = const(115_200)
_TX_PIN = const(2)
_RX_PIN = const(0)

print(f"Baudrate: {_UART_BAUD}; Tx pin: {_TX_PIN}; Rx pin: {_RX_PIN}")

@asm_pio(sideset_init=PIO.OUT_HIGH, out_init=PIO.OUT_HIGH, out_shiftdir=PIO.SHIFT_RIGHT, fifo_join=PIO.JOIN_TX, )
def uart_tx():
    # fmt: off
    # Block with TX deasserted until data available
    pull()
    # Initialise bit counter, assert start bit for 8 cycles
    set(x, 7)  .side(0)       [7]
    # Shift out 8 data bits, 8 execution cycles per bit
    label("bitloop")
    out(pins, 1)              [6]
    jmp(x_dec, "bitloop")
    # Assert stop bit for 8 cycles total (incl 1 for pull())
    nop()      .side(1)       [6]
    # fmt: on

@asm_pio(in_shiftdir=PIO.SHIFT_RIGHT, fifo_join=PIO.JOIN_RX, )
def uart_rx():
    # fmt: off
    label("start")
    # Stall until start bit is asserted
    wait(0, pin, 0)
    # Preload bit counter, then delay until halfway through
    # the first data bit (12 cycles incl wait, set).
    set(x, 7)                 [10]
    label("bitloop")
    # Shift data bit into ISR
    in_(pins, 1)
    # Loop 8 times, each loop iteration is 8 cycles
    jmp(x_dec, "bitloop")     [6]
    # Check stop bit (should be high)
    jmp(pin, "good_stop")
    # Either a framing error or a break.
    # Wait for line to return to idle state.
    wait(1, pin, 0)
    # Don't push data if we didn't see good framing.
    jmp("start")
    # No delay before returning to start; a little slack is
    # important in case the TX clock is slightly too fast.
    label("good_stop")
    push(block)
    # fmt: on


# Set up the state machine we're going to use to receive the characters.
sm_rx = StateMachine(
    0,
    uart_rx,
    freq=8 * _UART_BAUD,
    in_base=Pin(_RX_PIN, Pin.IN, Pin.PULL_UP),  # For WAIT, IN
    jmp_pin=Pin(_RX_PIN, Pin.IN, Pin.PULL_UP),  # For JMP
)

sm_tx = StateMachine(
    1,
    uart_tx,
    freq=8 * _UART_BAUD,
    sideset_base=Pin(_TX_PIN),
    out_base=Pin(_TX_PIN),
)
sm_tx.active(1)


fifo_tx = deque((), 64)
fifo_rx = deque((), 64)

def core1_task(sm_tx, sm_rx, fifo_tx, fifo_rx): # Push and pull between PIO's and in-memory FIFOs to allow larger buffers
    while True:
        if sm_rx.rx_fifo() > 0: # Prevent trying to pull from empty FIFO to avoid blocking
            # Get a 32-bit word from PIO's FIFO, convert it to a character and then append it to the in-memory FIFO
            fifo_rx.append(chr(sm_rx.get(None, 24))) # Shift right by 24 bits before returning
        
        if len(fifo_tx) > 0: # Prevent trying to pull from empty in-memory FIFO to avoid exception
            if sm_tx.tx_fifo() < 8: # Prevent trying to push into full FIFO to avoid blocking
                # Pop a character out of in-memory FIFO, convert it to binary and push it into PIO's FIFO
                sm_tx.put(ord(fifo_tx.popleft()))

sm_rx.active(1)
_thread.start_new_thread(core1_task, (sm_tx, sm_rx, fifo_tx, fifo_rx))

def receive(len = -1): # Pull "len" amount of characters out of the FIFO, return them as one string
    global fifo_rx
    out = ""
    
    if len == -1:
        while True:
            try: out += fifo_rx.popleft()
            except IndexError: return out # Exit upon emptying FIFO
    
    for _ in range(len):
        try: out += fifo_rx.popleft()
        except IndexError: break # Exit prematurely when FIFO is empty; blocking could be potentially used
    return out

def receive_until(until):
    global fifo_rx
    out = ""
    char = ""
    while char != until:
        try: char = fifo_rx.popleft()
        except IndexError: continue
        out += char
    return out

def transmit(string):
    global fifo_tx
    for character in string:
        fifo_tx.append(character)
        
print("DONE")