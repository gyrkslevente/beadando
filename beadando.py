import streamlit as st
import yfinance as yf
import pandas as pd

st.header("Simple Stock Price")

ticker = 'GOOGL'
start_date = '2010-1-1'
end_date = '2020-12-31'

data = yf.download(ticker, start_date, end_date)

line_data = pd.DataFrame(data)

st.write(ticker)

st.line_chart(line_data.Close)
st.line_chart(line_data.Volume)