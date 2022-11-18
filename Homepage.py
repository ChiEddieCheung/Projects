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
            content: 'Updated 11/17/2022';
            font-style: italic;
            display: block;    
            text-align: center;
            background: LemonChiffon;
            color: black;
            padding: 5px;
            height: 35px;
        }     
        footer:before {
            visibility: visible;
            content: 'Test';
            text-align: center;
            display: block;
            height: 20px;
        }   
    </style>
    <footer>
      <a href="">A link</a>
    </footer>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.subheader("Eddie Cheung's Python Learning Project")
st.info('##### \N{clipboard} Sidebar menu contains a list of apps written in Streamlit Python')
