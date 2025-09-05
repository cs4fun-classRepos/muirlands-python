# Functions in python

A fuction is like a module in codes that does a specific job. Like a chef, a plumber, a teacher in life. They do a specific job when you ask them to.

## Syntax
```python
def function_name (param list):
    things this function do
```

## Example
```python
def nameLength(name):
    return name.size()

def f2c(f):
    c = 5/9*(f-32)
    return c
```
 <div style="page-break-after: always;"></div>
 
## Control turtle movement using keypad

```python
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

```