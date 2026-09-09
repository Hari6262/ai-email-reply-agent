import google.generativeai as genai
from config import GEMINI_API_KEY

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

class EmailClassifier:
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.model = genai.GenerativeModel(model_name)

    def classify(self, sender: str, subject: str, body: str) -> str:
        """Classifies email into PROFESSIONAL, PERSONAL, LEAVE_REQUEST, or SPAM."""
        prompt = f"""
You are an intelligent email triage agent.
Analyze the following email metadata and content:

Sender: {sender}
Subject: {subject}
Content: {body}

Categorize this email into exactly one of these labels:
- PROFESSIONAL
- PERSONAL
- LEAVE_REQUEST
- SPAM

Respond with ONLY the uppercase label.
"""
        try:
            response = self.model.generate_content(prompt)
            result = response.text.strip().upper()
            valid_labels = ["PROFESSIONAL", "PERSONAL", "LEAVE_REQUEST", "SPAM"]
            for label in valid_labels:
                if label in result:
                    return label
            return "PROFESSIONAL"
        except Exception as e:
            print(f"[Error in classification]: {e}")
            return "PROFESSIONAL"

    def draft_professional_reply(self, sender: str, subject: str, body: str) -> str:
        """Drafts a concise, professional reply acknowledging the sender."""
        prompt = f"""
You are an executive assistant drafting an email reply on behalf of Hari (Student, Computer Science).
Sender: {sender}
Subject: {subject}
Body: {body}

Draft a polite, context-aware, professional response. Keep it concise.
Return ONLY the email body text.
"""
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Thank you for your email. I have received your message regarding '{subject}' and will get back to you shortly."
