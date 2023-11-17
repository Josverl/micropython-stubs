import array

NUM_LEDS = 10

ar = array.array("I", [0 for _ in range(NUM_LEDS)])

x = ar[3] 
ar[3] = 0x12345678 
