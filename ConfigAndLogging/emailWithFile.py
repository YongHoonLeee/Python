# from email import message
from email.mime import multipart
from email.mime import text
import smtplib


smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'myfirstemail@pukyong.ac.kr'
to_email = 'myfirstemail@pukyong.ac.kr'
username = 'myfirstemail@pukyong.ac.kr'
password = 'ismyfirstemailyes'

msg = multipart.MIMEMultipart()
msg.attach(text.MIMEText('Test email', 'plain'))
with open('ConfigAndLogging/emailWithFile.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='ConfigAndLogging/emailWithFile.py'
    )
    msg.attach(attachment)

msg['Subject'] = 'hello'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
# tls start
server.starttls()
server.ehlo()
server.login(username, password)
# server.send_message(msg)
server.sendmail(from_email, to_email, msg.as_string())
server.quit()
