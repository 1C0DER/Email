import getpass
import smtplib
import datetime as dt
import time

def request_pass():
    try:
        password = getpass.getpass("Enter password: ")
    except Exception as e:
        print(f"Error error wee woo wee woo password error:{e}") 
    return password

def message_create(from_email, to_email, subject, body):
    try:
        message = f"Subject: {subject}\n\n{body}"
    except Exception as e:
        print(f"Error error wee woo wee woo message wont create:{e}") 
    return message

def send_email(from_email, to_email, password, subject, body, host="smtp.gmail.com", port=587):
    message = message_create(from_email, to_email, subject, body)
    
    try:
        smtp = smtplib.SMTP(host, port)

        status_code, response = smtp.ehlo()
        print(f"[*] Echoing the server: {status_code} {response}")

        status_code, response = smtp.starttls()
        print(f"[*] Starting TLS connection: {status_code} {response}")

        status_code, response = smtp.login(from_email, password)
        print(f"[*] Logging in {status_code} {response}")
        
        smtp.sendmail(from_email, to_email, message)
        smtp.quit()
        print('Email sent successfully: ') 
        
    except Exception as e:
        print(f"Error error wee woo wee woo the message wont send:{e}")  

def delay_email(from_email, to_email, password, subject, body):
    try:
        tnow = dt.datetime.now()      
        send_time = tnow + dt.timedelta(days=365)
        print(send_time.timestamp())
        time.sleep((send_time - tnow).total_seconds())
        send_email(from_email, to_email, password, subject, body)
    except Exception as e:
        print(f"Error error wee woo wee woo the delay wont go through:{e}") 

def send_reminder(from_email, to_email, password, delay_days=358):
    try:
        tnow = dt.datetime.now()
        send_time = tnow + dt.timedelta(days=358)
        reminder_subject = f"Reminder:"
        reminder_body = f"Heyyo Good day\nYou have yet to refresh your subsctiption.\nIf it has not been done by {delay_days}\nIt shall be taken away fron you:\n\n"   
        delay_seconds = (send_time - tnow).total_seconds() 
        if delay_seconds > 0:
            time.sleep(delay_seconds)
        send_email(from_email, to_email, password, reminder_subject, reminder_body)
    except Exception as e:
        print(f"Error error wee woo wee woo the 7-day delay aint working:{e}")  
    
if __name__ == '__main__':
    from_email = "d9006714@gmail.com"
    to_email = "nuttzack12@gmail.com"
    password = getpass.getpass("Enter password: ")
    subject = """Test drive"""
    body = """Heyyo Good day bish 
    
    You have finally completed this you can collapse now
    
    Testing testing 1,2,3"""
    delay_email(from_email, to_email, password, subject, body)   
    send_reminder(from_email, to_email, password, delay_days=358)