import streamlit as st
from pydub import AudioSegment
import tempfile
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google API for audio summarization
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def summarize_audio(audio_file_path):
    """Summarize the audio using Google's Generative API."""
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    audio_file = genai.upload_file(path=audio_file_path)
    response = model.generate_content(
        [
            "Please summarize the following audio.",
            audio_file
        ]
    )
    return response.text

def save_uploaded_file(uploaded_file):
    """Save uploaded file to a temporary file and return the path."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        st.error(f"Error handling uploaded file: {e}")
        return None

# Custom CSS to enhance the interface
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 40px;
        color: #4CAF50;
        margin-bottom: 10px;
    }
    .description {
        text-align: center;
        font-size: 18px;
        color: #777;
        margin-bottom: 30px;
    }
    .audio-uploader {
        display: flex;
        justify-content: center;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-size: 18px;
        padding: 8px 15px;
        margin-top: 20px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .summary-box {
        background-color: #f5f5f5;
        border-radius: 10px;
        padding: 15px;
        margin-top: 20px;
        font-family: 'Courier New', Courier, monospace;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        padding: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app interface
st.markdown('<h1 class="title">Audio Summarization App</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">Upload your audio file and get a concise summary using Google\'s Generative AI.</p>', unsafe_allow_html=True)

# Upload audio file section
audio_file = st.file_uploader("Upload Audio File", type=['wav', 'mp3'])
if audio_file is not None:
    audio_path = save_uploaded_file(audio_file)  # Save the uploaded file and get the path
    st.audio(audio_path, format="audio/wav" if audio_file.type == "audio/wav" else "audio/mp3")

    # Button to summarize the audio
    if st.button('Summarize Audio'):
        with st.spinner('Summarizing...'):
            summary_text = summarize_audio(audio_path)
            st.markdown(f'<div class="summary-box"><strong>Summary:</strong><br>{summary_text}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Audio Summarization App | Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)

