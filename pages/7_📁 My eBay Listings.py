import streamlit as st
from bs4 import BeautifulSoup
from PIL import Image

hide_menu = """
    <style>
        #MainMenu {Visibility: Hidden}
        footer {Visibility: Hidden}    
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.caption('*Page under construction*')
st.write('#### My eBay Listings')

sImg = "https://i.ebayimg.com/images/g/m-EAAOSwl1diWZJN/s-l500.jpg"
sImg2 = "https://i.ebayimg.com/images/g/Ha0AAOSwg8FiWZJV/s-l500.jpg"

col1, col2 = st.columns([3,5], gap='medium')

with col1:
    #st.write('Slide to select picture:')
    val = st.slider('Slide to select a picture to view:', 1, 2, 1)

    if val == 1:
        st.caption('Picture 1 of 2')
        showImg = f"""
            <img src={sImg} 
            width="80" height="120" alt="LEGO Harry Potter">
        """
        st.markdown(showImg, unsafe_allow_html=True)
    else:
        st.caption('Picture 2 of 2')
        st.image(sImg2, width=120)

with col2:
    st.write('###### LEGO Harry Potter Hogwarts Moment')
