import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Analytics Portal", layout="wide")

st.title("📊 Data Analytics & Insights")
st.markdown("Upload your dataset (CSV or Excel) to get instant analysis.")

# File Uploader
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        # Load Data
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("File uploaded successfully!")

        # --- Data Preview Section ---
        st.subheader("1. Data Preview")
        st.dataframe(df.head())

        # --- Basic Stats Section ---
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("2. Dataset Info")
            st.write(f"Total Rows: {df.shape[0]}")
            st.write(f"Total Columns: {df.shape[1]}")
        
        with col2:
            st.subheader("3. Missing Values")
            st.write(df.isnull().sum())

        # --- Statistical Summary ---
        st.subheader("4. Statistical Summary")
        st.write(df.describe())

        # --- Basic Visualization Section ---
        st.subheader("5. Quick Visualizations")
        numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
        
        if numeric_columns:
            selected_col = st.selectbox("Select a column to visualize:", numeric_columns)
            
            fig, ax = plt.subplots(figsize=(10, 4))
            sns.histplot(df[selected_col], kde=True, ax=ax, color='skyblue')
            st.pyplot(fig)
        else:
            st.warning("No numeric columns found for visualization.")

    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Waiting for file upload...")