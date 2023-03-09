#!/usr/bin/python3

# Program pentru introducere de la tastatura a numelui si varstei
# Afisarea anului cand va implinii 100 de ani

import datetime
date = datetime.date.today()

nume1 = input("Care este numele tau? ")
varsta1 = input("Ce varsta ai? ")
print(f"Salut, {nume1} !\nTu ai {varsta1} de ani. \nIn anul {date.year - int(varsta1) +100} vei face 100 de ani.")

print("\nUrmatoarea persoana:")
nume2 = input("Care este numele tau? ")
varsta2 = input("Ce varsta ai? ")
print("\nUrmatoarea persoana:")
nume3 = input("Care este numele tau? ")
varsta3 = input("Ce varsta ai? ")
print("\nUrmatoarea persoana:")
nume4 = input("Care este numele tau? ")
varsta4 = input("Ce varsta ai? ")

print(f"\n{nume2} are {varsta2} de ani. \nIn anul {date.year - int(varsta2) +100} va 100 de ani.")
print(f"\n{nume3} are {varsta3} de ani. \nIn anul {date.year - int(varsta3) +100} va 100 de ani.")
print(f"\n{nume4} are {varsta4} de ani. \nIn anul {date.year - int(varsta4) +100} va 100 de ani.")