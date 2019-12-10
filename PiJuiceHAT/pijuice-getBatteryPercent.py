#!/usr/bin/python3
from pijuice import PiJuice
pijuice = PiJuice(1, 0x14)

def get_battery_percent():
    return pijuice.status.GetChargeLevel()['data']

def get_battery_percent_str():
    return print(get_battery_percent(),'%')

print(get_battery_percent())
