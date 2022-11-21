#STVORCE VEDLA SEBA POMOCOU FOR CYKLU

from turtle import *

showturtle()

penup()
goto(-400,0)
pendown()

dlzka = 100

for i in range(4):    #prvy for ma posunie o 200 doprava
    penup()
    forward(200)
    pendown()
    for j in range(4):  #druhy for mi kresli stvorec
        forward(dlzka)
        right(90)

done()
