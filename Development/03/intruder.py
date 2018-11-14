import RPi.GPIO as GPIO
import sys
import wave
import pyaudio
import time

channel = 7
CHUNK= 1024
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel,GPIO.IN)
p = pyaudio.PyAudio()
while True:
    if GPIO.input(channel)==GPIO.HIGH:
        print('INTRUDER ALERT!!!!!')
        wf = wave.open('intruder.wav','rb')
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels = wf.getnchannels(),rate=wf.getframerate(),output=True)
        data = wf.readframes(CHUNK)
        while data !='':
            stream.write(data)
            data = wf.readframes(CHUNK)
        stream.stop_stream()
        stream.close()
    else:
        print('no intruder alert')
    time.sleep(1)
p.terminate()
GPIO.cleanup()
