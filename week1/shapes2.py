from turtle import *
mode('logo')
speed(9)
shape('turtle')

def square(size, fill, color):
    pencolor(color)
    if fill == 'y':
        begin_fill()
        fillcolor(color)
        for x in list(range(4)):
            forward(size)
            right(90)
        end_fill()
    else:
        for x in list(range(4)):
            forward(size)
            right(90)

def triangle(size, fill, color):
    pencolor(color)
    if fill == 'y':
        begin_fill()
        fillcolor(color)
        for x in list(range(3)):
            right(120)
            forward(size)
        end_fill()
    else:
        for x in list(range(3)):
            right(120)
            forward(size)

def star(size, fill, color):
    pencolor(color)
    if fill == 'y':
        begin_fill()
        fillcolor(color)
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
    

def pentagon(size, fill, color):
    pencolor(color)
    if fill == 'y':
        begin_fill()
        fillcolor(color)
        for x in list(range(5)):
            forward(size)
            right(360/5)
        end_fill()
    else:
        for x in list(range(5)):
            forward(size)
            right(360/5)
        

    

def octagon(size, fill, color):
    pencolor(color)
    if fill == 'y':
        begin_fill()
        fillcolor(color)
        for x in list(range(8)):
            forward(size)
            right(360/8)
        end_fill()
    else:
        for x in list(range(8)):
            forward(size)
            right(360/8)
        


    
'''
circle(size)
square()
triangle()
pentagon()
octagon()
star()
'''

def draw():
    mainloop()
    

