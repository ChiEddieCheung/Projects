import streamlit as st
import streamlit.components.v1 as com   #For rendering HTML code
import requests
import json

st.set_page_config(
    page_title="TV Show",
    layout = "wide",
    initial_sidebar_state="expanded"
)

hide_menu = """
    <style>
        #MainMenu {Visibility: Hidden}
        footer {Visibility: Hidden}

        p {font-family: arial}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

url = 'http://api.tvmaze.com/singlesearch/shows'

show_name = st.sidebar.text_input('Enter a TV Show name:')
if show_name != '':
    param = {"q":show_name}
    response = requests.get(url, param)
    data = json.loads(response.text)

    image = data['image']['medium']
    name = data['name']
    premiered = data['premiered']
    summary = data['summary']

    st.image(image)
    st.title(name)
    st.subheader('Date premiered: ' + premiered)
    with open('pages/style.css') as f:
        com.html(f"""                              
            <b>{summary}</b>
        """)