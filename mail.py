"""
import getpass
#getting password from user

import smtplib
#used to send email

import datetime as dt

import time

HOST = "smtp.gmail.com"
#This is the smtp server domain name(for gmail in particular)

PORT = 587
#The port to connect to the smtp server

FROM_EMAIL = "d9006714@gmail.com"
#the email sending

TO_EMAIL = "ejiro006@gmail.com"
#the email receiving

PASSWORD = getpass.getpass("Enter password: ")
#this is to ask for password
"""

"""
MESSAGE = Subject: Test drive
Heyyo Good morning Sir 

I hope you have finished filling the school documents

Your village people,
Testing testing 1,2,3
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

send_time = dt.datetime(2023, 6, 26, 9, 00, 0)
#Okay so yeah this is in the format of Year-Month-Date-Hour-Minuite-Second

print(send_time.timestamp())
#getting the time in teh time stanp format

print(time.time())
#print current time 

x = time.sleep(send_time.timestamp() - time.time())
print(x)

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
#used to send the mail after a succesful login

smtp.quit()
#To close the connection with the server 

print('Email sent successfully :)')
"""




import getpass
import smtplib
import datetime as dt
import time

def get_password():
    return getpass.getpass("Enter password: ")

def send_email():
    HOST = "smtp.gmail.com"
    PORT = 587
    FROM_EMAIL = "d9006714@gmail.com"
    TO_EMAIL = "ejiro006@gmail.com"
    PASSWORD = get_password()
    MESSAGE = """Subject: Test drive
    Heyyo Good morning Sir 

    I hope you have finished filling the school documents

    Your village people,
    Testing testing 1,2,3"""

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in {status_code} {response}")

    send_time = dt.datetime(2023, 6, 26, 9, 0, 0)
    print(send_time.timestamp())

    print(time.time())
    x = time.sleep(send_time.timestamp() - time.time())
    print(x)

    smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    smtp.quit()

    print('Email sent successfully :)')

send_email()


