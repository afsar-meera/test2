import streamlit as st

# Streamlit app
st.title('My Streamlit App')
user_input = st.text_input('Enter your name:')
st.write('Hello, ' + user_input + '! Welcome to Streamlit.')