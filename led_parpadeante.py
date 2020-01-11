from machine import Pin
from time import sleep

while True:
   led = Pin(16, Pin.OUT)
   led.value(0)
   sleep(5)
   led.value(1)
   sleep(5)

