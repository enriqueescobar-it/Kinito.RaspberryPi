#!/usr/bin/python3
from sense_hat import SenseHat
senseHat = SenseHat()
senseHat.clear()

def get_humidity():
    return senseHat.get_humidity()

print(round(get_humidity(),2))
