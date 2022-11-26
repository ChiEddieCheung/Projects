import pandas as pd
import streamlit as st
#from pathlib import Path

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

st.write('#### Powerball Number Analysis')
st.write('___')

#powerball_csv = Path(__file__).parents[1]
#st.write(powerball_csv)

df = pd.read_csv('Powerball.csv')

df1 = pd.DataFrame(df, columns = ['Draw Date', 'P1', 'P2', 'P3', 'P4', 'P5'])
df2 = pd.DataFrame(df, columns = ['Draw Date', 'Powerball'])

with st.checkbox('Check to display data table:)
    st.dataframe(df, use_container_width=True)

st.info('##### ' + 'Trending Patterns of Big 5 Numbers')
st.line_chart(df1, x='Draw Date') 

st.info('##### Trending Pattern of Powerball')
st.line_chart(df2, x='Draw Date')
