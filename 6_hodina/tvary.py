from turtle import *

showturtle()

dlzka = 100
speed(30)

for i in range(100):
    forward(dlzka)
    right(175)            #menime uhol od 0 po 180
    #dlzka = dlzka + 5    #pri zvacsovani dlzky sa vykreslia ine obrazce, ale treba nastavit pociatocnu dlzku na mensiu hodnotu
    
done()
