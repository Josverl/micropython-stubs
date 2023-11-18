# I2S

from machine import I2S, Pin
buf = bytearray(10)  # create a buffer with 10 bytes

i2s = I2S(0, sck=Pin(16), ws=Pin(17), sd=Pin(18), mode=I2S.TX, bits=16, format=I2S.STEREO, rate=44100, ibuf=40000)  # create I2S object
i2s.write(buf)  # write buffer of audio samples to I2S device

i2s = I2S(1, sck=Pin(0), ws=Pin(1), sd=Pin(2), mode=I2S.RX, bits=16, format=I2S.MONO, rate=22050, ibuf=40000)  # create I2S object
i2s.readinto(buf)  # fill buffer with audio samples from I2S device

