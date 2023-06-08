from turtle import *

showturtle()

def Hviezda(strana, uhol):
    for i in range (8):
        forward(strana)
        right(uhol)
        
def posun(pos):
    penup()
    forward(pos)
    pendown()

penup()
goto(-500,0)
pendown()

strana = 50

for i in range (3):
    Hviezda(strana,135)
    posun(strana+50)
    strana+=50



for i in range (3):
    Hviezda(strana,135)
    posun(strana+50)
    strana-=50


done()
