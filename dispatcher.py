import base64
from email.mime.text import MIMEText
from twilio.rest import Client
from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_WHATSAPP_NUMBER,
    ALERT_WHATSAPP_NUMBER
)

class ActionDispatcher:
    def __init__(self, gmail_service=None):
        self.gmail_service = gmail_service

    def send_gmail_reply(self, to_email: str, subject: str, reply_body: str):
        if not self.gmail_service:
            print(f"[Dry Run - Gmail Reply to {to_email}]:\nSubject: Re: {subject}\n{reply_body}\n")
            return

        message = MIMEText(reply_body)
        message['to'] = to_email
        message['subject'] = f"Re: {subject}"
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        self.gmail_service.users().messages().send(userId='me', body={'raw': raw}).execute()
        print(f"-> Sent email to {to_email}")

    def send_whatsapp_alert(self, sender: str, subject: str, body_preview: str):
        text = f"📨 *New Personal Email Received*\n*From:* {sender}\n*Subject:* {subject}\n\n*Content:* {body_preview}"
        if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
            print(f"[Dry Run - WhatsApp Alert]:\n{text}\n")
            return

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=ALERT_WHATSAPP_NUMBER,
            body=text
        )
        print("-> WhatsApp notification dispatched.")

    def handle_spam(self, email_id: str):
        print(f"-> Email {email_id} flagged as SPAM. No action taken.")
