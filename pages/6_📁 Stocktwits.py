import streamlit as st
import pandas as pd
import numpy as np
import requests
import yfinance as yf

#st.cache(suppress_st_warning=True)
st.set_page_config(
    page_title="Stocktwits Latest Messages",
    layout = "wide",    
)
  
hide_menu = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 24px">Stocktwits Latest Messages</h1>
    </div><br>
"""
st.markdown(html_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

colTicker, colElse = st.columns([1,3])
with colTicker:
    symbol = st.text_input("Enter a stock ticker:", max_chars=5)
    
search = st.button('Search', key={symbol})
if symbol:
    try:
        r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
        data = r.json() 
        
        #if 'Price' in st.session_state:
        #    Stock_Price = '$' + str(st.session_state['Price'])
        #else:
        #    Stock_Price = ''

        #st.success(f"###### {data['symbol']['title']} \n {Stock_Price}") 
        stock = yf.Ticker(symbol)          
        info = stock.get_info()        
        imgUrl = info['logo_url']
        price = info['regularMarketPrice']
    
        st.success(stock.get_info()['shortName'])

        col1, col2 = st.columns([1,4])
        with col1:
            st.image(imgUrl)
        with col2:
            st.metric(label='', value=f'${price}', 
            delta=round(info['regularMarketPrice'] - info['previousClose'], 2))

        st.write('___')
        for message in data['messages']:                  
            st.image(message['user']['avatar_url'])
            st.write(message['user']['username'])        
            st.write(message['created_at'])
            st.write(message['body'])        
            st.write('___')                
    except:
        st.write('\N{cross mark} Stock ticker not found!')
