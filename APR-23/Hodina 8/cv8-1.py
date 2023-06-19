from turtle import *
from random import randint

showturtle()
colormode(255)  #farbu mozeme zadat v RGB formate

def stvorec(strana, x, y):
    penup()
    goto(x,y)
    pendown()
    for i in range(4):
        forward(strana)
        right(90)

for i in range(10):
    color(randint(0,255),randint(0,255),randint(0,255))
    strana = randint(20,150)
    x = randint(-200,200)
    y = randint(-200,200)
    stvorec(strana, x, y)
#write(cislo, font=("Arial",30,"normal"))

done()
