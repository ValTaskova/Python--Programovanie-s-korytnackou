from turtle import *
from random import randint

showturtle()

cislo = 6

if cislo < 10:
    forward(100)
if cislo < 5:
    left(90)
    forward(200)
else:
    right(90)
    forward(200)
    
done()
