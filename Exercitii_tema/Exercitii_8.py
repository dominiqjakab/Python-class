#!/usr/bin/python3

# Exercitiul destinat acestui capitol este urmatorul:
# Creeaza un program care citeste numerele din cele 3 fisiere atasate AICI. Dupa citire aceste numere vor fi sortate
# in ordine crescatoare si vor fi scrise intr-un fisier nou denumit “rezultat.txt”. Pe prima linie se va scrie cel mai
# mare numar dintre cele citite, urmat numarul total de elemente citite din cele 3 fisiere.

import os
import ast

print("Programul citeste numerele din 3 fisiere .txt, determina maximul si numarul de elemente si apoi le scrie in "
      "fisierul rezultat.txt\n")



def get_files_dir(dir):
    ### Functie care colecteaza calea fisierelor .txt ce contin numere si urmeaza sa fie citite ###
    all_files = os.listdir(dir)
    txt_files = []
    for file in all_files:
        full_path = os.path.join(dir,file)
        if file.find('.txt') != -1:
            txt_files.append(full_path)
        else:
            pass
    return txt_files

def merge_data(files):
    ### Functie pentru concatenarea datelor din mai multe fisiere intr-un singur fisier ###
    with open(r'/home/dj/PycharmProjects/Programare_Python/numere/rezultat.txt','w') as outfile:
        for file in files:
            with open(file) as infile:
                outfile.write(infile.read()+ '\n')

def max_num_in_file(filename):
    ### Functie care determina maximul dintr-un set de numere scrise intr-un fisier ###
    with open(filename, "r") as f:
        data = f.readlines()
    return (int(max(data)))

def number_elements_file(filename):
    ### Functie care determina numarul numerelor scrise intr-un fisier ###
    with open(filename, "r") as f:
        data = f.readlines()
    return (len(data) - data.count('\n'))

path = r'/home/dj/PycharmProjects/Programare_Python/numere'
# print(path)
files = get_files_dir(path)
# print(files)
merge_data(files)
# f = open('/home/dj/PycharmProjects/Programare_Python/numere/rezultat.txt','r')


filename = r'/home/dj/PycharmProjects/Programare_Python/numere/rezultat.txt'
max_val = max_num_in_file(filename)
count_val = number_elements_file(filename)
print("Maximul si numarul elementelor:")
print(str(max_val) + " " + str(count_val))

f = open('/home/dj/PycharmProjects/Programare_Python/numere/rezultat.txt','r')
x = []
a = f.read()
f.close()
print("\nValorile din fisierul rezultat.txt sunt:")
print(a)
prepend = open('/home/dj/PycharmProjects/Programare_Python/numere/rezultat.txt','w+')
prepend.write(str(max_val) + " " + str(count_val)+ "\n" +a)
# result = []
# for i in f.readlines():
#     x.append(i.strip())
# result = sorted(x)
# print(result)

# for i in range(len(result)):
#     print(result[i])









