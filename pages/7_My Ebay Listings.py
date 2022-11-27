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
st.markdown(hide_menu, unsafe_allow_html=True)

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 28px">My EBay Listings</h1>
    </div><br>
"""
st.markdown(html_temp.format('lightblue','black'),unsafe_allow_html=True)

st.write('LEGO Speed Champions: Ferrari F40 Competizione (75890)'

st.markdown('<a href="https://www.ebay.com/itm/403908078579?mkcid=16&mkevt=1&mkrid=711-127632-2357-0&ssspo=hd1-ldmkqjm&sssrc=2051273&ssuid=hd1-ldmkqjm&var=&widget_ver=artemis&media=MORE">LEGO Speed Champion</a>', unsafe_allow_html=True)

components.iframe('https://www.google.com")
