from machine import Pin, I2C

sda = Pin(0)
scl = Pin(1)
i2c = I2C(0, sda=sda, scl=scl, freq=200000)

print(i2c.scan())
