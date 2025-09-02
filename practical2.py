import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIG ---
st.set_page_config(page_title="Mini Dashboard", page_icon="📊", layout="wide")

# --- TITLE ---
st.title("📈 Interactive Dashboard")
st.markdown("Welcome! This Streamlit app includes charts, user input, and file upload!")

# --- SESSION STATE ---
if "user_name" not in st.session_state:
    st.session_state["user_name"] = ""

# --- SIDEBAR ---
st.sidebar.title("🔧 Settings")
st.session_state["user_name"] = st.sidebar.text_input("Enter your name:", st.session_state["user_name"])
theme = st.sidebar.radio("Choose a theme:", ["Light", "Dark"])

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📄 Profile", "📊 Charts", "📁 File Upload"])

# --- TAB 1: Profile ---
with tab1:
    st.header("👤 Personal Information")
    age = st.slider("How old are you?", 10, 100, 25)
    gender = st.selectbox("Gender", ["Prefer not to say", "Male", "Female", "Other"])
    bio = st.text_area("Short bio:")

    st.subheader("📝 Summary")
    st.write(f"**Name:** {st.session_state['user_name']}")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Bio:** {bio}")

# --- TAB 2: Charts ---
with tab2:
    st.header("📊 Chart Example")
    chart_type = st.selectbox("Select chart type:", ["Line", "Bar", "Area"])

    # Sample data
    data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Sales": [150, 200, 180, 220, 300]
    })

    st.write("### Monthly Sales Data")
    st.dataframe(data)

    st.write("### Visualization")
    if chart_type == "Line":
        st.line_chart(data.set_index("Month"))
    elif chart_type == "Bar":
        st.bar_chart(data.set_index("Month"))
    elif chart_type == "Area":
        st.area_chart(data.set_index("Month"))

# --- TAB 3: File Upload ---
with tab3:
    st.header("📁 Upload CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.write("### Preview of Data")
        st.dataframe(df.head())

        st.write("### Basic Statistics")
        st.write(df.describe())

# --- FOOTER ---
st.markdown("---")
st.caption("🚀 Built with Streamlit | Customize this template as you like.")
