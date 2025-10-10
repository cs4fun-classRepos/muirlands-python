# Instructions  

Ball movement in the pong game

## Sample starter code

```python
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
#define the location of the ball
bx = width//2
by = height//2
#define the speed of the ball
xspeed = random.randint(-20, 20)
yspeed = random.randint(-10, 10)

#get started with the game
pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Pong Game by Huaxia')

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  surface.blit(bg, (0,0))
  ################################
  #   Complete the game here
  ################################



  pygame.display.flip()

  fpsClock.tick(30)


```