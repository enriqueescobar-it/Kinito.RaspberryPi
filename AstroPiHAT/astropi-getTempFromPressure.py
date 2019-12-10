#!/usr/bin/python3
from sense_hat import SenseHat
senseHat = SenseHat()
senseHat.clear()

def get_pressure_temp():
    return senseHat.get_temperature_from_pressure()

print(round(get_pressure_temp(),2))
