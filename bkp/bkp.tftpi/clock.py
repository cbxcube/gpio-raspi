#!/usr/bin/env python

import os
import sys
import math
import pygame
import pygame.mixer
from pygame.locals import *

black = 0,0,0
white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255

pygame.display.set_mode((320,240))

screen = screen_width, screen_height = 320, 240

clock = pygame.time.Clock()

pygame.display.set_caption("Physics")

fps_cap = 120
running = True
while running:
    clock.tick(fps_cap)

    for event in pygame.event.get(): #error is here
        if event.type == pygame.QUIT:
            running = False

    screen.fill(red)

    pygame.display.flip()

pygame.quit()
sys.exit    
