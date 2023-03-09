#!/usr/bin/python3

### Algorithm used to send emails using SMTP server ###
### apt-get mime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(fromAdd, toAdd, subject, message):
    ### Part 0 ### Creating the email in MIME format

    msg = MIMEMultipart()
    msg["From"] = fromADD
    msg["To"] = toADD
    msg["Subject"] = subject
    print("Creating the message")

    ### Part 1 ### Creating the message

    msg.attach(MIMEText(message,'plain'))

    ### Part 2 ### Connecting to the server

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    # Login with the credentials used for the gmail account
    server.login(fromADD, "token app from the google account ")

    print("Connecting to server")

    ### Part 3 ### Sending the email

    server.sendmail(fromADD,toADD,msg.as_string())

    print("Done sending")

fromADD = "testdj500@gmail.com"
toADD = "dominiq50@gmail.com"
subject = "HeLLO FROM Python"
message = "Hello! From my algorithm written in Python"

if True:
    sendMail(fromADD, toADD, subject, message)