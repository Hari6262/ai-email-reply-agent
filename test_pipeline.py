from classifier import EmailClassifier
from dispatcher import ActionDispatcher
from config import LEAVE_REQUEST_REPLY

sample_emails = [
    {
        "id": "msg_001",
        "from": "professor_noble@college.edu",
        "subject": "Re: S5 results are out",
        "body": "Dear Hari, the semester 5 exam results are officially declared on the KTU portal. Please review."
    },
    {
        "id": "msg_002",
        "from": "allu@gmail.com",
        "subject": "Birthday dinner this week!",
        "body": "Hi Hari, we are celebrating at Mandi Manzil Ullor at 8 PM on Sunday. Let me know if you can make it!"
    },
    {
        "id": "msg_003",
        "from": "student@college.edu",
        "subject": "Request for Duty Leave Approval",
        "body": "Hi, I was absent for the DBMS lab and need permission for attendance shortage consideration."
    },
    {
        "id": "msg_004",
        "from": "deals@promotions-market.com",
        "subject": "Claim your $500 gift card now",
        "body": "Click here to claim a lottery reward immediately."
    }
]

def run_simulation():
    print("=== Starting Autonomous Email Triage Simulation ===")
    classifier = EmailClassifier()
    dispatcher = ActionDispatcher(gmail_service=None)

    for mail in sample_emails:
        print(f"\n[Processing Mail]: {mail['subject']} from {mail['from']}")
        intent = classifier.classify(mail['from'], mail['subject'], mail['body'])
        print(f"-> Identified Intent: {intent}")

        if intent == "PROFESSIONAL":
            reply = classifier.draft_professional_reply(mail['from'], mail['subject'], mail['body'])
            dispatcher.send_gmail_reply(mail['from'], mail['subject'], reply)
        elif intent == "PERSONAL":
            dispatcher.send_whatsapp_alert(mail['from'], mail['subject'], mail['body'])
        elif intent == "LEAVE_REQUEST":
            dispatcher.send_gmail_reply(mail['from'], mail['subject'], LEAVE_REQUEST_REPLY)
        elif intent == "SPAM":
            dispatcher.handle_spam(mail['id'])

if __name__ == "__main__":
    run_simulation()
