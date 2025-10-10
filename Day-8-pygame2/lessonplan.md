# Lesson plan
  
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
hspeed = random.randint(-10, 10)
vspeed = random.randint(-10, 10)

#create a reflect function

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
    ################################
    #   Complete the game here
    ################################
    #Paint the world
    surface.fill((0, 255, 255))

    #update the ball's location
    bx += hspeed
    by += vspeed

    #bounce the ball if needed
    if bx < 10 or bx > 390:
        hspeed = -hspeed
        bsize+=2
    
    if by < 10 or by > 290:
        vspeed = -vspeed
        bsize+=2

    #draw the ball
    pygame.draw.circle(surface, bcolor, (bx, by), bsize, 0)




    
    pygame.display.flip()
    
    fpsClock.tick(30)





    

```