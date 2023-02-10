import utime
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

sda = Pin(0)
scl = Pin(1)
i2c = I2C(0, sda=sda, scl=scl, freq=200000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    

lcd.custom_char(0, bytearray([0x0E,
  0x11,
  0x11,
  0x02,
  0x04,
  0x04,
  0x00,
  0x04]))
lcd.move_to(0, 0)
lcd.putstr(chr(0))
utime.sleep(10)
lcd.clear()
