#!/usr/bin/python3

# l = [5,10,4]
# a = sorted(l)
# print(a)

# f = open("/home/dj/PycharmProjects/Programare_Python/numere/fisier1.txt", "r")
# a = f.read()
# b = sorted(a.strip())
# print(b)

Top_Score = open("/home/dj/PycharmProjects/Programare_Python/numere/fisier1.txt", "r+")
X = []
for line in Top_Score.readlines():
    X.append(int(line))
X.sort()
# print(type(X))
for i in range(len(X)):
    print(X[i])
# print(type(X))
Top_Score.close()


