#!/usr/bin/python3

# 1. Lista a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Sa se scrie o linie Python care ia lista
# si face o noua lista care contine doar elementele pare are acesteia.
print("Programul 1\nPentru lista urmatoare se selecteaza si se stocheaza intr-o alta lista doar elemente pare.")
print("\nLista completa")
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b =[]

def odd_elements(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            b.append(a[i])
    return b
print(a)
b = odd_elements(a)
print("\nLista cu elemente pare")
print(b)

# 2. Creati o list cu numele a 10 prieteni, nu trebuie sa fie distince. Sa se rezolve urmatoarele cerinte
#   Sortati lista de nume.
#   Utilizand o lista auxiliara, determinati numarul de aparitii al fiecarui nume.
#   Determinati numele care apare de cele mai multe ori in lista initiala.
#   Determinati numele care apar cel mai putin ori in lista initiala.
#   Revenind la lista initiala de nume, inversati ordinea elementelor.

print("\nProgramul 2.1\nPentru o lista de 10 nume, se efectueaza urmatoarele operatii\n")
from collections import Counter

print("Lista de nume")
list = ['Dominiq', 'Ion', 'Gigi', 'Popescu', 'Ion', 'Alex', 'Calin', 'Dan', 'Dominiq', 'Ion']
print(list)

print("\nLista sortata")
list.sort()
print(list)

print("\nAfisarea numarului de aparitii pentru fiecare nume")
print(Counter(list))

print("\nAfisarea numelui care are cele mai multe aparitii folosind functia max")
print(max(list,key=list.count))

print("\nAfisarea numelui care are cele mai multe aparitii folosind functia modulul Counter")
print(Counter(list).most_common(3))

print("\nAfisarea numelui care are cele mai putine aparitii folosind functia min")
print(min(list, key=list.count))

print("\nAfisarea numelui care are cele mai putine aparitii folosind functia modulul Counter")
print(Counter(list).most_common()[-1])

print("\nAfisarea listei sortata in ordine inversa")
list.reverse()
print(list)

# 2.2 Formati perechi de 2 persoane cu numele din lista initiala si impartiti lista in 2 liste (in mod egal).
#   Asigurati-va ca acestor perechi nu li se poate modifica valoarea - tupluri.
#   Avand aceste perechi, calculati nr total de caractere pentru fiecare perechein parte si creati o lista noua
#   in care sa introduceti valoare in ordine descrescatoare.

print("\nProgramul 2.2\nAcest program impart o lista de nume in doua liste si apoi se fac cateva operatii cu acestea.\n")

print("Lista de nume")
list = ['Dominiq', 'Ion', 'Gigi', 'Popescu', 'Ion', 'Alex', 'Calin', 'Dan', 'Dominiq', 'Ion', 'Florin', 'Calin']
print(list)

#o = [(list[i],list[i+1]) for i in range(0,round(int(len(list))/2),2)]
# p = [(list[i],list[i+1]) for i in range(round(int(len(list))/2),int(len(list)),2)]

o = []
p = []

for i in range(0,round(int(len(list))/2),2):
    o.append((list[i],list[i+1]))
for i in range(int(len(list)/2),int(len(list)),2):
    p.append((list[i],list[i+1]))

print("\nPrima lista de nume")
print(o)
print("\nA doua lista de nume")
print(p)

a = tuple(o)
b = tuple(p)

print("\nPrima lista de nume transformata in tuplu")
print(a)
print("\nA doua lista de nume transformata in tuplu")
print(b)

def pair_characters(a):
    ### Functie pentru calcului numarului total de caractere al unei perechi de nume###
    nr = []
    for i in range(0,int(len(a))):
        for j in range(1,int(len(a))-1):
            nr.append(len(a[i][j-1])+len(a[i][j]))
    return nr

number_char = pair_characters(a) + pair_characters(b)

print("\nNumarul total de caractere pentru fiecare pereche de nume este:")
print(number_char)
number_char.sort()
number_char.reverse()
print("\nLista cu numarul total de caractere pentru fiecare pereche afisata in ordine descrescatoare:")
print(number_char)

#3 Script care afiseaza toate nr divizibile cu 7 din  [0,3463]
# Ajustati codul astfel incat la aparitia primului multiplu al lui 666, algoritmul sa se opreasca.
# print("\nProgramul 3\nAfisarea numerelor divizibile cu 7 pana la numarul 666:\n")
for i in range(3463):
    if i % 7 == 0 and i< 666:
        print(i)

print("\nProgramul s-a oprit.")