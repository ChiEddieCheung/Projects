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
            display: block;    
            text-align: centered;
            background-color: DarkOrange;
            color: white;
        }        
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.subheader("Eddie Cheung's Python Learning Project")
st.info('##### \N{clipboard} Sidebar menu contains a list of apps written in Streamlit Python')
