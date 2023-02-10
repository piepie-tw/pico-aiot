from machine import ADC
import utime

sensor_temp = machine.ADC(ADC.CORE_TEMP)
normalization = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * normalization
    temperature = 27 - (reading - 0.706)/0.001721

    print(temperature)
    utime.sleep(1)
