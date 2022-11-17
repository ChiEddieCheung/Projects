import streamlit as st
import time

st.set_page_config(
    page_title='Home Page',
    initial_sidebar_state='expanded',
    layout='wide'
)

hide_menu = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: visible;                
                padding: 3px;
                background-color: DarkSalmon;
                color: white;}
    </style>
    <body>
        <footer>
            <p><i>Updated 11/07/2022</i></p>
        </footer>
    </body>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.subheader("Eddie Cheung's Python Learning Project")
st.info('##### \N{clipboard} On the left sidebar contains a list of apps written in Streamlit Python')
