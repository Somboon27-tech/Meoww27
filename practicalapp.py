import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Title
st.title("📊 View Finance Data from GitHub")

# Read CSV data from the provided URL
csv_url = (
    "https://raw.githubusercontent.com/"
    "Somboon27-tech/Meoww27/refs/heads/main/Finance_data.csv"
)
df = pd.read_csv(csv_url)

# Display DataFrame
st.subheader("Finance Data Table")
st.dataframe(df)

# Provide a download link for the data
st.download_button(
    label="Download this data as CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name="Finance_data.csv",
    mime="text/csv"
)

# Optional: show some basic statistics
st.subheader("Dataset Summary")
st.write(f"Number of rows: {df.shape[0]}")
st.write(f"Number of columns: {df.shape[1]}" )

# Load data
csv_url = "https://raw.githubusercontent.com/Somboon27-tech/Meoww27/refs/heads/main/Finance_data.csv"
finance_df = pd.read_csv(csv_url)

# List of numerical columns
numerical_cols = ['age', 'Mutual_Funds', 'Equity_Market', 'Debentures',
                  'Government_Bonds', 'Fixed_Deposits', 'PPF', 'Gold']

# Title
st.title("📈 Distribution of Financial Data")

# Loop through and plot each column
for col in numerical_cols:
    st.subheader(f"Distribution of {col}")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(data=finance_df, x=col, kde=True, ax=ax)
    st.pyplot(fig)


