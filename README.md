# 🤖 Autonomous AI Email Routing & Auto-Reply Agent

An intelligent, multi-branch email automation system built with **Python**, **Gemini LLM**, and **Relay.app** workflow architecture. The system monitors incoming emails, leverages LLM reasoning to classify intent, and routes each message along dedicated action pipelines (automated professional drafting, personal WhatsApp notifications, leave request redirects, or spam filtration).

---

## 📌 Routing Logic

| Intent Category | Processing Action | Output Channel |
| :--- | :--- | :--- |
| **Professional** | Context-aware professional response generation | Automated Gmail Reply |
| **Personal** | Extracts message details and alerts instantly | WhatsApp Notification (Twilio) |
| **Leave Request** | Directs sender to class representative / department | Standard Auto-Reply |
| **Spam** | Flags and skips processing | Tagged & Discarded |

---

## 🛠️ Architecture Workflow

```text
Incoming Email (Gmail Trigger)
          │
          ▼
   [ AI Intent Classifier ]
          │
  ┌───────┼───────────────────┬───────────────┐
  ▼       ▼                   ▼               ▼
[Professional]           [Personal]    [Leave Request]     [Spam]
  │                           │               │               │
  ▼                           ▼               ▼               ▼
Generate & Send Reply    Send WhatsApp   Redirect Reply   Tag & Ignore
```

---

## 📂 Project Structure

```text
ai-email-reply-agent/
├── classifier.py      # LLM reasoning engine for intent classification & drafting
├── dispatcher.py      # Multi-channel routing (Gmail & Twilio WhatsApp)
├── test_pipeline.py   # Dry-run test suite simulating incoming emails
├── config.py          # Environment & API configurations
├── requirements.txt   # Python dependencies
├── .env.example       # Sample environment template
└── README.md          # Project documentation
```

---

## 📸 Demo & Verification

<!-- DROP YOUR IMAGES RIGHT HERE (SEE PART 2 BELOW) -->

---

## 🚀 Quickstart & Simulation

Run the local test simulation without requiring live Gmail credentials:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Hari6262/ai-email-reply-agent.git](https://github.com/Hari6262/ai-email-reply-agent.git)
   cd ai-email-reply-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment (Optional):**
   ```bash
   cp .env.example .env
   # Add your GEMINI_API_KEY in .env
   ```

4. **Run the simulation:**
   ```bash
   python test_pipeline.py
   ```

---

## 📜 Acknowledgements
* Built following AI workflow automation principles from the *Foundations of Agentic AI + AI Workflows Masterclass*.
