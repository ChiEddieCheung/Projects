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
but 
url = 'http://api.tvmaze.com/singlesearch/shows'

st.info('#### TV Show Lookup')

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
