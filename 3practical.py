import streamlit as st

# Title of the app
st.title("🚀 My First Streamlit App")

# Simple description
st.write("Welcome! This is my very first Streamlit web app.")

# Ask for the user's name
name = st.text_input("What's your name?")

# Ask how the user is feeling
feeling = st.selectbox("How are you feeling today?", ["Happy 😊", "Tired 😴", "Excited 🤩", "Sad 😢", "Just okay 😐"])

# Button to show greeting
if st.button("Say Hello"):
    if name:
        st.success(f"Hi {name}! Glad to hear you're feeling {feeling.lower()}!")
    else:
        st.warning("Please enter your name above.")

# Footer
st.markdown("---")
st.caption("👩‍💻 Created with Streamlit")
