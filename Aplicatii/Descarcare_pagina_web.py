#!/usr/bin/pythonn3

### Algorithm used to scrape a web page in a html file - version 1
### apt-get install urllib2-file urllib3

### Part 0 ### Import necessary modules
import codecs
from urllib import request, response, error, parse

### Part 1 ### Define the url and request from the server
url = "https://google.ro"
# print(dir(request))
reply_server = request.urlopen(url)
data = reply_server.read()

try:
    fisier_html = open("/home/dj/PycharmProjects/Programare_Python/Aplicatii/site_downloadat.html", "w")
    fisier_html.write(str(data))
except Exception:
    print("The process finished unsuccesfully.")
else:
    fisier_html.close()

print("Job done.")
