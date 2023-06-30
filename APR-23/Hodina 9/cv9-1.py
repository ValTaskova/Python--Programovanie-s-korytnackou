from turtle import *
from random import randint

showturtle()

cislo = randint(1,10)
write(cislo, font=("Arial",30, "normal"))

if cislo >= 1 and cislo < 5:
    pencolor("red")
    forward(100)
    

elif cislo >= 5 and cislo < 10:
    pencolor("green")
    right(90)
    forward(200)
  
done()
