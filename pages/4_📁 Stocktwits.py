import streamlit as st
import pandas as pd
import numpy as np
import requests

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

st.info('#### StockTwits Latest Messages')

symbol = ''
symbol = st.text_input("Enter a stock ticker:", max_chars=5)
search = st.button('Search', key={symbol})
if symbol or search:
    try:
        r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
        data = r.json()    
        
        st.info(f"##### {data['symbol']['title']}")        

        for message in data['messages']:                  
            st.image(message['user']['avatar_url'])
            st.write(message['user']['username'])        
            st.write(message['created_at'])
            st.write(message['body'])        
            st.write('___')                
    except:
        st.write('\N{cross mark} Stock ticker not found!')
