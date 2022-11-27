import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(
    page_title="Feedback Form",
    layout = "wide"
)

hide_menu = """
    <style>
        #MainMenu {visibility: hidden;}
        Footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 28px">My EBay Listings</h1>
    </div><br>
"""
st.markdown(html_temp.format('lightblue','black'),unsafe_allow_html=True)
