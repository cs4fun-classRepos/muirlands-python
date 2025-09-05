from turtle import *
speed = 0

def turnLeft():
    left(10)
## Complete turnRight below (similar to turnLeft)


def move():
    global speed
    speed = 1

## Complete pause below (similar to start)

#setup the turtle
shape('turtle')
showturtle()
penup()

# bind key strokes to functions
screen = Screen()
screen.onkey(penup, "Up")
screen.onkey(pendown, "Down")
screen.onkey(turnLeft, "Left")
## Attach turnRight to Right arrow key
screen.onkey(move, 'm')
## Attach pause to letter p
screen.listen()
while True:
    forward(speed)