def Stvorec():
    for i in range(4):
        forward(100)
        right(90)

from turtle import *

showturtle()

Stvorec()

penup()
goto(-200,0)
pendown()

Stvorec()

done()
