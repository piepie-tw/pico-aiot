from machine import Pin
import utime
import _thread

red   = Pin(16, Pin.OUT)
green = Pin(15, Pin.OUT)

def core0_thread(t):
    for i in range(t):
        red.toggle()
        utime.sleep(0.5)
    
def core1_thread(t):
    for i in range(t):
        green.toggle()
        utime.sleep(1)

_thread.start_new_thread(core1_thread, (20,))
core0_thread(10)
