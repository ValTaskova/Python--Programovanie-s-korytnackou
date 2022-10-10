from turtle import *

#Toto je komentar

showturtle()    #Ukaze korytnacku    

bgcolor('medium violet red')    #zmeni farbu pozadia

pensize(8)          #Zmeni hrubku pera
color('#458B74')    #Zmeni farbu pera 
forward(100)

pensize(10)
color('Navy')
forward(100)

left(90)
penup()             #Zdvihne pero z papiera
forward(100)

left(90)
pendown()           #Polozi pero na papier
color('light salmon')
forward(200)


penup()
forward(200)
pendown()

write("CIARA \"?\" ", font=("Arial", 30, "italic"))     #Napise slovo v uvodzovkach
                                                        #font nastavuje pismo, velkost a styl

left(90)
penup()
forward(200)


pendown()

fillcolor('yellow')     #Vyplni utvar farbou
begin_fill()            #Zacina sledovat co ma vyplnit

left(90)                #Nas utvar - trojuholnik
forward(100)
left(120)
forward(100)
left(120)
forward(100)

end_fill()              #Prestane sledovat a vyplni utvar farbou 

done()



