#!/usr/bin/python3

try:
    f = open("filee.py", "r")

    s = f.read()

    print(s)

except FileNotFoundError:
    print("Ceva nu este bine. Probabil ca ai gresit numele fisierului")
except IOError:
    print("Problema IO")
except ValueError:
    print("Problema de variabile")
except Exception:
    print("O eroare")
else:
    f.close()

print("Multumesc pentru utilizare !")

def testFunc (d = 0):
    try:
        a = d + 1
    except TypeError:
        print("Ai gresit tipul valorii introduse")
    else:
        return a

print(testFunc(1))

print(testFunc("str"))

print("Salul. Ai terminat !")