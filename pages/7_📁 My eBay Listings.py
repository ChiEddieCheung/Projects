import streamlit as st
from bs4 import BeautifulSoup
from PIL import Image
from datetime import datetime

st.caption('*Page under construction*')
st.title('My eBay Listings')

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

sImg = "https://i.ebayimg.com/images/g/m-EAAOSwl1diWZJN/s-l500.jpg"
sImg2 = "https://i.ebayimg.com/images/g/Ha0AAOSwg8FiWZJV/s-l500.jpg"

val = st.slider('Select a picture to view:', 1, 2, 1)
if val == 1:
    showImg = f"""
        <img src={sImg} 
        width="54" height="80" alt="LEGO Harry Potter">
    """
    st.markdown(showImg, unsafe_allow_html=True)
else:
    st.image(sImg2, width=80)
st.caption('LEGO Harry Potter Hogwarts Moment')
