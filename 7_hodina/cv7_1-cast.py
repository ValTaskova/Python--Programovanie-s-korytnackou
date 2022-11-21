#STVORCE VEDLA SEBA

from turtle import *

showturtle()

penup()
goto(-300, 0)     #posuniem sa dolava aby som mohla stvorce kreslit vedla seba
pendown()

dlzka = 100

for i in range(4):
    forward(dlzka)
    right(90)

penup()
forward(200)    #posunie ma o 100 + 100 -> prvych 100 je strana stvorca ktoru musime prejst, druhych 100 je velkost medzere medzi stvorcami
pendown()
    
for i in range(4):
    forward(dlzka)
    right(90)

penup()
forward(200)
pendown()
    
for i in range(4):
    forward(dlzka)
    right(90)

penup()
forward(200)
pendown()
    
for i in range(4):
    forward(dlzka)
    right(90)
        
done()
