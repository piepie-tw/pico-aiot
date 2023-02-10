from machine import Pin
import utime

led = Pin(15, Pin.OUT)

print("LED is on")
led.value(1)
utime.sleep(5)

print("LED is off")
led.value(0)
