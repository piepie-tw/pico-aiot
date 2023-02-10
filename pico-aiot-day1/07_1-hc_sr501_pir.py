from machine import Pin
import utime

sensor_pir = Pin(28, Pin.IN, Pin.PULL_DOWN)

def pir_handler(pin):
    if pin.value():
        print("ALARM! Motion detected @", utime.mktime(utime.localtime()))

sensor_pir.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

while True:
    utime.sleep(10)

