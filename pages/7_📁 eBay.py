import streamlit as st
from bs4 import BeautifulSoup
from PIL import Image

st.caption('*Page under construction*')
st.title('My eBay Listings')


sImg = "https://i.ebayimg.com/images/g/m-EAAOSwl1diWZJN/s-l500.jpg"
showImg = f"""
    <img src={sImg} 
     width="54" height="80" alt="LEGO Harry Potter">
"""
st.markdown(showImg, unsafe_allow_html=True)

st.write('---')

#st.image(sImg, width=40)

