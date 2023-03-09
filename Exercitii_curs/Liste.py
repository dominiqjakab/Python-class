#!/usr/bin/python3

l = [1,2,3,4,5]
l[0] = "Retele"
l[4] = "Python"
del l[2]
len(l)
print(len(l))
l.append(1)
print(len(l))
print(l)

l.insert(2,"Linux")
print(l)

'1' in l
