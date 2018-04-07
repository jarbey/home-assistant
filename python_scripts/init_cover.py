#!/usr/bin/python
from time import sleep
import sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in sys.argv[1].split(","):
	GPIO.setup(int(pin), GPIO.OUT)
	GPIO.output(int(pin), 1)
