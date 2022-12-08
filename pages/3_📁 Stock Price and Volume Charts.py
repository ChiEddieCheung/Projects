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

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 24px">Stock Price and Volume Charts</h1>
    </div><br>
"""
st.markdown(html_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

ticker_sym = st.text_input('Enter a stock ticker:', max_chars=5)
search = st.button('Search', key={ticker_sym})

if search or ticker_sym:
    ticker_Data = yf.Ticker(ticker_sym)

    info = yf.Ticker(ticker_sym).info
    if info['regularMarketPrice']:    
        Stock_Name = info['shortName']
        Stock_Price = info['regularMarketPrice']
        st.session_state['Price'] = Stock_Price

        st.success(f"###### {Stock_Name} \n ${Stock_Price}")

        current_date = datetime.now().date()

        tickerDf = ticker_Data.history(period='1d', start='2022-01-01', end=current_date)

        st.line_chart(tickerDf.Close)
        st.line_chart(tickerDf.Volume)
    elif info['regularMarketPrice'] is None:
        #st.write('\N{cross mark} Stock ticker not found!')
        st.write('')
