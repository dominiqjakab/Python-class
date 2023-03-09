#!usr/bin/python3

### Algorithm used to scrape a web page in a html file - version 2
### apt-get install beautifoulsoup4 requests

import requests
from bs4 import BeautifulSoup
from urllib import request, response, error, parse

### Part 0 ### Obtain the content of the website in a variable
url = 'https://google.ro'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

### Part 1 ### Print the content in the console
# print(soup.prettify())
# print("\n"*10)

### Part 2 ### Search and print the list of links
data = []
for link in soup.find_all("a"):
    data.append(link.get('href'))
for i in data:
    print(i)

### Part 3 ### Open and write the content from the website

f = open("test1.html", "w")
f.write(str(soup))
f.close()

### Part 4 ### Scrapp the content for each link and store it in file
# # # opening a file in append mode
f = open("test1.html", "a")
# # # traverse paragraphs from soup
for link in data:
        reply_server = request.urlopen(link)
        link_content = reply_server.read()
        f.write("\n"+str(link_content))
        f.write("\n")
f.close()
