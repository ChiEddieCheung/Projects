import streamlit as st
import pandas as pd
import sqlite3

hide_menu = """
    <style>
        #MainMenu {visibility: hidden;}
        Footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

try:
    conn = sqlite3.connect('projects/pages/data.db')
    c = conn.cursor()
except:
    st.warning(st.exception)

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate,DATE)')

def add_data(author,title,article,postdate):
    c.execute('INSERT INTO blogtable(author,title,article,postdate) VALUES (?,?,?,?)',(author,title,article,postdate))
    conn.commit()

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 28px">Add Feedback</h1>
    </div><br>
"""
st.markdown(html_temp.format('lightblue','black'),unsafe_allow_html=True)

st.write("###### *Please leave any comment or idea on our feedback form.*")
st.write('###### *Your feedback is very important to me!*')
create_table()

with st.form('myForm', clear_on_submit=True):
    blog_title = st.text_input('Enter Your Topic:')
    blog_author = st.text_input("Enter Your Name (or Email)",max_chars=50)
    blog_article = st.text_area("Enter Your Feedback:",height=200)
    blog_post_date = st.date_input("Post Date")
    submit_button = st.form_submit_button('Add')    
    if submit_button:
        add_data(blog_author,blog_title,blog_article,blog_post_date)
        st.success("Post: '{}' is saved".format(blog_title))
