import streamlit as st
from transformers import pipeline

def main():
    st.title("Text Summarizer App")

    # User input for text
    user_input = st.text_area("Enter text to summarize:")

    if st.button("Summarize"):
        if not user_input:
            st.warning("Please enter some text for summarization.")
        else:
            # Summarize using Hugging Face's pipeline
            summarizer = pipeline("summarization")
            summary = summarizer(user_input, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

            # Display the original text and the summary
            st.subheader("Original Text:")
            st.write(user_input)

            st.subheader("Summary:")
            st.write(summary[0]['summary_text'])

if __name__ == "__main__":
    main()
