import os
import smtplib
import traceback
from email.mime.text import MIMEText
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart

load_dotenv()

email_client = os.getenv("EMAIL_ADDRESS")
email_pwd = os.getenv("EMAIL_APP_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send(recipient_name, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = email_client
        msg['To'] = recipient_name
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(email_client, email_pwd)
            server.sendmail(email_client, recipient_name, msg.as_string())
        print("Success")                

    except Exception as e:
        traceback.print_exc()

# Manual Testing
# send('arav302005@gmail.com', 'Hey', "Testing successful")