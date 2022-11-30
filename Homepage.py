import streamlit as st

st.set_page_config(
    page_title='Home Page',
    page_icon='🏠',
    initial_sidebar_state='auto',
    layout='wide'
)

hide_menu = """
    <style>               
        #MainMenu {visibility: hidden;}                
        footer {
            visibility: hidden;
        }
        footer:after {
            visibility: visible;
            content: 'Updated 11/30/2022';
            font-style: italic;
            display: block;    
            text-align: center;
            background: whitesmoke;
            color: black;
            padding: 5px;
            height: 35px;
        }   
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

urlImg = "https://github.com/ChiEddieCheung/Projects/blob/main/abstract.jpg?raw=true"

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("{urlImg}");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

with st.form('myform'):
    st.header("Eddie Cheung's Python Learning Project")

    st.write('')
    st.write('###### \N{clipboard} Sidebar menu contains a list of apps written in Streamlit Python')

    for i in range(5):
        st.write('')

    st.write("###### [My bio](https://my.indeed.com/p/chichiueddiec-5mgjx37) and drop me [some feedbacks or ideas](https://chicheung.streamlit.app/Feedback_Form).")
    send = st.form_submit_button('Hi')
    if send:
        st.markdown("""
            <head>
              <meta http-equiv="refresh" content="0; URL='https://my.indeed.com/p/chichiueddiec-5mgjx37'"/>
            </head>
          """, unsafe_allow_html=True)
