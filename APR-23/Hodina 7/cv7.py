from turtle import *

showturtle()
def Hviezda():
    for i in range (8):
        forward(100)
        right(135)

def Stvorec():
    for i in range (4):
        forward(100)
        right(90)

def posun():
    penup()
    forward(200)
    pendown()

penup()
goto(-500,0)
pendown()

for i in range (6):
    Stvorec()
    posun()
    Hviezda()
    posun()

done()
