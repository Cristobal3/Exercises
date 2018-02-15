'''
#PRoblem 1
for x in range(1,11):
    print(x)

#Problem 2
start = int(input('Starting number? '))
end = int(input('Ending number? '))
for x in range(start,end):
    print(x)

#Problem 3
for x in range(1,11):
    if x % 2 != 0:
        print(x)

#Problem 4
for x in range(5):
    print('*****')

#Problem 5
n = int(input('How big is the square? '))
sq = '*' * n
for x in range(n):
    print(sq)

#Problem 6
w = int(input('What is the width of the box? '))
h = int(input('What is the height of the box? '))
for x in range(1,h+1):
    if x == 1:
        print('*'* w)
    elif x == h:
        print('*'* w)
    else:
        print('*' + ' '*(w-2) + '*' )
        

#Problem 7
print('   *   ')
print('  ***  ')
print(' ***** ')
print('*******')


#Problem 8
h = int(input('Height of the triangle? '))
for x in range(1,h+1):
    print(' '*(h-x) + '*' * x + '*' * (x-1)+ ' '*(h-x) )
'''
#Problem 9
x = range(1,11)
for y in x:
    for z in x:
        mu = y * z
        print(y,' X ',z, ' = ',mu)

 


