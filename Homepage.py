import streamlit as st

st.set_page_config(
    page_title="Eddie Cheung's Python Study Project",
    page_icon='🏠',
    initial_sidebar_state='auto',
    layout='wide'
)

hide_menu = """
    <style>               
        #MainMenu {visibility: hidden}                
        footer {
            visibility: hidden;
        }
        footer:after {
            visibility: visible;
            content: 'Updated 12/24/2022';
            font-style: italic;
            display: block;    
            text-align: center;
            background: #e2f0fb;
            border-radius: 8px;
            color: black;
            padding: 5px;
            height: 35px;
        }   
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

ImgUrl = "https://github.com/ChiEddieCheung/Projects/blob/main/bluewave.png?raw=true"
def add_background(file):
    binstr = file
    bgImg = '''
    <style>
        .stApp {
            background-image: url(%s);  
            background-attachment: fixed;
            background-size: cover; 
            background-repeat: repeat;
         }
    </style>
    ''' % binstr
    st.markdown(bgImg, unsafe_allow_html=True)

add_background(ImgUrl)
h1_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 28px">Eddie Cheung's Python Study Project</h1>
    </div><br>
"""
st.markdown(h1_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

st.write('')
st.write('###### <center>This site shares my new journey into the world \
    of Python programming through different interesting projects written \
    in Streamlit app framework and other Python tools.</center>', unsafe_allow_html=True)

for i in range(5):
    st.write('')

st.write("###### <center>Feel free to check out [My bio]" \
    "(https://my.indeed.com/p/chichiueddiec-5mgjx37) " \
    "and drop me [some feedbacks or ideas]" \
    "(https://chicheung.streamlit.app/Feedback_Form).</center>", unsafe_allow_html=True)
