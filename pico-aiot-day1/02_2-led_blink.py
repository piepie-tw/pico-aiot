from machine import Pin
import utime

led = Pin(15, Pin.OUT)

while True:
    print("LED is on")
    led.value(1)
    utime.sleep(1)

    print("LED is off")
    led.value(0)
    utime.sleep(1)

