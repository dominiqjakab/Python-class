#!/usr/bin/python3
### Scrieti un generator de parole (password generator) in Python. Fiti creativi cu modul in care generati parolele – parolele puternice au un
### amestec de litere mici (abcd…), majuscule (ABCD…), numere (0123…) si simboluri (@!#$…). Parolele trebuie sa fie aleatoare (foloseste modulul random),
### generand o parola de fiecare data cand utilizatorul solicita una noua.
### Include acest cod intr-o functie (best-practice), si apeleaza-o in main.
### Extra: Intreaba-l userul (prin “input()” ) cat de puternica vrea sa fie parola. Pentru parolele slabe, alegeti un cuvant sau doua dintr-o lista.

### Part 0 ### Import the necessary mdules
import random
import secrets
import string

### Part 1 ### Define the alphabet

letters = string.ascii_letters
digits = string.digits
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
special_chars = string.punctuation
alphabet = letters + digits + special_chars
# print(alphabet)

### Part 2 ### Define the function for password generator
def password_generator():
    pass_list = ['password123', '123456', 'qwerty', 'abcd', 'etc.', '0000']
    print("Welcome to the password generator.")
    ### Part 2.1 ### Define the level of strength for the password
    print('''Please choose what type of password would you like:
          1 - weak
          2 - strong''')
    pass_strength = input("Pick a number: ")

    ### Part 2.2 ### Generate the password
    ### For a weak password, a random choice from a list is performed ###
    try:
        if  (int(pass_strength) == 1):
            password = secrets.choice(pass_list)

        elif (int(pass_strength) == 2):
            ### For a strong password, the length and character selection is performed ###
            length = int(input("\nEnter the length of the password: "))
            print('''Choose a character to be included in the password :
                     1. Digits
                     2. Letters - uppercase
                     3. Letters - lowercase
                     4. Special characters
                     5. Exit''')

            tempstring = ''

            ### Getting the character constraint set for the password ###
            while True:
                choice = int(input("Pick a number from the list presented above: "))
                if (choice == 1):
                    #Add digit to the list
                    tempstring += secrets.choice(digits)
                elif (choice == 2):
                    #Add upper character to the list
                    tempstring += secrets.choice(upper_letters)
                elif (choice == 3):
                    #Add lower character to the list
                    tempstring += secrets.choice(lower_letters)
                elif (choice == 4):
                    #Add special character to the list
                    tempstring += secrets.choice(special_chars)
                elif (choice == 5):
                    break
                else:
                    print("Pick a valid option!")
            print("Temporary string is: " +tempstring)
            ### The password is created by a random choice for the remaining characters joined to the initial list ###
            passtemp = tempstring
            print("Length of the string is:", len(passtemp))
            for i in range(length-len(tempstring)):
                # Pick random characters from the remaining characters
                randomchar = secrets.choice(alphabet)
                passtemp += randomchar
            password = ''.join(random.sample(passtemp,len(passtemp)))
        else:
            print("Pick a valid option!")
            exit()
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        exit()

    return password

if __name__== '__main__':
    password = password_generator()
    print("\nYour password is: " + str(password))