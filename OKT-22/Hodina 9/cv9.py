import turtle   #musime napisat kniznicu takto

prva = turtle.Turtle()
druha = turtle.Turtle()

prva.showturtle()
druha.showturtle()

druha.penup()
druha.goto(200,100)
druha.pendown()

def stvorec():
    for i in range(4):
        druha.forward(100)    #aj vo funkcii musime povedat, ktora korytnacka, inak vyhodi chybu
        druha.left(90)

prva.circle(50)

stvorec()

prva.done()
druha.done()
