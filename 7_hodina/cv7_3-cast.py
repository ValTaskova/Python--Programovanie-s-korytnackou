#STVORCE VEDLA SEBA POMOCOU FUNKCIE A FOR CYKLU

from turtle import *

def stvorec():    #definicia funkcie -> nazov + zatvorky a vsetko treba odsadit tabulatorom
    penup()
    forward(200)
    pendown()
    for i in range(4):
        forward(dlzka)
        right(90)

showturtle()

penup()
goto(-400,0)

pendown()
dlzka = 100

for i in range(4):
    stvorec()       #volanie nasej funkcie

done()
