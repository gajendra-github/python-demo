# go to gmail and setup 2 factor authentication
# generate app password
# create a function to send email

#axbuzpmjzmwgdxjw

from email.message import EmailMessage
from config import password
import ssl
import smtplib


email_sender = 'gajen.demo@gmail.com'
email_password = password

email_receiver = 'dokewet494@cosaxu.com'

subject = 'Subject'

body = '''
    This is the body of email
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())













