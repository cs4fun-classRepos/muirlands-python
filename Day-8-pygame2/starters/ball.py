import pygame, sys, random, math
from pygame.locals import *

#global variables
#width of the world
width = 400
#height of the world
height = 300
#define the size of the ball
bsize = 10
#define the color of the ball
bcolor = (255, 0, 0)


#get started with the game
pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Pong Game by Muirlands')

xspeeds=[]
yspeeds=[]
bxs=[]
bys=[]
#######################################
### Part 1: Generate speed and location
######################################



############STOP HERE###################
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  surface.fill((255, 255, 255))
  ################################
  #   Part 2: Complete the game below
  ################################



  ######################################
  ##  Don't change the lines below######
  ######################################

  pygame.display.flip()

  fpsClock.tick(30)
