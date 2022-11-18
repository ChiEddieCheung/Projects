import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

st.set_page_config(
    page_title="TV Tracker",
    layout = "wide"    
)

hide_menu = """
    <style>
        #MainMenu {Visibility: Hidden}
        footer {Visibility: Hidden}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.title('Stock Price and Volume Charts')
ticker_sym = st.text_input('Enter a stock ticker:', max_chars=5)
search = st.button('Search', key={ticker_sym})
ticker_Data = yf.Ticker(ticker_sym)

info = yf.Ticker(ticker_sym).info
if info:
    if 'shortName' in info:
        Stock_Name = info['shortName']

if (ticker_sym != '' or search):
    try:        
        st.info(f"##### {Stock_Name}")

        current_date = datetime.now().date()

        tickerDf = ticker_Data.history(period='1d', start='2022-01-01', end=current_date)

        st.area_chart(tickerDf.Close)
        st.line_chart(tickerDf.Volume)
    except:
        st.write('\N{cross mark} Stock ticker not found!')