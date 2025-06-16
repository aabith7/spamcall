# 📞 Spam Call Detection & Cyber Reporting System

A real-time project that listens to phone calls, transcribes them, classifies whether it's spam or not using a **Naive Bayes** machine learning model, and sends an **automated report** to cyber police if spam is detected.

---

## 🧠 Features

- 🎧 Record incoming call audio
- 🗣️ Transcribe using speech recognition
- 🤖 Classify spam using Naive Bayes (trained on real/synthetic transcripts)
- 📩 Send alert email to cybercrime authorities
- 🌐 Streamlit Web UI for interaction

---

## 🚀 How It Works

1. User records a phone call through the app
2. Audio is converted to text using `speech_recognition`
3. The transcript is processed and passed into a **Naive Bayes** model
4. If flagged as spam, the system sends an **automated cyber report email**
5. User sees result and email status on the Streamlit interface

---

## 🛠️ Tech Stack

| Purpose              | Technology Used                        |
|----------------------|----------------------------------------|
| ML Model             | Naive Bayes (Scikit-learn)             |
| Audio Recording      | `pyaudio`, `wave`                      |
| Speech Recognition   | Google Speech API                      |
| Frontend Interface   | Streamlit                              |
| Email Reporting      | `smtplib`, `email.message`             |
| Programming Language | Python                                 |

---
Spam Detected:
Transcript: "You have won a free iPhone..."
Predicted: SPAM

Cyber Report Email Sent to: cyberpolice@support.in
Status: ✅ Delivered

📁 Project Structure

spam-call-detection/
├── app.py                # Streamlit app main logic
├── model/
│   └── naive_bayes.pkl   # Trained ML model
├── audio/
│   └── sample_call.wav   # Example call recording
├── utils/
│   └── processing.py     # Transcription & preprocessing
├── send_report.py        # Email logic
├── requirements.txt
└── README.md

📜 Naive Bayes Classifier
Input: Preprocessed text transcript of a call

Features: Bag of Words or TF-IDF vectors

Labels: Spam / Not Spam

Libraries: CountVectorizer, MultinomialNB, sklearn

📬 Auto Cyber Report Sample
Subject: 🚨 SPAM Call Alert from Aabith's Detection System

This is to inform you that a spam call was detected on:
Date: 16 June 2025
Time: 8:00 PM

Transcript:
"Your bank account is blocked. Share your OTP now!"

Caller: Unknown
Classification: SPAM

Please take necessary action. Report generated automatically.

📷 Screenshot

![Screenshot 2025-06-16 213928](https://github.com/user-attachments/assets/073d0d0a-3590-4b87-9297-6b748e95199c)


📌 Future Plans
NLP-powered classification (e.g., BERT, RoBERTa)

Webhook/OTP verification before auto-report

Dashboard to view call history and status

Multi-language support (Tamil, Hindi, etc.)



🙋‍♂️ Author
Aabith Navab
📍 Bengaluru
🎓 Data Science Intern @ GradTwin
🔗 [LinkedIn](https://www.linkedin.com/in/aabith-n-9b2434269/)
💻 [GitHub](https://github.com/aabith7)



