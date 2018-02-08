from turtle import *
mode('logo')
speed(9)
shape('turtle')

def square(size, fill, color):
    pencolor(str(color))
    if fill == 'y':
        begin_fill()
        for x in list(range(4)):
            forward(size)
            right(90)
        end_fill()
    else:
        for x in list(range(4)):
            forward(size)
            right(90)

def triangle(size, fill, color):
    pencolor(str(color))
    if fill == 'y':
        begin_fill()
        for x in list(range(3)):
            right(120)
            forward(size)
        end_fill()
    else:
        for x in list(range(3)):
        right(120)
        forward(size)

def star(size, fill, color):
    pencolor(str(color))
    if fill == 'y'
        begin_fill()
        for x in list(range(5)):
            forward(size)
            right(180-36)
            forward(size)
        end_fill()
    else:
        for x in list(range(5)):
            forward(size)
            right(180-36)
            forward(size)
    

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

