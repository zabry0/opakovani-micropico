from machine import Pin
from time import sleep
import dht

button =Pin(0,Pin.IN,Pin.PULL_UP)

sensor = dht.DHT11(Pin(1))

metr = 1

while True:
    if button.value() == 1:
        if metr == 1:
            metr = 2
        else:
            metr = 1
   
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()

    if metr == 1:
        print("temp=" + str(t))
    
    if metr == 2:
        print("humidity=" + str(h))
    
    sleep(5)
    
    for i in range(10):
        print(" ")
