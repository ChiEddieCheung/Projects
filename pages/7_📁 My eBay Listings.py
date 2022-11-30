import streamlit as st
from bs4 import BeautifulSoup
from PIL import Image
import streamlit.components.v1 as components

hide_menu = """
    <style>
        #MainMenu {Visibility: Hidden}
        footer {Visibility: Hidden}    
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.caption('*Page under construction*')
st.write('#### My eBay Listings')

sSite = "https://www.ebay.com/itm/403826614108"
sImg = "https://i.ebayimg.com/images/g/m-EAAOSwl1diWZJN/s-l500.jpg"
sImg2 = "https://i.ebayimg.com/images/g/Ha0AAOSwg8FiWZJV/s-l500.jpg"

col1, col2 = st.columns([3,5], gap='medium')

with col1:
    #st.write('Slide to select picture:')
    val = st.slider('Slide to select picture:', 1, 2, 1)

    if val == 1:    
        showImg = f"""
            <img src={sImg} 
            width="160" height="240" alt="LEGO Harry Potter">
        """
        st.markdown(showImg, unsafe_allow_html=True)
        st.caption('Picture 1 of 2')   
    else:       
        st.image(sImg2, width=240)
        st.caption('Picture 2 of 2')

with col2:
    st.write('##### LEGO Harry Potter Hogwarts Moment')
    #if st.button('View Detail...'):
    st.write(f'''
        <a href={sSite}>
        <button>
            View Details...
        </button>
        </a>
    ''', unsafe_allow_html=True)
    
