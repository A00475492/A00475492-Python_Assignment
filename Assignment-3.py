import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('CSV File Upload and Age Histogram')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    if 'Name' in data.columns and 'Age' in data.columns:
        plt.hist(data['Age'], bins=10, edgecolor='black')
        plt.xlabel('Ages')
        plt.ylabel('Frequency')
        plt.title('Histogram of Ages')
        st.pyplot(plt)
    else:
        st.error('The uploaded file does not have the required columns.')