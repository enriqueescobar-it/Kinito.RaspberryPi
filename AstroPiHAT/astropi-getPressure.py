#!/usr/bin/python3
from sense_hat import SenseHat
senseHat = SenseHat()
senseHat.clear()

def get_pressure():
    return senseHat.get_pressure()

print(round(get_pressure(),2))
