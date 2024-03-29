import streamlit as st
import pandas as pd
import requests
import yfinance as yf

#st.cache(suppress_st_warning=True)
st.set_page_config(
    page_title="Stocktwits Messages",
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
    <h1 style="color:{};text-align: center;font-size: 24px">Stocktwits Messages</h1>
    </div><br>
"""
st.markdown(html_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

colTicker, colElse = st.columns([1,3])
with colTicker:
    symbol = st.text_input("Enter a stock ticker:", max_chars=5, key='symbol')
    
search = st.button('Search', key={symbol})
if symbol:
    r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
    data = r.json() 
               
    stock = yf.Ticker(symbol)          
    #info = stock.info

    #imgUrl = info['logo_url']
    last_price = round(stock.fast_info['lastPrice'], 2)
    prev_close = stock.fast_info['previousClose']
          
    #st.success(info['shortName'])
    st.success(data['symbol']['title'])

    col1, col2 = st.columns([1,4])
    #with col1:
        #st.image(imgUrl)
    with col2:
        st.metric(label='', value=f'${last_price}', 
        delta=round(last_price - prev_close, 2))

    st.write('___')
    for message in data['messages']:                  
        st.image(message['user']['avatar_url'])
        st.write(message['user']['username'])        
        st.write(message['created_at'])
        st.write(message['body'])        
        st.write('___')                    
    
    #st.write('\N{cross mark} Stock ticker not found!')

    del st.session_state['symbol']
