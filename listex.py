import numpy
import math
#Problem 1
list = numpy.random.random((1,5))
sumnum = sum(list)

#Problem 2
x = 0
larg = list[0]
if (x+1) < len(list):
    if list[x+1] > larg:
        larg = list[x+1]
        x += 1
    else:
        x += 1
else:
    print(larg)



largnum = max(list)