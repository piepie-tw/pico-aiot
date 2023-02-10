from machine import Pin
import utime

buzzer = Pin(15, Pin.OUT)

while True:
    buzzer.value(1)
    utime.sleep(1)

    buzzer.value(0)
    utime.sleep(1)

