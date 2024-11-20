import streamlit as st
import requests
import pyttsx3

# Cohere API configuration
API_KEY = "KGzncCCfHjKlNhAUwedCm7jWsq0i7Evz9hbijD3s"
API_URL = "https://api.cohere.ai/v1/summarize"

# Streamlit app
st.title("Text Summarization and Voice Generation using Cohere")

# Input field for user text
text_input = st.text_area("Enter text to summarize")

# Button to trigger summarization and voice generation
if st.button("Summarize and Speak"):
    if text_input:
        # Request headers for Cohere API
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        # API request body
        data = {
            "text": text_input,
            "summary_length": "short"
        }
        
        # Sending POST request to Cohere API
        response = requests.post(API_URL, json=data, headers=headers)
        
        if response.status_code == 200:
            # Get the summary text from the response
            summary = response.json().get("summary")
            st.write("Summary: ", summary)
            
            # Initialize text-to-speech engine
            engine = pyttsx3.init()
            engine.say(summary)  # Speak the summary
            engine.runAndWait()
        else:
            st.error("Error: Unable to summarize text.")
