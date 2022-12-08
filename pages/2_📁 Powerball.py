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
    layout = "wide"
)
st.markdown(hide_menu, unsafe_allow_html=True)

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 24px">Powerball Number Analysis</h1>
    </div><br>
"""
st.markdown(html_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

#powerball_csv = Path(__file__).parents[1]
#st.write(powerball_csv)

df = pd.read_csv('Powerball.csv')

df1 = pd.DataFrame(df, columns = ['Draw Date', 'P1', 'P2', 'P3', 'P4', 'P5'])
df2 = pd.DataFrame(df, columns = ['Draw Date', 'Powerball'])

checked = st.checkbox('Check to display Powerball data')
if checked:
    st.dataframe(df, use_container_width=True)

st.success('##### ' + 'Trending Patterns of Big 5 Numbers')
st.line_chart(df1, x='Draw Date') 

st.success('##### Trending Pattern of Powerball')
st.line_chart(df2, x='Draw Date')
