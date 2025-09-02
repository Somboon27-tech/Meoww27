import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Simple Dashboard", page_icon="📊", layout="centered")

# --- TITLE & DESCRIPTION ---
st.title("📊 Welcome to My Streamlit App!")
st.markdown("This app collects your info and displays a personalized message.")

# --- IMAGE (OPTIONAL) ---
st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=200)

# --- USER INPUTS ---
name = st.text_input("What's your name?")
age = st.slider("How old are you?", 0, 100, 25)
hobby = st.selectbox("Choose a hobby", ["Reading", "Gaming", "Cooking", "Sports", "Traveling", "Others"])

# --- CONDITIONAL RESPONSE ---
if name:
    st.subheader("👤 Your Profile")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Hobby:** {hobby}")
    
    # Personalized message
    st.success(f"Nice to meet you, {name}! Enjoy your time with {hobby.lower()}! 🎉")

# --- FOOTER ---
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
