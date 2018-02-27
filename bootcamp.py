# imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_server():
    username = 'bootcamp_manipal@outlook.com'
    password = input('Enter password: ')

    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(username, password)
    
    return s

def send_email(to, body, server):
    username = 'bootcamp_manipal@outlook.com'
        

    message = MIMEMultipart()
    message['From'] = username
    message['To'] = to
    message['Subject'] = "TEST"
    message.attach(MIMEText(body, 'plain'))
    text = message.as_string()
    
    server.sendmail(username, to, text)

def close_server(server):
    server.close()


def read_file(path):
    #TODO
    pass