from turtle import *

showturtle()

pensize(5)
bgcolor('#912658')

pencolor('#5ead93')
forward(100)
left(90)

color('purple')
forward(200)
left(90)

color('#12876a')
forward(100)
left(90)

color('pink')
forward(200)
left(90)

color('yellow')
write("napiš", font=("Arial", 30, "italic"))    #normal, italic, bold

#right(90)
#delay(1000)
#speed(1000)
color('red')    #pravy ALT + P

#penup()
#pendown()

#delay(1000)
fillcolor('#12876a')
begin_fill()

circle(100)

penup()
forward(100)
pendown()

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
#forward(100)

end_fill()

done()
