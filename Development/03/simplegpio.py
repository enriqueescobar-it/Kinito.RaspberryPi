import RPi.GPIO as GPIO
import time
channel = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel,GPIO.OUT)
for n in range(100):
    GPIO.output(channel,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(channel,GPIO.LOW)
    time.sleep(5)
