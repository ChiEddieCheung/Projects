import streamlit as st
from bs4 import BeautifulSoup
from PIL import Image

st.caption('*Page under construction*')
st.title('My eBay Listings')

sImg = "https://i.ebayimg.com/images/g/m-EAAOSwl1diWZJN/s-l500.jpg"
sImg2 = "https://i.ebayimg.com/images/g/Ha0AAOSwg8FiWZJV/s-l500.jpg"

col1, col2 = st.columns(2)
with col1:
    showImg = f"""
        <img src={sImg} 
        width="54" height="80" alt="LEGO Harry Potter">
    """
    st.markdown(showImg, unsafe_allow_html=True)
    st.caption('LEGO Harry Potter Hogwarts Moment')
    #st.image(sImg, width=54)

with col2:
    st.image(sImg2, width=80)
    
val = st.slider('Picture 1 of 2', 1, 2, 1)
if val == 1:
    showImg = f"""
        <img src={sImg} 
        width="54" height="80" alt="LEGO Harry Potter">
    """
    st.markdown(showImg, unsafe_allow_html=True)
else:
    st.image(sImg2, width=80)
st.caption('LEGO Harry Potter Hogwarts Moment')
