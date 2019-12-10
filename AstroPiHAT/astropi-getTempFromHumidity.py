#!/usr/bin/python3
from sense_hat import SenseHat
senseHat = SenseHat()
senseHat.clear()

def get_humid_temp():
    return senseHat.get_temperature_from_humidity()

print(round(get_humid_temp(),2))
