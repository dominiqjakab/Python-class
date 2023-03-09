#!/usr/bin/python3

d={"Nume":"Dominiq", "Varsta": 28, "Domeniu":"IT"}
d2={"Nume":"Adi", "Varsta": 25, "Domeniu":"Financiar"}
# print(type(d))

# print(d["Varsta"])

# d['Nume'] = 'Adi'

print(d.get('Nume'))
print(d.keys())
print(d.items())

l = [d, d2]

for i in l:
    print("In baza de date avem :")
    print(i.get('Nume'))