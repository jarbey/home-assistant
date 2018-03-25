#!/usr/bin/python
from time import sleep
import sys
import RPi.GPIO as GPIO

pin=int(sys.argv[1])

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, 1)
sleep(0.25)
GPIO.output(pin, 0);
