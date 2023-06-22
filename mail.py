import getpass
#getting password from user

import smtplib
#used to send email

HOST = "smtp.gmail.com"
#This is the smtp server domain name(for gmail in particular)

PORT = 587
#The port to connect to the smtp server

FROM_EMAIL = "d9006714@gmail.com"
#the email sending

TO_EMAIL = "nuttzack12@gmail.com"
#the email receiving

PASSWORD = getpass.getpass("Enter password: ")
#this is to ask for password

MESSAGE = """Subject: Test drive
Hey dumbass, 

YOYYO IT WORKS. YOU CAN STOP SUFFERING NOW

Your clueless past self,
Test Account"""
#the mail being sent (always make sure it is sent in this format)

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
#this is to check if the smtp server is running

print(f"[*] Echoing the server: {status_code} {response}")
#print the response

status_code, response = smtp.starttls()
#establishes a connection between the system and the tls server

print(f"[*] Starting TLS connection: {status_code} {response}")
#print the response

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
#used to login to the server

print(f"[*] Logging in {status_code} {response}")
#print the response

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
#used to send the mail after a succesful login

smtp.quit()
#To close the connection with the server 