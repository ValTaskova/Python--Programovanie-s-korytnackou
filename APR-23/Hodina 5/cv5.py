from turtle import *

showturtle()

speed(1000)

strana = 5
for pocet in range (1, 500): 
    strana += 5
    forward(strana)
    right(290)  #cisla od 0 do 360


done()
