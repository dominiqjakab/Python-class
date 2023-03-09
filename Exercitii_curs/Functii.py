#!/usr/bin/python3

valoare = input("Introdu un numar: ")

def calcul_suma(valoare):
    suma = 0
    for i in range (int(valoare) +1):
        suma += i
    return suma

# print(type(valoare))
print("Suma pentru " + valoare + " este " + str(calcul_suma(valoare)))

x1 = calcul_suma(3)
x2 = calcul_suma(4)

print("Valoare " + str(x1) + " " + str(x2))

def calcul_persoana(numeF, varstaF):
    print("Ok, te numesti " + numeF + " si ai " + varstaF + " ani ")
    ani = 0
    ani = int(varstaF) + 20
    print("Peste 20 de ani vei avea " + str(ani) + " de ani")
    return

nume = input("Salut! Spune-mi cum te numesti: ")
varsta = input("Cati ani ai: ")

calcul_persoana(nume, varsta)