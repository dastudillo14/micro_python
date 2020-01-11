from machine import Pin
import dht
import time

d = dht.DHT11(machine.Pin(14))  #pin referente a esquema de controlador. Pin de entrada de datos

while True:    
    d.measure()
    print("Temperatura: "+str(d.temperature()))
    print("Humedad: "+str(d.humidity()))
    time.sleep(5)
