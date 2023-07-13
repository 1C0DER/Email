import getpass
import smtplib
import datetime as dt
import time

def send_email():
    host = "smtp.gmail.com"
    port = 587
    from_email = "d9006714@gmail.com"
    to_email = "nuttzack12@gmail.com"
    password = getpass.getpass("Enter password: ")
    message = """Subject: Test drive
    Heyyo Good morning Sir 

    I hope you have finished filling the school documents

    Your village people,
    Testing testing 1,2,3"""

    smtp = smtplib.SMTP(host, port)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")


    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(from_email, password)
    print(f"[*] Logging in {status_code} {response}")
    
    tnow = dt.datetime.now()
    
    send_time = tnow.replace(year=tnow.year+1)

    print(send_time.timestamp())

    print(time.time())

    time.sleep(send_time - tnow)

    smtp.sendmail(from_email, to_email, message)

    smtp.quit()

    print('Email sent successfully: ')

send_email()