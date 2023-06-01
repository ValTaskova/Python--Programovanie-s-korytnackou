from turtle import *

showturtle()

prirastok = 10
stranaStvorca = 10

cislo = 100

uhol = 90
#strana = cislo + uhol * 5

cislo = cislo + prirastok
cislo = cislo + prirastok

cislo += 50

write(cislo)

forward(cislo)
right(uhol)

forward(cislo + 100)
right(uhol)

forward(cislo)
right(uhol)

forward(cislo + 100)
right(uhol)

done()
