    #-------------------------------------------------------------------------------
# Name:        game.py
# Purpose:     Demonstrate dynamic loading of game background
#
# Author:      Arvin
#
# Created:     22/01/2012
# Copyright:   (c) Arvin 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
from pygame import *
import map1
import random

DEFAULT_SCREENSIZE = [434, 434] #16 X 14 grid with 32px X 32px cell

pygame.init()

screen = pygame.display.set_mode(DEFAULT_SCREENSIZE)
display.set_caption('Background Rendering Demo')
tile0=pygame.image.load("tile0.png") # one 
tile1=pygame.image.load("tile1.png") # angle
tile2=pygame.image.load("tile2.png") # three way
MAP=[]
for i in range(7):
    row=[]
    for a in range(7):
        tile = random.choice(['l','a','t'])
        rand=random.choice([0,90,180,270])
        if (i == 0 and a == 0):
            tile = 'a'
            rand=270
        if (i == 0 and a == 6):
            tile = 'a'
            rand=180
        if (i == 6 and a == 0):
            tile = 'a'
            rand = 0
        if (i==6 and a == 6):
            tile = 'a'
            rand=90
        
        
        row.append(map1.Map(tile, rand))
    MAP.append(row)
    print(MAP)
for y in range(len(MAP)):
    for x in range(len(MAP[y])):
        images, location = MAP[y][x].get_object(y,x)
        screen.blit(images, location)
        # location = 
#loops through map to set background
# for y in range(len(map1.MAP)):
#     for x in range(len(map1.MAP[y])):
#         location = (x*62, y*62)
#         rand=random.choice([0,90,180,270])
#         print(y,x)        
            
#         if map1.MAP[y][x] == "l":
#             rotated = pygame.transform.rotate(tile0, rand)
#         if map1.MAP[y][x] == "a":
#             rotated = pygame.transform.rotate(tile1, rand)
#         if map1.MAP[y][x] == "t":
#             rotated = pygame.transform.rotate(tile2, rand)
#         if (y == 0 and x == 0):
#             rotated = pygame.transform.rotate(tile1, 270)
#         if (y == 0 and x == 6):
#             rotated = pygame.transform.rotate(tile1, 180)
#         if (y == 6 and x == 0):
#             rotated = pygame.transform.rotate(tile1, 0)
#         if (y == 6 and x == 6):
#             rotated = pygame.transform.rotate(tile1, 90)
#         screen.blit(rotated, location)

            
updated = False
going = True

while going:
    if updated == False:
        pygame.display.update()
        updated = True

    for e in event.get():
        if e.type == QUIT: #checks if close button was clicked
            going = False

pygame.quit()
