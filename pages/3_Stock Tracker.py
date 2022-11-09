import pandas as pd
import streamlit as st
import yfinance as yf
from datetime import datetime

st.set_page_config(
    page_title="TV Tracker",
    layout = "wide",
    initial_sidebar_state="expanded"
)

hide_menu = """
    <style>
        #MainMenu {Visibility: Hidden}
        footer {Visibility: Hidden}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.title('Stock Price and Volume Charts')
ticker_Sym = st.text_input('Enter a stock ticker:', max_chars=5)
ticker_Data = yf.Ticker(ticker_Sym)

info = yf.Ticker(ticker_Sym).info
if info:
    if 'shortName' in info:
        Stock_Name = info['shortName']

if (ticker_Sym != ''):
    try:
        msg = 'You enter stock ' + Stock_Name
        st.write("### " + msg)

        #Method 1:
            #now = datetime.now()
            #current_date = now.date()
        #Method 2:
            #or 1 line of code for current date
        current_date = datetime.now().date()

        tickerDf = ticker_Data.history(period='1d', start='2022-01-01', end=current_date)

        st.area_chart(tickerDf.Close)
        st.line_chart(tickerDf.Volume)
    except:
        st.write('\N{cross mark} Stock ticker not found!')
