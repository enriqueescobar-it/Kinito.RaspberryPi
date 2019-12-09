#!/usr/bin/python3
from pijuice import PiJuice
pijuice = PiJuice(1, 0x14)

def get_battery_temp():
    return pijuice.status.GetBatteryTemperature()['data']

def get_battery_temp_C():
    return print(get_battery_temp(),'C')

print(get_battery_temp())
