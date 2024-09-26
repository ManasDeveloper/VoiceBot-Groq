import speech_recognition as sr
from gtts import gTTS
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from llm import get_response

load_dotenv()

os.environ["GROQ_API_KEY"] = "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"
groq_api_key = "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"

print(groq_api_key)

llm = ChatGroq(model = "gemma2-9b-it")

# Initialize recognizer
r = sr.Recognizer()

# Function to capture speech and convert it to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        st.write("Listening...")
        
        # Listen to the user's input
        audio = r.listen(source)
        
        try:
            # Recognize speech using Google Web Speech API
            text = r.recognize_google(audio)
            print("You said: " + text)
            st.write("You said : " + text)
            return text
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred while recognizing speech")

# Convert the recognized text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")  # For Windows, use 'afplay output.mp3' for macOS

# Main function to handle speech to text and text to speech
def main():
    pass
    
        
st.title("GROQ Voice Bot")
st.write("Click the button below to start speaking...")

if st.button("Start"):
    recognized_text = speech_to_text()

    # send the recognized text to llm
    response = get_response(recognized_text,groq_api_key)
    # retreive the output
    output = response.content
    if recognized_text:
        st.write(output)
        text_to_speech(output)
