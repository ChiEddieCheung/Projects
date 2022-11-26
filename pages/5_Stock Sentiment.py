import streamlit as st
import pandas as pd
import numpy as np
import requests
import warnings

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

st.write('#### Stock Sentiment')
st.write('___')

def HiLightCells():
    color='yellow'
    return 'background-color: {}'.format(color)

symbol = st.text_input("Enter a stock ticker:", max_chars=5)
search = st.button('Search', key={symbol})

if search == True or symbol != '':
    url = 'https://api.stocktwits.com/api/2/streams/symbol/{}.json'.format(symbol)
    
    try:
        data = requests.get(url).json()  

        st.info(f"##### {data['symbol']['title']}")

        df = pd.DataFrame()     #Initialize blank data frame        

        for i in range(0, len(data['messages'])):
            if i < 30:
                msg = data['messages'][i]            
                twitter = msg['user']['username']
                #followers = f"{msg['user']['username']} has {msg['user']['followers']}"
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
        df.style.applymap(HiLightCells)
        st.write(df)
        
    except:
        st.write('\N{cross mark} Stock ticker not found!')
