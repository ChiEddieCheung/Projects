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
st.write('<center><h3>Stock Price Analysis</h3></center>', \
    unsafe_allow_html=True)

#df = pd.read_csv('main-projects/NEM.csv')
ticker = st.text_input('Enter a stock ticker:', max_chars=5)

today = datetime.date.today()
datediff = datetime.timedelta(365)

col1, col2 = st.columns(2)
with col1:
    start_date = today - datediff
    start_date = st.date_input('Start Date:', value=start_date)
with col2:
    end_date = st.date_input('End Date:')

search = st.button('Search', key={ticker})

if ticker:    
    stock = yf.Ticker(ticker)
    st.info(stock.get_info()['shortName'])
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
                        vertical_spacing=0.02,
                        row_heights=[0.5, 0.2, 0.2])
    
    # Draw candlestick chart
    fig.add_trace(go.Candlestick(x=df.index, 
    open=df.Open, high=df.High, low=df.Low, close=df.Close), 
    row=1, col=1)

    fig.update_yaxes(title='Price', row=1, col=1)

    # Add 20 EMA and 50 EMA lines on the chart
    fig.add_trace(go.Scatter(x=df.index, y=df['20 EMA'], 
        line=dict(color='blue', width=2), name='20-day MA'))
    fig.add_trace(go.Scatter(x=df.index, y=df['50 EMA'],
        line=dict(color='brown', width=2), name='50-day MA'))
    
    # Remove weekend gaps on the chart
    fig.update_xaxes(rangebreaks=[dict(bounds=['sat','mon'])])

    fig.update_layout(title=f'{ticker.upper()} Candlestick Chart', 
        xaxis_rangeslider_visible=False,
        width=1000,height=800,showlegend=False,
        margin={'l':40,'t':30,'b':20,'r':20})

    # Draw volume bar chart
    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], showlegend=False), row=2, col=1)

    fig.update_yaxes(title='Volume', row=2, col=1)

    # Draw RSI line chart
    fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], line=dict(color='black', width=2),
                    showlegend=False), row=3, col=1)
    
    fig.add_hline(y=30, line_dash='dot', fillcolor='gray', row=3, col=1)
    fig.add_hline(y=70, line_dash='dot', fillcolor='gray', row=3, col=1)

    fig.update_yaxes(title='RSI', row=3, col=1)
                        
    st.plotly_chart(fig)   
