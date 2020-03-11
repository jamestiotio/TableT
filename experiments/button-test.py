import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

CONTROLS = { 26:'Y', 19:'A', 13:'X', 6:'B', 21:'U', 20:'D', 16:'L', 12:'R' }

for pin in CONTROLS:
	GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

while True:
	state = ""
	for pin in CONTROLS:
		state += "%s (%d): %d   " % (CONTROLS[pin], pin, GPIO.input(pin))
	print(state)
	sleep(0.1)
