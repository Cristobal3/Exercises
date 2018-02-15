'''
#Problem 1
m = 'testing string uppercase code'
print(m.upper())

#Problem 2
m = m[0].upper() + m[1:]
print(m)

#Problem 3
m = 'testing string uppercase code'
n = ''
for x in range(-1,-1*len(m)-1,-1):
    n += m[x]
print(n)

#Problem 4
l = 'leet'.upper()
n = '' #empty string to house the new coverted string
con = 'AEGIOST' #letters that need to be switched
og = '4361057' #the number corresponding to each letter
an = 'n' #indicator variable for wether or not string was moded
for x in range(len(l)):
    for y in range(len(og)):
        if l[x] == con[y]:
            n += og[y]
            an = 'y'
    if an == 'y':
        pass
    else:
        n += l[x]
print(n)

#Problem 5
st = 'Good'
p = ''
st2 = ''
for x in range(len(st)):
    if st[x] == p:
        st2 += 4*st[x]
        p = st[x]
        print(st2)
    else:
        st2 += st[x]
        p = st[x]
        print(st2)
print(st2)
'''
#Problem 6
cip = "lbh zhfg hayrnea jung lbh unir yrnearq"
plain = 'abcdefghijklmnopqrstuvwxyz'
cipher =''
an = ''
push = plain.index('r') - plain.index('e')
for x in range(len(plain)):
    if x+push > (len(plain)-1):
        y = push - (len(plain)-x)
        cipher += plain[y]
    else:
        cipher += plain[x+push] 
print(cipher)

for x in range(len(cip)):
    if cip[x] != ' ': 
        an += plain[cipher.index(cip[x])]
    else:
        an += cip[x]
print(an)

    

     

        


