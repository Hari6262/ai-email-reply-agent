# 🤖 Autonomous AI Email Routing & Auto-Reply Agent

An intelligent email automation workflow built using **Relay.app** and **LLMs**. The system listens for incoming Gmail messages, classifies sender intent, and executes custom automated actions across email and WhatsApp.

---

## 📌 Routing Logic

| Intent Category | Processing Action | Output Channel |
| :--- | :--- | :--- |
| **Professional** | Context-aware professional response generation | Automated Gmail Reply |
| **Personal** | Extracts message details and alerts instantly | WhatsApp Notification |
| **Leave Request** | Directs sender to class representative / department | Standard Auto-Reply |
| **Spam** | Flags and skips processing | Tagged as Spam |

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
