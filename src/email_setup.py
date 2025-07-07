import os
import smtplib
import traceback
from email.mime.text import MIMEText
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from langchain_core.tools import tool

load_dotenv()

email_client = os.getenv("EMAIL_ADDRESS")
email_pwd = os.getenv("EMAIL_APP_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

@tool
def send_email(recipient_name: str, subject: str, body: str) -> str:
    """
    This is Python function for Sending Email.

    Args:
        recipient_name: The Email name of the Receiver
        subject: The subject of the Email
        body: The body of the Email
    
    Returns: None
    """
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
        return "Success"                

    except Exception as e:
        return f"Error in Sending the Email: {e}"

# Manual Testing
# send_email('siddharth.sulur@gmail.com', 'Hey', "Testing successful")