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
for i in range(10):
  bxs.append(random.randint(0, 200))
  bys.append(random.randint(0, 200))
  xspeeds.append(random.randint(-3, 3))
  yspeeds.append(random.randint(-3, 3))



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
  for i in range(10):

    bxs[i] +=xspeeds[i]
    bys[i] +=yspeeds[i]

    if bxs[i] < 10 or bxs[i] > width - 10:
      xspeeds[i] *=-1
    if bys[i] < 10 or bys[i] > height - 10:
      yspeeds[i] *= -1
    pygame.draw.circle(surface,(0, 0, 255), (bxs[i], bys[i]),bsize)




  ######################################
  ##  Don't change the lines below######
  ######################################

  pygame.display.flip()

  fpsClock.tick(30)
