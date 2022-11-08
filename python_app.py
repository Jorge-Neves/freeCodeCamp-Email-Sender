# Process
# Setup 2-factor authentication on the email that will be sending the emails
# Create the function that will send the emails

from email.message import EmailMessage
from credentials import password
import ssl
import smtplib

email_sender = "paulo.dev.acc@gmail.com"
email_receiver = "paulo.jorge.ngs@gmail.com"
email_password = password

subject = "Python Email Sender App -Email"
body = "An email generated from a python app"

email = EmailMessage()
email["From"] = email_sender
email["TO"] = email_receiver
email["subject"] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, email.as_string())
