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

def send_reminder_7days(from_email, to_email, password, day7subject, day7body):
    try:
        tnow = dt.datetime.now()
        send_time = tnow + dt.timedelta(minutes=1)
        #(delay_days)
        delay_seconds = (send_time - tnow).total_seconds() 
        if delay_seconds > 0:
            time.sleep(delay_seconds)
        send_email(from_email, to_email, password, day7subject, day7body)
    except Exception as e:
        print(f"Error error wee woo wee woo the 7-day delay aint working:{e}")
        
def send_reminder_3days(from_email, to_email, password, day3subject, day3body):
    try:
        tnow = dt.datetime.now()
        send_time = tnow + dt.timedelta(minutes=1)
        delay_seconds = (send_time - tnow).total_seconds() 
        if delay_seconds > 0:
            time.sleep(delay_seconds)
        send_email(from_email, to_email, password, day3subject, day3body)
    except Exception as e:
        print(f"Error error wee woo wee woo the 3-day delay aint working:{e}")
        
def send_reminder_Dday(from_email, to_email, password, subject, body):
    try:
        tnow = dt.datetime.now()      
        send_time = tnow + dt.timedelta(minutes=1)
        #(days=365)
        print(send_time.timestamp())
        time.sleep((send_time - tnow).total_seconds())
        send_email(from_email, to_email, password, subject, body)
    except Exception as e:
        print(f"Error error wee woo wee woo the d-day wont go through:{e}")   
        
def send_now(from_email, to_email, password, sendnowsubject, sendnowbody):
    try:
        send_email(from_email, to_email, password, sendnowsubject, sendnowbody)
    except Exception as e:
        print(f"Error error wee woo wee woo the first message wont send:{e}")
    
if __name__ == '__main__':
    from_email = "d9006714@gmail.com"
    to_email = "nuttzack12@gmail.com"
    password = getpass.getpass("Enter password: ")
    sendnowbody = "Heyyo Good day customer\nYou have sucessfully subcribed to ..... thank you for choosing us\n\n" 
    sendnowsubject = """Congratulations"""
    day7subject = """Reminder"""
    day7body = "Heyyo Good day\nYou have yet to refresh your subsctiption.\nYou have within the next 7 days to re-subscribe\nOr else it shall be taken away fron you:\n\n" 
    day3subject = """Reminder"""
    day3body = "Heyyo Good day\nYou have yet to refresh your subsctiption.\nYou have within the next 3 days to re-subscribe\nOr elseIt shall be taken away fron you:\n\n" 
    subject = """Reminder"""
    body = "Heyyo Good day\nYou have yet to refresh your subsctiption.\nIf it has not been done by the end of today\nIt shall be taken away fron you:\n\n" 
    send_now(from_email, to_email, password, sendnowsubject, sendnowbody) 
    send_reminder_7days(from_email, to_email, password, day7subject, day7body)
    send_reminder_3days(from_email, to_email, password, day3subject, day3body)
    send_reminder_Dday(from_email, to_email, password, subject, body) 