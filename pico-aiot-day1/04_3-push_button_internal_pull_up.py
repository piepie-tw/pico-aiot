from machine import Pin
import utime

button = Pin(14, Pin.IN, Pin.PULL_UP)

WAIT_TIME = 0.2
previousStatus = None
currentTime    = None
previousTime   = utime.mktime(utime.localtime())

while True:
    input = button.value()

    currentTime = utime.mktime(utime.localtime())

    if input == 0 and previousStatus == 1 and (currentTime - previousTime) > WAIT_TIME:
        previousTime = currentTime
        print("Button pressed @", utime.mktime(utime.localtime()))

    previousStatus = input
