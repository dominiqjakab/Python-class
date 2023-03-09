#!/usr/bin/python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(fromAdd, toAdd, subiect, mesaj):
    ### Part 0 ### Crearea email-ului in formatul MIME

    msg = MIMEMultipart()
    msg["From"] = fromADD
    msg["To"] = toADD
    msg["Subject"] = subiect
    print("Creating the message")

    ### Part 1 ### Crearea mesajului

    msg.attach(MIMEText(mesaj,'plain'))

    ### Part 2 ### Conectarea la server

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    # Logarea cu credentialele pentru aplicatie din contul de gmail
    server.login(fromADD, "token cont gmail")

    print("Connecting to server")

    ### Part 3 ###

    server.sendmail(fromADD,toADD,msg.as_string())

    print("Done sending")

fromADD = "testdj500@gmail.com"
toADD = "dominiq50@gmail.com"
subiect = "HeLLO FROM Python"
mesaj = "Te salut! Din programul meu scris in Python"

if True:
    sendMail(fromADD, toADD, subiect, mesaj)