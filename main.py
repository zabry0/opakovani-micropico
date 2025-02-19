import machine
import dht
import time

meric = machine.Pin(1)

button = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_UP)

sensor = dht.DHT11(meric)

while True:
    if button.value() == 0:
        if mereni == 1:
            mereni = 2
        else:
            mereni = 1
    
    sensor.measure() 
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    
    if mereni == 1:
        print('Temperature: %3.1f C' %temp)
        print('Temperature: %3.1f F' %temp_f)
               


    if mereni == 2:
        print('Humidity: %3.1f %%' %hum)
        time.sleep(0.5)