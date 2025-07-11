import os
import smtplib
import traceback
from email.mime.text import MIMEText
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from langchain_core.tools import tool
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()

email_client = os.getenv("EMAIL_ADDRESS")
email_pwd = os.getenv("EMAIL_APP_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

@tool
def send_email(recipient_name: str, subject: str, body: str, attachment_path: str = None):
    """
    This is Python function for Sending Email.
    Sends an email with an optional attachment.

    Args:
        recipient_name: The Email name of the Receiver
        subject: The subject of the Email
        body: The body of the Email
        attachment_path: Path to a file to attach (e.g., QR code image)
    
    Returns: None
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = email_client
        msg['To'] = recipient_name
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {os.path.basename(attachment_path)}",
                )
                msg.attach(part)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(email_client, email_pwd)
            server.sendmail(email_client, recipient_name, msg.as_string())
        return "Success"                

    except Exception as e:
        return f"Error in Sending the Email: {e}"

# Manual Testing
# send_email('siddharth.sulur@gmail.com', 'Hey', "Testing successful")