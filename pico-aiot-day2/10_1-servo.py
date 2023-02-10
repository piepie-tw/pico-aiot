from machine import Pin, PWM
import utime

servo = PWM(Pin(0))
servo.freq(50)
servo.duty_u16(1000)
utime.sleep(5)

while True:
    for dc in range(1000, 9000, 50):
        servo.duty_u16(dc)
        utime.sleep(0.01)
    utime.sleep(1)
    
    for dc in range(9000, 1000, -50):
        servo.duty_u16(dc)
        utime.sleep(0.01)
    utime.sleep(1)

