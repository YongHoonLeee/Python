# from email import message
from email.mime.text import MIMEText
import smtplib


smtp_host = 'smtp.gmail.com'
smtp_port = 465
from_email = 'utf-8 decode error fuck@pukyong.ac.kr'
to_email = 'utf-8 decode error fuck@pukyong.ac.kr'
username = 'utf-8 decode error fuck@pukyong.ac.kr'
password = 'utf-8 decode error fuck'

# msg = message.EmailMessage()
# msg.set_content('This is my first E-mail by Python ;)')
msg = MIMEText('This is my first Python-mail. ;)')
msg['Subject'] = 'hello'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP_SSL(smtp_host, smtp_port)
server.ehlo()
# tls start
# server.starttls()
# server.ehlo()
server.login(username, password)
# server.send_message(msg)
server.sendmail(from_email, to_email, msg.as_string())
server.quit()
