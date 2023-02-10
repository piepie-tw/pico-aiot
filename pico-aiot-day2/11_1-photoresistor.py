from machine import ADC, Pin
import utime

photoresistor = ADC(Pin(26))

def readADC(pin):
    vout = photoresistor.read_u16()
    vout = round((vout/65535)*3.3, 2)
    
    if vout != 0:
        r1 = 330*(3.3-vout)/vout
        r1 = round(r1, 0)
        
        return (vout, r1)


while True:
    vout = readADC(photoresistor)[0]
    r1   = readADC(photoresistor)[1]
    
    print("---------------------")
    print("Vout: " + str(vout) +" V")
    print("R1: " + str(r1) +" ohm")
    
    utime.sleep(1) 
