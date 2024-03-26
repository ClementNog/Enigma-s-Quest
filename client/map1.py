#-------------------------------------------------------------------------------
# Name:        map.py
# Purpose:     Serve as a sample map for a game background
#
# Author:      Arvin
#
# Created:     22/01/2012
# Copyright:   (c) Arvin 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame
import random
# fills a 16 X 14 map with rectangles representing tiles to be rendered from the
# source images to the game display

#assigns source image
class Map():
   line=pygame.image.load("tile0.png") 
   angle=pygame.image.load("tile1.png") 
   three=pygame.image.load("tile2.png") # three way

   def __init__(self, tipe, rotation):
      self.tipe = tipe
      self.rotation = rotation
      self.location = (0,0)
      self.image=""
   
   def get_object(self,y,x):
      self.location = (x*100, y*100)
      if self.tipe == "l":
         self.image = pygame.transform.rotate(self.line, self.rotation)
      if self.tipe == "a":
         self.image = pygame.transform.rotate(self.angle, self.rotation)
      if self.tipe == "t":
         self.image = pygame.transform.rotate(self.three, self.rotation)
      return self
   
   def get_wall(self):
      # wall_horizontal_line= pygame.Rect(self.location[0],self.location[1],100, 30)
      # wall_vertical_line = pygame.Rect(self.location[0],self.location[1],30,100)
      if self.tipe == "l":
         if self.rotation == 0 or self.rotation == 180:
            return[(self.location[0],self.location[1]+100,100,5),(self.location[0],self.location[1],100,5)]
         if self.rotation == 90 or self.rotation == 270:
            return [(self.location[0]+100,self.location[1],10,100),(self.location[0],self.location[1],10,100)]
      if self.tipe == "a":
         if self.rotation == 0:
            return[(self.location[0]+100,self.location[1], 10,100),(self.location[0],self.location[1]+100,100,5)]
         if self.rotation == 90:
            return[(self.location[0]+100,self.location[1], 10,100),(self.location[0],self.location[1],100,5)]
         if self.rotation == 180:
            return[(self.location[0],self.location[1], 10,100),(self.location[0],self.location[1],100,5)]
         if self.rotation == 270:
            return[(self.location[0],self.location[1], 10,100),(self.location[0],self.location[1]+100,100,5)]
      if self.tipe == "t":
         if self.rotation == 0:
            return[(self.location[0],self.location[1]+100, 100,5)]
         if self.rotation == 90:
            return[(self.location[0]+100,self.location[1], 10,100)]
         if self.rotation == 180:
            return[(self.location[0],self.location[1], 100,5)]
         if self.rotation == 270:
            return[(self.location[0],self.location[1], 10,100)]


   # def get_map(self):
      
# line = pygame.Rect(0, 0, 62, 62) #area of source image containing pavement
# angle= pygame.Rect(0, 0, 62, 62) #area of source image containing grass
# three = pygame.Rect(0, 0, 62, 62) #area of source image containing sand/dirt


#matrix containing the pattern of tiles to be rendered
# MAP = [[p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p],\
#        [p,b,b,b,b,b,p,p,p,p,b,b,b,b,b,p],\
#        [p,b,b,g,g,g,g,p,p,g,g,g,g,b,b,p],\
#        [p,b,g,g,g,g,g,p,p,g,g,g,g,g,b,p],\
#        [p,b,g,g,g,p,p,p,p,p,p,g,g,g,b,p],\
#        [p,b,g,s,g,p,s,s,s,s,p,g,s,g,b,p],\
#        [s,s,s,s,s,s,s,g,g,s,s,s,s,s,s,s],\
#        [s,s,s,s,s,s,s,g,g,s,s,s,s,s,s,s],\
#        [p,b,g,s,g,p,s,s,s,s,p,g,s,g,b,p],\
#        [p,b,g,g,g,p,p,p,p,p,p,g,g,g,b,p],\
#        [p,b,g,g,g,g,g,p,p,g,g,g,g,g,b,p],\
#        [p,b,b,g,g,g,g,p,p,g,g,g,g,b,b,p],\
#        [p,b,b,b,b,b,p,p,p,p,b,b,b,b,b,p],\
#        [p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p]]
