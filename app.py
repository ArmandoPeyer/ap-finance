import streamlit as st
import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt

# Fetch data from Yahoo Finance 
start_date = "2018-04-28"
end_date = "2023-04-28"

st.markdown("# AP Finance")

st.markdown("## Welcome. Please explore this beautiful app.")

stock = st.radio(
    "What stock would you like to explore?",
    ('TSLA', 'MSFT', 'AMZN'))

if stock == "TSLA":
    ticker = "TSLA"
    data = yf.download(ticker, start=start_date, end=end_date)
    st.line_chart(data['Adj Close'])
elif stock == "MSFT":
    ticker = "MSFT"
    data = yf.download(ticker, start=start_date, end=end_date)
    st.line_chart(data['Adj Close'])
else:
    ticker = "AMZN"
    data = yf.download(ticker, start=start_date, end=end_date)
    st.line_chart(data['Adj Close'])

# st.table(data)