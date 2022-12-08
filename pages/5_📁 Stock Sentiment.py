import streamlit as st
import pandas as pd
import numpy as np
import requests
import warnings

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

st.info('#### Stock Sentiment')

symbol = st.text_input("Enter a stock ticker:", max_chars=5)
search = st.button('Search', key={symbol})

if search == True or symbol != '':
    url = 'https://api.stocktwits.com/api/2/streams/symbol/{}.json'.format(symbol)
    
    try:
        data = requests.get(url).json()  

        st.success(f"###### {data['symbol']['title']}")

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
