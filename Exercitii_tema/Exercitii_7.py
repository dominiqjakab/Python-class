#!/usr/bin/python3
import itertools
from collections import OrderedDict
from operator import getitem

#Iar acum sa ne reintoarcem la partea practica si sa concepem o “baza de date”:
#1.1) Creati cu ajutorul unui dictionar o baza de date la care sa retineti numerele de telefon a 10 prieteni

print("Programul 1\nCrearea si afisarea unei baze de date cu numerele de telefon a 10 prieteni")

list = { 1:{'Nume':'Dominiq', 'Telefon':'072466200'},
         2:{'Nume':'Jack', 'Telefon':'0724930680'},
         3:{'Nume':'Gigi', 'Telefon':'072746500'},
         4:{'Nume':'Ion', 'Telefon':'0798782200'},
         5:{'Nume':'Milan', 'Telefon':'07564689200'},
         6:{'Nume':'Ovidiu', 'Telefon':'07468956540'},
         7:{'Nume':'Ioan', 'Telefon':'0724654790'},
         8:{'Nume':'Andrei', 'Telefon':'6549874654'},
         9:{'Nume':'Denis', 'Telefon':'465498798'},
         10:{'Nume':'Cristi', 'Telefon':'1123494654'},
        }

for id, info in list.items():
    print("\nNr.", id)
    for i in info:
        print(i + ':',info[i])

# 1.2) Afisati intrarile din aceasta baze de date in ordine alfabetica, dupa nume.
print("\nProgramul 1.2a\nAfisarea intrarilor in ordine alfabetica, dupa nume, folosind functia OrderedDict\n")
# Method 1  - sort usind OrderedDict
sortedDict = OrderedDict(dict(sorted(list.items(), key=lambda x: getitem(x[1], 'Nume'))))
print("Baza de date sortata\n" + str(sortedDict))

# Method 2 - sort using sorted()
print("\nProgramul 1.2b\nAfisarea intrarilor in ordine alfabetica, dupa nume, folosind functia sorted\n")
sortedDict = sorted(list.items(), key=lambda x: x[1]['Nume'])

print("Baza de date sortata\n" + str(sortedDict))
print("\nAfisarea valorilor sortate\n")
for (key,value) in sortedDict:
    print(value)
    # print(key,":",value)

#2) Scrieti un program pentru a obtine (sortate dupa pret) primele 3 produse dintr-un online magazin.
# Produse magazin: {‘Pantofi’: 45.50, ‘Geaca’: 35, ‘Pulover’: 41.30, ‘Sacou’: 55, ‘Tricou’: 24}

print("\nProgramul 2\nAfisarea primelor 3 produse dintr-un magazin online sortate dupa pret.\n")

magazin = {'Pantofi':45.50,'Geaca': 35, 'Pulover': 41.30, 'Sacou': 55, 'Tricou': 24}
print("Baza de date a magazinului este:\n")
for key,value in magazin.items():
    print(key,value)

sorted_magazin = dict(sorted(magazin.items(), key = lambda x: x[1],reverse=True))

print("\nArticolele sortate dupa pret sunt:\n")
for key, value in sorted_magazin.items():
    print(key,value)

print("\nPrimele 3 articole sortate dupa pret sunt:\n")

out = dict(itertools.islice(sorted_magazin.items(), 3))

for key,value in out.items():
    print(key,value,"\n")

