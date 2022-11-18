import streamlit as st
import time
import streamlit.components.v1 as components

st.set_page_config(
    page_title='Home Page',
    initial_sidebar_state='expanded',
    layout='wide'
)

hide_menu = """
    <style>   
        body {background: white}
                            
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
            color: black;
            padding: 5px;
            height: 35px;
            border-radius: 5px;
            border: 2px solid #73AD21;
        }   
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.subheader("Eddie Cheung's Python Learning Project")
st.info('##### \N{clipboard} Sidebar menu contains a list of apps written in Streamlit Python')

st.success("##### \N{paperclip} [Feel free to check out my bio](https://my.indeed.com/p/chichiueddiec-5mgjx37)")
    #components.iframe("https://docs.streamlit.io/en/latest", scrolling=True)
