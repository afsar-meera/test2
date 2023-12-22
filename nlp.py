!pip install streamlit transformers

import streamlit as st
from transformers import pipeline

# Load the Hugging Face model for sentiment analysis
sentiment_analyzer = pipeline("sentiment-analysis", model="bert-base-uncased")

st.title("Sentiment Analysis with Hugging Face + Streamlit")

# Create a text input for user input
user_input = st.text_area("Enter text for sentiment analysis:")

if st.button("Analyze Sentiment"):
    # Analyze sentiment using the Hugging Face model
    result = sentiment_analyzer(user_input)
    sentiment = result[0]['label']
    confidence = result[0]['score']

    st.write(f"Sentiment: {sentiment}")
    st.write(f"Confidence: {confidence}")
