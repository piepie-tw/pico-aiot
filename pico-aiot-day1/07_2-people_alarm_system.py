from machine import Pin
import utime

sensor_pir = Pin(28, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)

def pir_handler(pin):
    if pin.value():
        print("ALARM! Motion detected @", utime.mktime(utime.localtime()))

        for i in range(10):
            led.toggle()
            utime.sleep_ms(200)

sensor_pir.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

while True:
    utime.sleep(10)


