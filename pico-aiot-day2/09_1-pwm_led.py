from machine import Pin, PWM
import utime

led = PWM(Pin(15))
led.freq(100)
led.duty_u16(0)

while True:
    for dc in range(0, 65536, 4096): 
        led.duty_u16(dc)
        utime.sleep(0.1)
    utime.sleep(2)
    for dc in range(65535, -2, -4096):
        led.duty_u16(dc)
        utime.sleep(0.1)
    utime.sleep(2)

