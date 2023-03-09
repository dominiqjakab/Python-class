#!/usr/bin/pythonn3

import codecs
from urllib import request, response, error, parse

url = "https://google.ro"
# print(dir(request))
raspuns_server = request.urlopen(url)
date = raspuns_server.read()

try:
    fisier_html = open("/home/dj/PycharmProjects/Programare_Python/Aplicatii/site_downloadat.html", "w")
    fisier_html.write(str(date))
except Exception:
    print("Procesul nu s-a incheiat cu succes.")
else:
    fisier_html.close()

print("Job done.")
