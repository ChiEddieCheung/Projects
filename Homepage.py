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
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.title('Main Menu')
st.subheader('\N{clipboard} On the left sidebar contains samples of apps written in Streamlit Python')

with st.sidebar:
    st.success("Select a page above:")
