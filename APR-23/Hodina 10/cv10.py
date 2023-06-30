import turtle
from random import randint

turtle.showturtle()
screen=turtle.Screen()

turtle.colormode(255)

screen.setup(width=400, height=400)

turtle.shape("turtle")

def dopredu():
    turtle.forward(100)

def vymaz(x, y):
    turtle.right(90)

def farba(x, y):
    turtle.bgcolor(randint(0,255),randint(0,255),randint(0,255))


turtle.Screen().onkey(dopredu, "a")     #to iste ako screen.onkey(dopredu, "a")
screen.listen()

turtle.onscreenclick(farba)     #funkcia farba musi obsahovat v zapise (riadok 19) argumenty x a y
