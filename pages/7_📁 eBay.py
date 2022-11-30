import streamlit as st
from bs4 import BeautifulSoup
from PIL import Image

st.caption('*Page under construction*')
st.title('My eBay Listings')

col1, col2 = st.columns(2)

sImg = "https://i.ebayimg.com/images/g/m-EAAOSwl1diWZJN/s-l500.jpg"
sImg2 = "https://i.ebayimg.com/images/g/Ha0AAOSwg8FiWZJV/s-l500.jpg"

with col1:
    showImg = f"""
        <img src={sImg} 
        width="54" height="80" alt="LEGO Harry Potter">
    """
    st.markdown(showImg, unsafe_allow_html=True)

with col2:
    st.image(sImg2, width=80)

