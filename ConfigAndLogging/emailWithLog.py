# from email import message
import logging
import logging.handlers
import smtplib


smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = 'myfirstemail@pukyong.ac.kr'
to_email = 'myfirstemail@pukyong.ac.kr'
username = 'myfirstemail@pukyong.ac.kr'
password = 'ismyfirstemailyes'

logger = logging.getLogger('eamil')
logger.setLevel(logging.CRITICAL)
logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject='Admin test log',
    credentials=(username, password),
    secure=(None, None, None),
    timeout=20
))
logger.info('test')
logger.critical('wow critical log')

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
# tls start
server.starttls()
server.ehlo()
server.login(username, password)
# server.send_message(msg)
server.quit()
