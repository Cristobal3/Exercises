import matplotlib.pyplot as plot
'''
#Problem 1
def helllo(name):
    print('Hello ',name)

#Problem 2
def f(x):
    return x + 1
xs = list(range(-3, 4))
ys = []
for x in xs:
    ys.append(f(x))
plot.plot(xs, ys)
plot.show()

#Problem 3
def sq(x):
    return x**2
xs = list(range(-100,101))
ys = []
for x in xs:
    ys.append(sq(x))
plot.plot(xs,ys)
plot.axis([-100,100, 0, 10000])
plot.show()
'''
#Problem 4
def f(x):
    if x % 2 == 0:
        return -1
    else:
        return 1

ys = []
xs = list(range(-5,6))
for x in range(-5,6):
    ys.append(f(x))

plot.bar(xs,ys)
plot.axis([-6,6, -1.0, 1.0])
plot.show()
    
