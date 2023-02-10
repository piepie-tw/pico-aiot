from machine import Pin
import utime

button = Pin(14, Pin.IN)
previousStatus = None

while True:
    input = button.value()

    if input == 0 and previousStatus == 1:
        print("Button pressed @", utime.time())

    previousStatus = input
