#!/usr/bin/python3

# 1.1 Suma nr de la 1 la 100 folosind bucla for
print("Programul 1.1")
print("Afisarea sumei numerelor de la 1 la 100 dupa ce programul a folosit bucla for")
sumf = 0
for i in range (1,101):
    sumf += i
print("Suma numerelor de la 1 la 100 este %d."%sumf)

# 1.2 Suma nr de la 1 la 100 folosind bucla for
print("\nProgramul 1.2")
print("Afisarea sumei numerelor de la 1 la 100 dupa ce algoritmul a folosit bucla while")

sumw = 0
i = 1
while i <= 100:
    sumw += i
    i += 1
print("Suma numerelor de la 1 la 100 este %d."%sumw)

# 1.3 Dinamizarea programului citind de la tastatura capatele de interval
print("\nProgramul 1.3")
print("Afisarea sumei numerelor citind de la tastatura capetele de interval\n")
lower = int(input("Introduceti capatul inferior al intervalului:"))
upper = int(input("Introduceti capatul superior al intervalului:"))
sum = 0

if  lower < upper:
    for i in range(lower,upper+1):
       sum += i
    print("\nSuma numerelor de la %d la %d este %d" % (lower, upper, sum))
else:
    print("\nNumerele introduse pentru capetele de interval nu sunt corespunzatoare.")

# 2. Joc Hartie-Piatra-Foarfece pentru 2 persoane. In momentul in care castiga cineva,
#   se printeaza un mesaj de felicitare si daca se doreste sa inceapa un joc nou.

# Reguli:
    # Piatra bate foarfeca
    # Foarfeca bate hartia
    # Hartia bate piatra

import time
from os import system

print("\nProgramul 2\n")
print ("Bine ati venit la Hartie-Piatra-Foarfece\n")
player1 = input("Numele primului jucator este: ")
player2 = input("Numele celui de-al doilea jucator este: ")

print ("\nPentru acest joc, se vor introduce de la tastatura:\n1 - Hartie\n2 - Piatra\n3 - Foarfece")
# system("clear")
enter = input("\nApasa Enter pentru a porni jocul...")
print('\n'*10)
time.sleep(1)
play = 1
while play == 1:
    print("Conventie:\n1 - Hartie\n2 - Piatra\n3 - Foarfece\n")
    option1 = int(input("Jucatorul %s este rugat sa alega una dintre optiunile numerice de mai sus: "%player1))
    print('\n' * 10)
    print("Conventie:\n1 - Hartie\n2 - Piatra\n3 - Foarfece\n")
    option2 = int(input("Jucatorul %s este rugat sa alega una dintre optiunile numerice de mai sus: "%player2))
    print('\n' * 10)
    time.sleep(0.1)

    if option1 == 1 and option2 == 2:
        print("%s - Hartie, %s - Piatra"%(player1,player2))
        print("\nFelicitari %s, ai castigat!"%player1)
    elif option1 == 1 and option2 == 3:
        print("%s - Hartie, %s - Foarfece" %(player1, player2))
        print("\nFelicitari %s, ai castigat!"%player2)
    elif option1 == 2 and option2 == 1:
        print("%s - Piatra, %s - Hartie" % (player1, player2))
        print("\nFelicitari %s, ai castigat!" % player2)
    elif option1 == 2 and option2 == 3:
        print("%s - Piatra, %s - Foarfece" % (player1, player2))
        print("\nFelicitari %s, ai castigat!" % player1)
    elif option1 == 3 and option2 == 1:
        print("%s - Foarfece, %s - Hartie" % (player1, player2))
        print("\nFelicitari %s, ai castigat!" % player1)
    elif option1 == 3 and option2 == 2:
        print("%s - Foarfece, %s - Piatra" % (player1, player2))
        print("\nFelicitari %s, ai castigat!" % player2)
    elif option1 == option2:
        print("\nJocul s-a terminat la egalitate")
    else:
        print("\nS-au introdus alte numere fata de conventia enuntata la inceput.")

    time.sleep(5)
    print('\n' * 10)
    play = int(input("\nMai doriti sa jucati? 1 pentru Da, 2 pentru Nu: "))

print("\nJocul s-a terminat. Sper ca ti-a placut.")