from turtle import*
from random import randint

showturtle()

loteria = randint(0,30)
write(loteria)
forward(20)

if (loteria <= 5):
    write("MALO ALEBO NIC SI NE/VYHRAL, HOR SA HOR ZNOVA DAT STAVKU!") 
elif (loteria > 5 and loteria <= 20):
    write("CELKOM SLUSNA VYHRA")
elif (loteria > 20 and loteria <= 29):
    write("SKORO SI TO CELE VYHRAL!")
else :
    write("KOMPLETNA VYHRA! GRATULUJEM...")
  
done()
