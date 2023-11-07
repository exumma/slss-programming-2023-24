# Pumpkin Drawing
# Author: Emma Xu
# Date: 31 October 2023

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(5, 0)
carver.pensize(10)
carver.pendown()
carver.setpos(0,5)
carver.setpos(-5,0)
carver.setpos(5,0)

# Left eye
carver.penup()
carver.setpos(-30, 20)
carver.dot(30)
carver.penup()

carver.setpos(-30,25)
carver.pensize(10)
carver.pendown()
carver.backward(20)

# Right eye
carver.penup()
carver.setpos(30,20)
carver.dot(30)

carver.setpos(30,25)
carver.pensize(10)
carver.pendown()
carver.forward(20)

# Mouth
carver.penup()
carver.setpos(-60,-30)
carver.pensize(10)
carver.pendown()
carver.setpos(-40,-40)
carver.pensize(10)
carver.setpos(-20,-30)
carver.setpos(0,-40)
carver.setpos(20,-30)
carver.setpos(40,-40)
carver.setpos(60,-30)


# Stem
carver.penup()
carver.color("green")
carver.setpos(0,95)
carver.pendown()
carver.pensize(30)
carver.setpos(10,130)
carver.pensize(40)

turtle.done()