from turtle import *
from random import randint

showturtle()

cislo = randint(1,6)

for i in range(4):
    forward(100)
    right(90)

penup()
goto(40,-70)
pendown()

write(cislo, font=("Arial",30,"normal"))

done()
