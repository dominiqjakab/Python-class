#!/usr/bin/python3

f = open("/home/dj/PycharmProjects/Programare_Python/Module.py", "r")

text = " "
l = [" "]
while text != '':
    text = f.read(50)
    l.append(text)
    print(text)

for i in l:
    print(i)

f.close()

r = open("/home/dj/PycharmProjects/Programare_Python/Module2.py", "a")
print("Writing in file...")
r.write("Text for Python\n")

for i in l:
    r.write(i)

print("Done with writting")

r.close()