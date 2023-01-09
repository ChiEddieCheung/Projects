import streamlit as st
import datetime
import pandas as pd
import pandas_ta as ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf

st.set_page_config(
    page_title = 'Stock Price Analysis',
    layout = 'wide'
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
    <h1 style="color:{};text-align:center;font-size:24px">Stock Price Analysis</h1>
    </div><br>
"""
st.markdown(html_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

today = datetime.date.today()
datediff = datetime.timedelta(365)

col1, col2, col3 = st.columns([1,1,1])
with col1:
    ticker = st.text_input('Enter a stock ticker:', max_chars=5, key='ticker')
with col2:
    start_date = today - datediff
    start_date = st.date_input('Start Date:', value=start_date)
with col3:
    end_date = st.date_input('End Date:')

search = st.button('Search', key={ticker})

if ticker:    
    stock = yf.Ticker(ticker)          
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
    
    st.write('')
    df = pd.DataFrame(yf.download(ticker, start=start_date, end=end_date,))             

    df['20 EMA'] = ta.ema(close=df['Adj Close'], length=20)
    #df['20 EMA'] = df['Adj Close'].rolling(window=20).mean()
    
    df['50 EMA'] = ta.ema(close=df['Adj Close'], length=50)
    #df['50 EMA'] = df['Adj Close'].rolling(window=50).mean()

    df['RSI'] = ta.rsi(close=df['Adj Close'], length=14)

    # Begin to draw Plotly charts
    fig = go.Figure()

    # The figure has 3 subplots: candlestick, volume, and RSI
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                        vertical_spacing=0.03,
                        row_heights=[3.0, 0.8, 0.8])
    
    # Draw candlestick chart
    fig.add_trace(go.Candlestick(x=df.index, 
    open=df.Open, high=df.High, low=df.Low, close=df.Close), 
    row=1, col=1)

    fig.update_yaxes(title='Price', row=1, col=1)

    # Add 20 EMA and 50 EMA lines on the chart
    fig.add_trace(go.Scatter(x=df.index, y=df['20 EMA'], 
        line=dict(color='blue', width=2), name='<b>20-day MA</b>'))
    fig.add_trace(go.Scatter(x=df.index, y=df['50 EMA'],
        line=dict(color='brown', width=2), name='<b>50-day MA</b>'))
    
    # Remove weekend gaps on the chart
    fig.update_xaxes(rangebreaks=[dict(bounds=['sat','mon'])])

    fig.update_layout(title=f'{ticker.upper()} Candlestick Chart', 
        xaxis_rangeslider_visible=False,
        showlegend=False,
        margin={'l':40,'t':30,'b':20,'r':20})
    
    colVolume, colRSI = st.columns([1,3])
    with colVolume:
        showVolume = st.checkbox('Show Volume Chart', value=True)
    
    with colRSI:
        showRSI = st.checkbox('Show RSI Chart', value=True)

    # Draw volume bar chart
    if showVolume:
        fig.add_trace(go.Bar(x=df.index, y=df['Volume'], showlegend=False), row=2, col=1)
        fig.update_yaxes(title='Volume', row=2, col=1)

    # Draw RSI line chart
    if showRSI:
        fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], line=dict(color='black', width=2),
                    showlegend=False), row=3, col=1)
        fig.add_hline(y=30, line_dash='dash', line_color='red', row=3, col=1)
        fig.add_hline(y=70, line_dash='dash', line_color='red', row=3, col=1)
        fig.update_yaxes(title='RSI', row=3, col=1)
                        
    st.plotly_chart(fig, use_container_width=True)   
    del st.session_state['ticker']
