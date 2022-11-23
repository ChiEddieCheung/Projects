import streamlit as st
import mysql.connector as mqc

#@st.experimental_singleton
#def init_connection():
#    return mqc.connect(**st.secrets["mysql"])

#conn = init_connection()

#@st.experimental_memo(ttl=600)
#def run_query(query):
#    with conn.cursor() as cur:
#        cur.execute(query)
#        return cur.fetchall()

#rows = run_query("SELECT * FROM mytable;")

#for row in rows:
#    # Emoji name syntax :{emoji name}:
#    st.write(f"{row[0]} has a :{row[1]}:")
st.write('Test')
