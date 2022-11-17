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
       .css-qri22k.egzxvld0 {
            visibility: hidden;
        }
        footer:after {
            visibility: visible;
            content: 'Updated 11/17/2022';
            font-style: italic;
            display: block;    
            text-align: center;
            background-color: #ffcc00;
            background: lightyellow;
            color: black;
        }        
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.subheader("Eddie Cheung's Python Learning Project")
st.info('##### \N{clipboard} Sidebar menu contains a list of apps written in Streamlit Python')
