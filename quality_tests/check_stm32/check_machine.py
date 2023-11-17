buf = b"00000000"

# I2C bus

from machine import I2C

i2c = I2C("X", freq=400000)  # create hardware I2c object


i2c = I2C(scl="X1", sda="X2", freq=100000)  # create software I2C object

i2c.scan()  # returns list of peripheral addresses
i2c.writeto(0x42, "hello")  # write 5 bytes to peripheral with address 0x42
i2c.readfrom(0x42, 5)  # read 5 bytes from peripheral

i2c.readfrom_mem(0x42, 0x10, 2)  # read 2 bytes from peripheral 0x42, peripheral memory 0x10
i2c.writeto_mem(0x42, 0x10, "xy")  # write 2 bytes to peripheral 0x42, peripheral memory 0x10
# Note: for legacy I2C support see pyb.I2C.

# I2S bus
# See machine.I2S.

from machine import I2S, Pin

i2s = I2S(
    2, sck=Pin("Y6"), ws=Pin("Y5"), sd=Pin("Y8"), mode=I2S.TX, bits=16, format=I2S.STEREO, rate=44100, ibuf=40000
)  # create I2S object
i2s.write(buf)  # write buffer of audio samples to I2S device

i2s = I2S(1, sck=Pin("X5"), ws=Pin("X6"), sd=Pin("Y4"), mode=I2S.RX, bits=16, format=I2S.MONO, rate=22050, ibuf=40000)  # create I2S object
i2s.readinto(buf)  # fill buffer with audio samples from I2S device
