from turtle import *

showturtle()

dlzka = 200

for i in range(10):
    forward(dlzka)
    right(100)
    for j in range(20):
        forward(50)
        right(100)

done()
