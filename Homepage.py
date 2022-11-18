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
        footer {
            visibility: hidden;
        }
        footer:after {
            visibility: visible;
            content: 'My bio url(https://my.indeed.com/p/chichiueddiec-5mgjx37)';
            font-style: italic;
            display: block;    
            text-align: center;
            background: LemonChiffon;
            color: black;
            padding: 5px;
            height: 35px;
        }        
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.subheader("Eddie Cheung's Python Learning Project")
st.info('##### \N{clipboard} Sidebar menu contains a list of apps written in Streamlit Python')
