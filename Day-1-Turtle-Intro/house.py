#Media Computing with Python
#Day 2 - Draw a house

#create a world and turtle
from turtle import *

#draw the horizon (Green)
left(90)
penup()
goto(-400, -400)
pendown()
pencolor('green')
pensize(40)
right(90)
forward(1000) #now face right

#draw the house (red)
penup()
goto(100, -400)
pendown()
pencolor('red')
pensize(3)
left(90)
forward(150)
right(45)
forward(100)
right(90)
forward(100)
right(45)
forward(150) #now face down

#draw the door (black door)
penup()
goto(125, -400)
pendown()
pencolor('black')
backward(50)
left(90)
forward(25)
right(90)
forward(50)#now face down

#draw the window frame (hot pink)
penup()
goto(200, -300)
pendown()
pencolor('red')
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)


#draw the cross in the window
backward(15)
left(90)
forward(30)
penup()
right(90)
forward(15)
right(90)
forward(15)
right(90)
pendown()
forward(30)
hideturtle()
right(90)
