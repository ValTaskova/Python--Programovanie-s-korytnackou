import turtle
from random import randint

hadik = turtle.Turtle()
ovocie = turtle.Turtle()
screen = turtle.Screen()

hadik.forward(100)
ovocie.shape("turtle")
x = randint(100,360)
y = randint(100,300)
ovocie.goto(x,y)
screen.onscreenclick(hadik.goto)    #hadik sa po kliknuti presunie tam, kde sme klikli


def f():
    hadik.forward(50)

screen.onkey(f, "Up")               #hadik po kliknuti sipky hore pojde 50 krokov doprava -> robi to co je vo funkcii f(), po stlaceni klavesi Up
screen.listen()
