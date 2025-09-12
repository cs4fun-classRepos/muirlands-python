from turtle import *
speed = 0

def turnLeft():
    left(10)
## Complete turnRight below (similar to turnLeft)
def turnRight():
    right(10)

def move():
    global speed
    speed = 1
def pause():
    global speed
    speed = 0

def red():
    pencolor('red')
    pensize(2)


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
screen.onkey(turnRight, "Right")

## Attach turnRight to Right arrow key
screen.onkey(move, 'm')
screen.onkey(pause, 'p')
screen.onkey(red, 'r')
screen.onkey(clear, 'c')
screen.listen()
while True:
    forward(speed)
