import turtle


def triangle(t):
    for i in range(3):
        t.forward(50)
        t.left(120)
        
def square(t):
    for i in range(4):
        t.forward(50)
        t.left(90)


def squares(t, n):
    for _ in range(n):
        square(t)
        t.left(360//n)
        
t = turtle.Turtle()
squares(t,5)
t.up()
t.goto(50, 100)
t.down()
triangle(t)