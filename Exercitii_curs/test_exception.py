#!/usr/bin/python3
#
# a = input("Insert option 1 sau 2:")
import random

# try:
#     if (int(a) == 1):
#         print("OK")
#     else:
#         print("ALta valoare numerica")
# except ValueError:
#     print("NU este valoare numerica")

string = 'this is a string'
print(string+str(len(string)))
string_letters = list(string)
random.shuffle(string_letters)
string_shuffled = ''.join(string_letters)
print(string_shuffled + str(len(string_shuffled)))