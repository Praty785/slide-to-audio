import streamlit as st
from PIL import Image
import pytesseract
from gtts import gTTS
import os

st.set_page_config(page_title="Lecture to Audio", layout="wide")
st.title("Lecture Slide to Audio Converter")
st.write("Upload slides - AI reads text - Download audio")

uploaded_files = st.file_uploader("Upload slides", type=["png","jpg","jpeg"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.subheader(uploaded_file.name)
        col1, col2 = st.columns(2)
        
        with col1:
            image = Image.open(uploaded_file)
            st.image(image)
        
        with col2:
            with st.spinner("Reading text"):
                text = pytesseract.image_to_string(image)
            
            if not text.strip():
                text = "No text found"
            
            st.text_area("Text", text, height=120, disabled=True)
            
            if st.button(f"Convert - {uploaded_file.name}"):
                tts = gTTS(text=text, lang='en')
                audio_file = "temp.mp3"
                tts.save(audio_file)
                
                with open(audio_file, 'rb') as f:
                    audio_data = f.read()
                
                st.audio(audio_data, format="audio/mp3")
                st.download_button("Download MP3", audio_data, file_name=f"{uploaded_file.name}.mp3")
                os.remove(audio_file)
```

