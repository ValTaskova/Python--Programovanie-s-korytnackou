from turtle import *
from random import randint 

def utvar(dlzka, pocet, uhol):
    for i in range(pocet):
        forward(dlzka)
        right(uhol)

showturtle()

dlzka = randint(50,100)
pocet = 100
uhol = randint(0,180)
write(dlzka, font=("Arial", 30, "italic"))

if dlzka < 60:  
    dlzka = 60
    
if dlzka == 60:  
    dlzka = 60

if dlzka > 0 and dlzka < 5:       #ak je dlzka vacsia ako 0 A ZAROVEN je mensia ako 5
    dlzka = 80

penup()
goto(randint(-500,500),randint(-500,500))
pendown()

write(dlzka)

utvar(dlzka, pocet, uhol)

done()
