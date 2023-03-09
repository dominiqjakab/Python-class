#!/usr/bin/python3

# 1. Numar citit de la tastatura se afiseaza daca este par sau impar
print("Programul 1\n")
number = input ("Introduceti un numar:")

if int(number) % 2 == 0:
    print("Numarul %d este par"%(int(number)))
else:
    print("Numarul %d este impar"%(int(number)))
    print("Numarul {} este impar".format(number))

# 2. Chestionar de intrebari de angajare iar input-ul citit de la tastatura afisat
print("\nProgramul 2\n")
print("Esti rugat/a sa raspunzi la urmatoarele intrebari:\n")

q1 = input("Cum te numesti ? ")
q2 = input("Ce job iti doresti ? ")
q3 = input("In cat timp crezi ca poti obtine acest job ? ")
q4 = input("Care sunt pasii pe care trebui sa-i urmezi pentru a te putea angaja ? ")
q5 = input("De cand doresti sa incepi? ")

print("\nCandidatul %s a raspuns astfel la intrebarile de mai sus:"%q1)
print(q2 + "\n" + q3 + "\n" + q4 + "\n" + q5)

# 3. Verificare daca un cuvant este palindrom
print("\nProgramul 3\n")
word = input("Introduceti un cuvant: ")

if word == word[::-1]:
    print("Cuvantul este palidrom")
else:
    print("Cuvantul nu este palindrom")