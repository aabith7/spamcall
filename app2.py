
import streamlit as st
import os
import tempfile
from pydub import AudioSegment
import speech_recognition as sr
import smtplib
from email.message import EmailMessage
from datetime import datetime
import pickle

# ========== Load the Trained Model ==========
with open("spam_call_classifier.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

# ========== Text Classification ==========
def classify_text(text):
    try:
        # Vectorize and predict
        text_vector = vectorizer.transform([text.lower()])
        prediction = model.predict(text_vector)[0]
        return prediction
    except Exception as e:
        return f"Error: {e}"

# ========== Transcribe Audio ==========
def transcribe_audio(wav_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)

# ========== Send Email ==========
def send_email(receiver_email, audio_path, transcribed_text, timestamp):
    try:
        msg = EmailMessage()
        msg['Subject'] = f'Cyber Crime Complaint:🚨Spam Call Detected on {timestamp}'
        msg['From'] = 'your_email@gmail.com'
        msg['To'] = receiver_email

        msg.set_content(f"""Respected Sir/Madam,

I am writing to report a suspicious spam call that was received and automatically flagged using an AI-based detection system I have developed.

The system transcribes incoming audio and classifies it as either spam or ham. On {timestamp}, the following message was received and identified as 'SPAM':

📄 Transcribed Message:
"{transcribed_text}"

📁 Attached Evidence:
- Audio File: {os.path.basename(audio_path)}

Kindly investigate this as per the IT Act and applicable cybercrime laws. I am available to provide any further assistance required.

Thank you for your attention.

Sincerely,  
Aabith M  
📧 aabith1853@gmail.com  
📞 9443683982  
📍 Salem, Tamil Nadu""")

        with open(audio_path, 'rb') as f:
            audio_data = f.read()
            msg.add_attachment(audio_data, maintype='audio', subtype='wav', filename=os.path.basename(audio_path))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('aabith1853@gmail.com', 'nvzviagfsqlsqaux')  # Use App Password here
            smtp.send_message(msg)

        return True
    except Exception as e:
        return str(e)

# ========== Streamlit UI ==========
st.title("📞 Spam Call Detection & Reporting System")

uploaded_file = st.file_uploader("Upload an MP3 File", type=["mp3"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_mp3:
        tmp_mp3.write(uploaded_file.read())
        mp3_path = tmp_mp3.name

    wav_path = mp3_path.replace(".mp3", ".wav")
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")
    st.success("✅ Audio converted to WAV format")

    try:
        transcribed_text = transcribe_audio(wav_path)
        st.text_area("📄 Transcribed Text", transcribed_text, height=150)

        classification = classify_text(transcribed_text)
        st.write("🔍 Classification Result:", classification.upper())

        if classification == "spam":
            timestamp = datetime.now().strftime("%d-%m-%Y %I:%M %p")
            if st.button("📤 Send Email to Cyber Police"):
                result = send_email("aabith1853@gmail.com", wav_path, transcribed_text, timestamp)
                if result == True:
                    st.success("📨 Email sent successfully!")
                else:
                    st.error(f"❌ Failed to send email: {result}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
