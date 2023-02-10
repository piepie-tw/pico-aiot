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

lcd.move_to(0, 0)
lcd.putstr("It Works!")
utime.sleep(5)
lcd.clear()

lcd.move_to(5, 0)
lcd.putstr("Hello")
lcd.move_to(4, 1)
lcd.putstr("World!!")
utime.sleep(5)
lcd.clear()
