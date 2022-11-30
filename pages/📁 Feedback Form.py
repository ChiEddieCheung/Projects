import streamlit as st
import pandas as pd
import mysql.connector as mqc

st.set_page_config(
    page_title="Feedback Form",
    layout = "wide"
)

hide_menu = """
    <style>
        #MainMenu {visibility: hidden;}
        Footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 28px">Feedback Form</h1>
    </div><br>
"""
st.markdown(html_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

def init_connection():
    return mqc.connect(**st.secrets['mysql'])

#def create_table():
#    c.execute('CREATE TABLE IF NOT EXISTS blogtable(author varchar(80),title varchar(80),article varchar(500),postdate date)')

def add_data(author,title,article,postdate):
    c.execute('INSERT INTO blogtable (author,title,article,postdate) VALUES (%s,%s,%s,%s)',(author,title,article,postdate))
    conn.commit()

st.write("###### *Please leave any comment or idea on my feedback form.*")
st.write('###### *Your feedback is very important to me!*')
#create_table()

with st.form('myForm', clear_on_submit=True):
    conn = init_connection()
    c = conn.cursor()
    
    blog_title = st.text_input('Enter Your Topic:')
    blog_author = st.text_input("Enter Your Name (or Email):",max_chars=50)
    blog_article = st.text_area("Enter Your Feedback:",height=200)
    blog_post_date = st.date_input("Post Date:")
    submit_button = st.form_submit_button('Add')    
    if submit_button:
        add_data(blog_author,blog_title,blog_article,blog_post_date)
        st.success("Post: '{}' is saved".format(blog_title))
        c.close()
        conn.close()
