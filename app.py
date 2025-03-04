import streamlit as st
import pandas as pd
import numpy as np
import datetime


# Define the log file
log_file = 'etl_log.txt'

def log_message(message):
    with open(log_file, 'a') as f:
        f.write(f'{datetime.datetime.now()} - {message}\n')

# Function to load data
@st.cache
def load_data():
    data = pd.read_csv('data_sales_file.csv')
    print(f'Data loaded at {datetime.datetime.now()}')
    return data
# Function to transform data
def transform_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Sales_to_Profit_Ratio'] = df['Sales'] / df['Profit']
    df['Cumulative_Sales'] = df['Sales'].cumsum()

    return df
# Function to extract summary statistics
def get_summary_statistics(df):
    summary = df.describe()
    return summary
# Main function to run the Streamlit app
def main():

    try:
        st.title("ETL Process for Sales Data")
        # Step 1: Extract
        st.header("Step 1: Extract")
        data = load_data()
        st.write("Raw Data")
        st.write(data)
        # Step 2: Transform
        st.header("Step 2: Transform")

        log_message(f'ETL job completed SUCCESS')
    
    except Exception as e:
        log_message(f'ETL job failed with error: {e}')