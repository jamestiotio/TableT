import RPi.GPIO as GPIO
from time import sleep
import sys

FPS = 1 / 30

GPIO.setmode(GPIO.BCM)
CONTROLS = { 26:'Y', 19:'A', 13:'X', 6:'B', 21:'U', 20:'D', 16:'L', 12:'R' }
for pin in CONTROLS: GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

import pygame
pygame.init()
screen = pygame.display.set_mode((800, 480))
running = True

WHITE	= (255,255,255)
RED 	= (255,0,0)
GREEN	= (0,255,0)
BLUE	= (0,0,255)
YELLOW	= (255,255,0)
BGRAY	= (50,50,50)
BLACK	= (0,0,0)

rectsz = 80
posrect = lambda x, y: pygame.Rect(x*rectsz, y*rectsz, rectsz, rectsz)

while running:
	pygame.draw.rect(screen, (GREEN if GPIO.input(21) == 0 else BLACK), posrect(2,1))
	pygame.draw.rect(screen, (YELLOW if GPIO.input(20) == 0 else BLACK), posrect(2,3))
	pygame.draw.rect(screen, (RED if GPIO.input(16) == 0 else BLACK), posrect(1,2))
	pygame.draw.rect(screen, (BLUE if GPIO.input(12) == 0 else BLACK), posrect(3,2))
	pygame.draw.rect(screen, (WHITE if GPIO.input(26) == 0 else BLACK), posrect(6,1))
	pygame.draw.rect(screen, (BGRAY if GPIO.input(19) == 0 else BLACK), posrect(6,3))
	pygame.draw.rect(screen, (WHITE if GPIO.input(13) == 0 else BLACK), posrect(5,2))
	pygame.draw.rect(screen, (BGRAY if GPIO.input(6) == 0 else BLACK), posrect(7,2))

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit(0)

	state = ""
	for pin in CONTROLS: state += "%s (%d): %d   " % (CONTROLS[pin], pin, GPIO.input(pin))
	print(state)
	pygame.display.flip()
	sleep(FPS)
