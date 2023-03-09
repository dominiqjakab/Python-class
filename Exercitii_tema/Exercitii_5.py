#!/usr/bin/python3

# 1. Afisarea numarului de caractere dintr-un string folosind o functie
print("Programul 1\nAfisarea numarului de caractere pentru un cuvant citit de la tastatura.")
def length(word):
    print("Sirul de caractere %s are numarul de caractere:"%word + str(len(word)))

def length_nospaces(word):
    length_input = len(word) - word.count(' ')
    print("Sirul de caractere %s are numarul de caractere:"%word + str(length_input))

i = 1
while i == 1:
    if i == 1:
        word = input("\nIntroduceti un cuvant: ")
        length_nospaces(word)
    i = int(input("\nDoriti sa mai introduceti un cuvant? 1 - Da, 2 - Nu: "))
print("\nProgramul s-a terminat.")


# 2. Afisarea inversului unui numar sau string
print("\nProgramul 2\nAfisarea numarului de caractere pentru un cuvant citit de la tastatura.")
def invers(string):
    print("The reverse of %s is %s"%(word,word[::-1]))

i = 1
while i == 1:
    if i == 1:
        word = input("\nIntroduceti un cuvant sau numar: ")
        invers(word)
    i = int(input("\nDoriti sa mai introduceti un cuvant? 1 - Da, 2 - Nu: "))
print("\nProgramul s-a terminat.")

