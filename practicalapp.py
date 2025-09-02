# save this as app.py

import streamlit as st

st.title("👋 Hello Streamlit!")
st.write("This is a simple Streamlit web app.")

# Text input
name = st.text_input("What's your name?")

# Button
if st.button("Say Hello"):
    st.success(f"Hello, {name}!")
