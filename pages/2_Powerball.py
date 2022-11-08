import pandas as pd
import streamlit as st

hide_menu = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""

st.set_page_config(
    page_title="Powerball Number Analysis",
    layout = "wide",
    initial_sidebar_state="expanded"
)
st.markdown(hide_menu, unsafe_allow_html=True)

st.title('Powerball Number Analysis')

df = pd.read_csv("powerball.csv")

df1 = pd.DataFrame(df, columns = ['Draw Date', 'P1', 'P2', 'P3', 'P4', 'P5'])
df2 = pd.DataFrame(df, columns = ['Draw Date', 'Powerball'])

st.dataframe(df)

st.success('##### ' + 'Trending Patterns of 5 Big Numbers')
st.line_chart(df1, x='Draw Date') 

st.success('##### Trending Pattern of Powerball')
st.line_chart(df2, x='Draw Date')
