#!/usr/bin/python3

from collections import OrderedDict
from operator import getitem

a = {1:{'Nume':'Dominiq', 'Varsta':28},
     2:{'Nume':'Bianca', 'Varsta':29},

    }

print("The original dictionary is:\n")
print(a)
print("\n")

res = OrderedDict(sorted(a.items(), key= lambda x: getitem(x[1],'Nume')))
res2 = dict(sorted(a.items(), key = lambda x: x[1]['Nume']))

print("The sorted dictionary is:\n")
# print(res)
print(res2)

d = {'Masina':25, 'Apa':28, 'Zbor':13}
ordered = dict(sorted(d.items(), key = lambda x: x[0]))
print(ordered)
