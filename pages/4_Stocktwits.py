import streamlit as st
import pandas as pd
import numpy as np
import requests

#st.cache(suppress_st_warning=True)
  
hide_menu = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.subheader("StockTwits Latest Messages")

symbol = ''
symbol = st.text_input("Enter a stock ticker:", max_chars=5)
if symbol:
    try:
        r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
        data = r.json()    
        
        st.success(data['symbol']['title'])
        st.write('___')

        for message in data['messages']:                 
            st.image(message['user']['avatar_url'])
            st.write(message['user']['username'])        
            st.write(message['created_at'])
            st.write(message['body'])        
            st.write('___')                
    except:
        st.write('\N{cross mark} Stock ticker not found!')
