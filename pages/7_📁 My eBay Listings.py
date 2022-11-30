import streamlit as st
from bs4 import BeautifulSoup
from PIL import Image

st.caption('*Page under construction*')
st.title('My eBay Listings')

sImg = "https://i.ebayimg.com/images/g/m-EAAOSwl1diWZJN/s-l500.jpg"
sImg2 = "https://i.ebayimg.com/images/g/Ha0AAOSwg8FiWZJV/s-l500.jpg"

val = st.slider('Slide to select a picture to view:', 1, 2, 1)
if val == 1:
    st.caption('Picture 1 of 2')
    showImg = f"""
        <img src={sImg} 
        width="54" height="80" alt="LEGO Harry Potter">
    """
    st.markdown(showImg, unsafe_allow_html=True)
else:
    st.caption('Picture 2 of 2')
    st.image(sImg2, width=80)
st.caption('LEGO Harry Potter Hogwarts Moment')
