import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("SmartCSV Analyzer")
uploaded_file = st.file_uploader("📁 Upload your CSV file", type="csv")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, on_bad_lines='skip')  # This fixes inconsistent row issue
        st.success("✅ File uploaded successfully!")

        # Preview data
        st.write("📄 Preview of your data:")
        st.dataframe(df.head())

        # Basic statistics
        st.write("📊 Basic Statistics:")
        st.write(df.describe())

        # Missing values
        st.write("❓ Missing Values in Each Column:")
        st.write(df.isnull().sum())

        # Column data types
        st.write("📌 Column Data Types:")
        st.write(df.dtypes)

        # Histogram for numeric columns
        st.write("📈 Histogram:")
        numeric_cols = df.select_dtypes(include='number').columns
        if not numeric_cols.empty:
            col = st.selectbox("Choose a numeric column", numeric_cols)
            fig, ax = plt.subplots()
            df[col].hist(ax=ax)
            st.pyplot(fig)
        else:
            st.info("ℹ️ No numeric columns found for histogram.")

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
