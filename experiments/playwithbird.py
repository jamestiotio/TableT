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

WHITE	= (255,255,255)
RED 	= (255,0,0)
GREEN	= (0,255,0)
BLUE	= (0,0,255)
YELLOW	= (255,255,0)
BGRAY	= (50,50,50)
BLACK	= (0,0,0)


def game_start():
    HEALTH = 10
    GAME_RUNNING = True
    bird = [240,60,0,0,45] # y,x,vy,vx,r
    blns = [[240,-30,0,-3,45,BLUE],[120,-30,0.6,-1.5,30,GREEN]] # y,x,vy,vx,r,color
    GRAV = -3
    lastbtn = False
    while GAME_RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit(0)
        if HEALTH < 1: break
        if GPIO.input(19) and not lastbtn: bird[2] += 45
        lastbtn = GPIO.input(19)
        bird[2] += GRAV
        bird[2] *= 0.9
		bird[0] += bird[2]
		bird[0] = min(max(bird[4], bird[0]), 480-bird[4])
        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, (bird[1], int(bird[0])), bird[4], 0)
        pygame.draw.circle(screen, WHITE, (bird[1]+6, int(bird[0])+18), 9, 0)
        pygame.draw.circle(screen, WHITE, (bird[1]+30, int(bird[0])+18), 9, 0)
        pygame.draw.circle(screen, BLACK, (bird[1]+6, int(bird[0])+18), 3, 0)
        pygame.draw.circle(screen, BLACK, (bird[1]+30, int(bird[0])+18), 3, 0)
        pygame.draw.polygon(screen, YELLOW, [(bird[1]+39, int(bird[0])-15), (bird[1]+9, int(bird[0])-30), (bird[1]+9, int(bird[0]))])
        screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
        pygame.display.flip()
        sleep(FPS)
        

game_start()