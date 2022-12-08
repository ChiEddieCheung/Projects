import streamlit as st
import streamlit.components.v1 as com   #For rendering HTML code
import requests
import json

st.set_page_config(
    page_title="TV Show",
    layout = "wide",
)

hide_menu = """
    <style>
        #MainMenu {Visibility: Hidden}
        footer {Visibility: Hidden}    
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
url = 'http://api.tvmaze.com/singlesearch/shows'

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 24px">TV Show Lookup</h1>
    </div><br>
"""
st.markdown(html_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

show_name = st.text_input('Enter a TV show name:')
search = st.button('Search', key={show_name})
if show_name != '' or search:
    try:
        param = {"q":show_name}
        response = requests.get(url, param)
        data = json.loads(response.text)

        st.write('')
        image = data['image']['medium']
        name = data['name']
        premiered = data['premiered']
        summary = data['summary']

        st.image(image)
        st.title(name)
        st.subheader('Date premiered: ' + premiered)       
        st.markdown(summary, unsafe_allow_html=True)
    except:
        st.write('\N{cross mark} TV show not found!')  
