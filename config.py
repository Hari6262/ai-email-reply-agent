import os
from dotenv import load_dotenv

load_dotenv()

# App Credentials
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GMAIL_TOKEN_PATH = os.getenv("GMAIL_TOKEN_PATH", "token.json")
GMAIL_CREDENTIALS_PATH = os.getenv("GMAIL_CREDENTIALS_PATH", "credentials.json")

# Notification Config (Twilio for WhatsApp)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER", "whatsapp:+14155238886")
ALERT_WHATSAPP_NUMBER = os.getenv("ALERT_WHATSAPP_NUMBER", "")

# Fallback Auto-Reply Templates
LEAVE_REQUEST_REPLY = (
    "Hello,\n\n"
    "Thank you for contacting regarding leave. Please reach out to the class "
    "representative or contact me directly via phone/WhatsApp for urgent approvals.\n\n"
    "Best regards,\nHari"
)
