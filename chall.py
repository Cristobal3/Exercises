#Algorithm 1
'''
list = list(range(1,101,1))
for x in list:
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)

#Algorithm 2
list = list(range(1,1000,1))
sum = 0
for x in list:
    if x % 3 == 0 and x % 5 == 0:
        sum += x
    elif x % 3 == 0:
        sum += x
    elif x % 5 == 0:
        sum += x
    else:
        pass
print(sum)

#Algorithm 3
fib = [1,2]
x = 0
while True:
    if max(fib) <= 4000000:
        fib.extend([fib[x] + fib[x+1]])
        x += 1
    else:
        break
even = 0

for x in fib:
    if x % 2 == 0:
        even += x

print(even)

'''
#algorithm 4
x = 600851475143
def prime(x):
    if x % 2 == 0:
        x /= 2
        prime(x)
    elif x % 3 == 0:
        x /= 3
        prime(x)
    elif x % 5 == 0:
        x /= 5
        prime(x)
    else:
        print(x)
prime(x)