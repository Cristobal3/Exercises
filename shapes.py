from turtle import *
mode('logo')
speed(9)
shape('turtle')

def square():
    for x in list(range(4)):
        size(10)
        forward(100)
        right(90)
    

def triangle():
    for x in list(range(3)):
        size(50)
        right(120)
        forward(100)
    

def star():
    for x in list(range(5)):
        forward(100)
        right(180-36)
        forward(100)
    

def pentagon():
    for x in list(range(5)):
        forward(100)
        right(360/5)
    

def octagon():
    for x in list(range(8)):
        forward(100)
        right(360/8)
    

circle(100)
square()
triangle()
pentagon()
octagon()
star()
mainloop()

