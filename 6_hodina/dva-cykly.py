from turtle import *

showturtle()

dlzka = 50
speed(30)
for i in range(10):
    forward(dlzka)
    right(100)
    #dlzka = dlzka + (i%5)
    for j in range(20):
        forward(20)
        right(5)

done()
