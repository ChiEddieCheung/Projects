import streamlit as st
import pandas as pd
import numpy as np
import requests
import warnings

st.set_page_config(
    page_title="Stock Sentiment",
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
#warnings.filterwarnings('ignore')

#st.sidebar.title('StockTwits Sentiment Metric')
symbol = st.sidebar.text_input("Enter a stock ticker:", max_chars=5)

if symbol != '':
    url = 'https://api.stocktwits.com/api/2/streams/symbol/{}.json'.format(symbol)
    
    try:
        data = requests.get(url).json()  
        st.title('StockTwits Sentiment Metric for')
        st.title(data['symbol']['title'])

        df = pd.DataFrame()     #Initialize blank data frame

        for i in range(0, len(data['messages'])):
            if i < 30:
                msg = data['messages'][i]            
                
                followers = msg['user']['followers']            
                try:
                    sentiment = msg['entities']['sentiment']['basic']
                except:
                    sentiment = 'Neutral'            
                date_created = msg['created_at']

                row = np.asarray([date_created, followers, sentiment])
                #row_df = pd.DataFrame(columns= ['Date Created', 'Followers', 'Sentiment'])
                df = df.append(pd.DataFrame(row).T)
            
        df = df.rename(columns = {0:'Date Created', 1:'Followers', 2:'Sentiment'})
        df['Date Created'] = pd.to_datetime(df['Date Created']).dt.date
        df = df.reset_index().drop(['index'], axis=1)
        st.write(df)
    except:
        st.write('\N{cross mark} Stock ticker not found!')
