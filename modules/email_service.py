import smtplib
from email.message import EmailMessage
import os

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_summary_via_email(summary_text, recipient_email):
    """Send summarized text via email."""
    msg = EmailMessage()
    msg.set_content(summary_text)
    msg['Subject'] = "Your Summarized Content"
    msg['From'] = EMAIL_SENDER
    msg['To'] = recipient_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
