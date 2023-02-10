from machine import Pin
from machine import Timer
import utime

button = Pin(14, Pin.IN, Pin.PULL_UP)
timer = Timer()

def debounce(pin):
    timer.init(mode=Timer.ONE_SHOT, period=200, callback=button_handler)
    
def button_handler(pin):
    print("Button pressed @", utime.mktime(utime.localtime()))

button.irq(trigger=Pin.IRQ_FALLING, handler=debounce)

while True:
    utime.sleep(10)

