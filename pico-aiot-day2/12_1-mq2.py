from machine import ADC, Pin
import utime

mq2 = ADC(Pin(26))
conversion_factor = 3.3 / (65535)

while True:
    value = mq2.read_u16() * conversion_factor
    print("MQ-2:", value)
    utime.sleep(1)


