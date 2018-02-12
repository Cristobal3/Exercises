'''
#Problem 1
list = [1,9,3,4]
suml = 0
for x in list:
    suml += x
print('The sum is ',suml)

#Problem 2
x = 0
larg = list[0]
for y in list:
    if (x+1) < len(list):
        if list[x+1] > larg:
            larg = list[x+1]
            x += 1
        else:
            x += 1
print('The largest number is ',larg)

#Problem 3
x = 0
small = list[0]
for y in list:
    if (x+1) < len(list):
        if list[x+1] < small:
            small = list[x+1]
            x += 1
        else:
            x += 1
print('The smallest number is ',small)

#Problem 4
x = 0
for x in list:
    if x % 2 == 0:
        print(x)

#Problem 5
x = 0
for x in list:
    if x > 0:
        print(x)

#Problem 6
x = 0
z = []
for x in list:
    if x > 0:
        z+=[x]
print('The list of positive numbers is ',z)   

#Problem 7
x = 0
factor = 4

for x in range(len(list)): 
    list[x] *= factor

print(list)    

#Problem 8
list2 = [4,5,1,2]
list3 = []
for x in range(len(list)): 
    list3 += [list[x]*list2[x]]
print(list3)

#Problem 9
a = [[1,3],[2,4]]
b = [[5,2],[1,0]]
c = [[],[]]

for j in range(len(a)):
    for k in range(len(a)):
        c[j]+= [a[j][k] + b[j][k]]

print(c)

#Problem 10
a = [[1,3],[2,4]]
b = [[5,2],[1,0]]
c = [[],[]]

for j in range(len(a)):
    for k in range(len(a)):
        c[j]+= [a[j][k] + b[j][k]]

print(c)
'''
# Problem 11
a = [1,3,2,2,4]
b = []
c = ''

for j in range(len(a)):
    if a[j] == c:
        c = a[j]
    else:
        b.extend([a[j]])
        c = a[j]

     
print(b)


