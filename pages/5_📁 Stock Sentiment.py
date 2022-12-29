import streamlit as st
import pandas as pd
import numpy as np
import requests
import warnings
import yfinance as yf

def colorCell(val):
    if val > 1000:
        color='yellow'
    return f'background-color:{color}'
    
st.set_page_config(
    page_title="Stock Sentiment",
    layout = "wide",    
)

hide_menu = """
    <style>
        #MainMenu {Visibility: Hidden}
        footer {Visibility: Hidden}
    </style>
"""#
st.markdown(hide_menu, unsafe_allow_html=True)

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 24px">Stock Sentiment</h1>
    </div><br>
"""
st.markdown(html_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

colTicker, colElse = st.columns([1,3])
with colTicker:
    symbol = st.text_input("Enter a stock ticker:", max_chars=5)

search = st.button('Search', key={symbol})

if search or symbol:
    url = 'https://api.stocktwits.com/api/2/streams/symbol/{}.json'.format(symbol)
    
    try:
        data = requests.get(url).json() 

        if 'Price' in st.session_state:
            Stock_Price = '$' + str(st.session_state['Price'])
        else:
            Stock_Price = ''
        
        #st.success(f"###### {data['symbol']['title']} \n {Stock_Price}")
        stock = yf.Ticker(symbol)
        info = stock.get_info()
        
        imgUrl = info['logo_url']
        price = info['regularMarketPrice']
        st.success(data['symbol']['title'])

        col1, col2 = st.columns([1,4])
        with col1:
            st.image(imgUrl)
        with col2:
            st.metric(label='', value=f'${price}', 
            delta=round(info['regularMarketPrice'] - info['previousClose'], 2))

        df = pd.DataFrame()     #Initialize blank data frame        
    
        for i in range(0, len(data['messages'])):
            if i < 30:
                msg = data['messages'][i]            
                twitter = msg['user']['username']
                followers = msg['user']['followers']
                
                try:
                    sentiment = msg['entities']['sentiment']['basic']
                except:
                    sentiment = 'Neutral'            
                date_created = msg['created_at']

                row = np.asarray([date_created, twitter, followers, sentiment])
                
                df = df.append(pd.DataFrame(row).T)
            
        df = df.rename(columns = {0:'Date Created', 1:'Twitter Name', 2:'Followers', 3:'Sentiment'})        
        df['Date Created'] = pd.to_datetime(df['Date Created']).dt.date
        df = df.reset_index().drop(['index'], axis=1)
        checked = st.checkbox("Check to exclude 'Neutral' sentiment")
        if checked:
            df = df.query('Sentiment != "Neutral"')
        
        def color_cell(value):            
            highlight = 'background-color: #ffdd00;'            
            if int(value) > 1000:
                return highlight
            
        st.dataframe(df.style.applymap(color_cell, subset=['Followers']), use_container_width=True)        
        st.info("*Note: Twitters with over 1000 followers are highlighted." \
                " In general, twitters with large number of followers" \
                " usually have 'Neutral' sentiment.*")
    except:
        st.write('\N{cross mark} Stock ticker not found!')
