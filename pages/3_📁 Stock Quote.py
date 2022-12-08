import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

st.set_page_config(
    page_title="Stock Quote",
    layout = "wide"    
)

hide_menu = """
    <style>
        #MainMenu {Visibility: Hidden}
        footer {Visibility: Hidden}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.info('#### Stock Price and Volume Charts')

ticker_sym = st.text_input('Enter a stock ticker:', max_chars=5)
search = st.button('Search', key={ticker_sym})
ticker_Data = yf.Ticker(ticker_sym)

info = yf.Ticker(ticker_sym).info
if info:
    if 'shortName' in info:
        Stock_Name = info['shortName']
        Stock_Price = info['regularMarketPrice']
        
        st.success(f"###### {Stock_Name}  \t \t \t ${Stock_Price}")

        current_date = datetime.now().date()

        tickerDf = ticker_Data.history(period='1d', start='2022-01-01', end=current_date)

        st.line_chart(tickerDf.Close)
        st.line_chart(tickerDf.Volume)
    else:
        st.write('\N{cross mark} Stock ticker not found!')
