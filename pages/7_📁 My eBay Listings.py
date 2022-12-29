import streamlit as st
import pyqrcode
import png

st.set_page_config(
    page_title="My eBay Listings",
    layout = "wide",    
)

hide_menu = """
    <style>
        #MainMenu {Visibility: Hidden}
        footer {Visibility: Hidden}    
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

#st.caption('(*Page under construction*)')

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 24px">My eBay Listings</h1>
    </div><br>
"""
st.markdown(html_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

sSite = "https://www.ebay.com/itm/403826614108"
sImg1 = "https://i.ebayimg.com/images/g/m-EAAOSwl1diWZJN/s-l500.jpg"
sImg2 = "https://i.ebayimg.com/images/g/Ha0AAOSwg8FiWZJV/s-l500.jpg"

col1, col2 = st.columns([3,5], gap='medium')

with col1:
    #st.write('Slide to select picture:')
    val = st.slider('Slide to select picture:', 1, 2, 1)

    if val == 1:    
        #showImg = f"""
        #    <img src={sImg} 
        #    width="160" height="240" alt="LEGO Harry Potter">
        #"""
        #st.markdown(showImg, unsafe_allow_html=True)
        
        st.image(sImg1, caption='LEGO Harry Potter Hogwarts Moment', width=160)
        st.caption('Picture 1 of 2')   
    else:       
        st.image(sImg2, caption='LEGO Harry Potter Hogwarts Moment', width=240)
        st.caption('Picture 2 of 2')

with col2:
    st.write('##### LEGO Harry Potter Hogwarts Moment: Potions Class (76383)')    
    st.markdown(f"""
        <a href={sSite}>
        <button class=button>
            View Details...
        </button>
        </a>
    """, unsafe_allow_html=True)
    
    st.write('')
        
    st.caption('or scan the QR code below to see product details:')
    url = pyqrcode.create(sSite)     
    file_name = '403826614108'            
    url.png(f'ebay{file_name}.png', scale = 6)
    st.image(f'ebay{file_name}.png', width=200)
