
# EchoMind: AI-Powered Audio Summarizer

### Overview
**EchoMind** is an AI-powered tool that efficiently generates concise summaries from audio files, transforming spoken content into brief, readable insights. Utilizing Google’s advanced generative AI technology, this application supports various audio formats such as WAV and MP3, providing a seamless and user-friendly experience for summarizing lengthy audio content.

### Features
- **AI-Powered Summarization**: Converts lengthy audio files into concise, easily digestible summaries.
- **Support for Multiple Formats**: Works with popular audio formats like WAV and MP3.
- **Intuitive Interface**: Simple, elegant UI designed for ease of use.
- **Custom Summarization**: Generates summaries that capture the key points of the audio content.

### Demo
Upload an audio file (WAV or MP3), click "Summarize Audio," and EchoMind will produce a short summary in seconds.

### Technology Stack
- **Front-End**: Streamlit for a sleek, interactive UI.
- **Back-End**: Google Generative AI for summarization.
- **Audio Processing**: Pydub for handling audio formats.
- **Cloud Environment**: Google API for AI integration.

### Requirements
To run this project locally, you will need the following:
- Python 3.7+
- Required Python libraries listed in `requirements.txt`
- Google API Key (sign up for an API key from Google Cloud)

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/atharv2001j/EchoMind.git
    cd EchoMind
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your `.env` file with your Google API key:
    ```
    GOOGLE_API_KEY=your_google_api_key
    ```

### How to Run
1. Launch the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Open the provided local URL (http://localhost:8501) in your browser.

3. Upload an audio file, and click "Summarize Audio" to generate the summary.

### Project Structure
```plaintext
📁 EchoMind/
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables for API keys
└── README.md             # Project documentation
```

### Future Improvements
- Add support for more audio formats (e.g., FLAC, AAC).
- Implement advanced options like summary length control.
- Add dark mode and other user interface customization.

### Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements.

### Contact
For any inquiries, please reach out at joshiatharv67@gmail.com.
