import turtle

tur = turtle.Turtle()
scr = turtle.Screen()

def movfr():
    tur.fd(10)

def movbk():
    tur.backward(10)

def anticlk():
    head = tur.heading()+10
    tur.setheading(head)
def clk():
    head = tur.heading()-10
    tur.setheading(head)
def clr():
    tur.reset()

scr.listen()
scr.onkey(key="w",fun=movfr)
scr.onkey(key="a",fun=anticlk)
scr.onkey(key="s",fun=movbk)
scr.onkey(key="d",fun=clk)
scr.onkey(key="c",fun=clr)













scr.exitonclick()

