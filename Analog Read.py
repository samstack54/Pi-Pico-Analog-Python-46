 
from utime import sleep

adc = machine.ADC(28)  # ADC2

while True:
    val = adc.read_u16()
    sleep(0.1)
    print(" value:", val)

