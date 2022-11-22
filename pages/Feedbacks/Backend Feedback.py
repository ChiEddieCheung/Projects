import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate,DATE)')

#def add_data(author,title,article,postdate):
#    c.execute('INSERT INTO blogtable(author,title,article,postdate) VALUES (?,?,?,?)',(author,title,article,postdate))
#    conn.commit()

def view_all_notes():
    c.execute('SELECT * FROM blogtable')
    data = c.fetchall()    
    return data

def view_all_titles():
    c.execute('SELECT DISTINCT title FROM blogtable')
    data = c.fetchall()    
    return data

def get_single_blog(title):
    c.execute('SELECT * FROM blogtable WHERE title="{}"'.format(title))
    data = c.fetchall()
    return data

def get_blog_by_title(title):
    c.execute('SELECT * FROM blogtable WHERE LOWER(title) LIKE "%{}%"'.format(title))
    data = c.fetchall()
    return data

def get_blog_by_author(author):
    c.execute('SELECT * FROM blogtable WHERE LOWER(author) LIKE "%{}%"'.format(author))
    data = c.fetchall()
    return data
 
def get_blog_by_msg(article):
    c.execute('SELECT * FROM blogtable WHERE article like "%{}%"'.format(article))
    data = c.fetchall()
    return data

def edit_blog_author(author,new_author):
    c.execute('UPDATE blogtable SET author ="{}" WHERE author="{}"'.format(new_author,author))
    conn.commit()
    data = c.fetchall()
    return data

def edit_blog_title(title,new_title):
    c.execute('UPDATE blogtable SET title ="{}" WHERE title="{}"'.format(new_title,title))
    conn.commit()
    data = c.fetchall()
    return data

def edit_blog_article(article,new_article):
    c.execute('UPDATE blogtable SET title ="{}" WHERE title="{}"'.format(new_article,article))
    conn.commit()
    data = c.fetchall()
    return data

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
st.set_option('deprecation.showPyplotGlobalUse', False) # Disable matplotlib warning

# Layout Templates
title_temp ="""
	<div style="background-color:cornflowerblue;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>	
	<h6>Author: {}</h6>
	<br/>
	<br/>	
	<p style="text-align:justify">{}</p>
	</div>
	"""

article_temp ="""
	<div style="background-color: cornflowerblue;padding: 10px;border-radius: 5px;margin: 10px;">
	<h4 style="color: white;text-align: center;">{}</h1>
	<h6>Author: {}</h6> 
	<h6>Post Date: {}</h6>	
	<br/>
	<br/>
	<p style="text-align:justify">{}</p>
	</div>
	"""

head_message_temp ="""
	<div style="background-color: cornflowerblue;padding: 10px;border-radius: 5px;margin: 10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<h6>Author: {}</h6> 		
	<h6>Post Date: {}</h6>		
	</div>
	"""

full_message_temp ="""
	<div style="background-color: lightsteelblue;overflow-x: auto;padding: 10px;border-radius: 5px;margin: 10px;">
		<p style="text-align: justify;color: black;padding: 10px">{}</p>
	</div>
	"""

def main():
	menu = ["Home","View User Feedback","Search Feedbacks","Manage Feedbacks"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		html_temp = """
			<div style="background-color:{};padding:5px;border-radius:8px">
			<h1 style="color:{};text-align: center;font-size: 28px">All User Feedbacks</h1>
			</div><br>
		"""
		st.markdown(html_temp.format('lightblue','black'),unsafe_allow_html=True)

		result = view_all_notes()
		for i in result:			
			short_article = str(i[2])[0:80] + '...'
			st.write(title_temp.format(i[1],i[0],short_article),unsafe_allow_html=True)

	elif choice == "View User Feedback":
		html_temp = """
			<div style="background-color:{};padding:5px;border-radius:8px">
			<h1 style="color:{};text-align: center;font-size: 28px">User Feedback</h1>
			</div><br>
		"""
		st.markdown(html_temp.format('lightblue','black'),unsafe_allow_html=True)
		#st.write('##### View Feedback')

		all_titles = [i[0] for i in view_all_titles()]
		postlist = st.sidebar.selectbox("Select a Post:",all_titles)
		post_result = get_blog_by_title(postlist)
		for i in post_result:
			st.markdown(head_message_temp.format(i[1],i[0],i[3]),unsafe_allow_html=True)
			st.markdown(full_message_temp.format(i[2]),unsafe_allow_html=True)			
				
	elif choice == "Search Feedbacks":
		html_temp = """
			<div style="background-color:{};padding:5px;border-radius:8px">
			<h1 style="color:{};text-align: center;font-size: 28px">Search Feedbacks</h1>
			</div><br>
		"""
		st.markdown(html_temp.format('lightblue','black'),unsafe_allow_html=True)

		search_term = st.text_input("Enter Something:").lower()		
		search_choice = st.radio("Field to Search:",("Title","Author"), horizontal=True)
		if st.button('Search'):
			if search_choice == "Title":
				article_result = get_blog_by_title(search_term)
			elif search_choice == "Author":
				article_result = get_blog_by_author(search_term)
			
			# Preview Articles
			for i in article_result:				
				st.write(head_message_temp.format(i[1],i[0],i[3]),unsafe_allow_html=True)
				st.write(full_message_temp.format(i[2]),unsafe_allow_html=True)
			
	elif choice == "Manage Feedbacks":
		html_temp = """
			<div style="background-color:{};padding:5px;border-radius:8px">
			<h1 style="color:{};text-align: center;font-size: 28px">Manage Feedbacks</h1>
			</div><br>
		"""
		st.markdown(html_temp.format('lightblue','black'),unsafe_allow_html=True)

													
		result = view_all_notes()
		clean_db = pd.DataFrame(result,columns=["Author","Title","Article","Post Date"])								
		st.dataframe(clean_db, use_container_width=True)
						
		if st.checkbox("Metrics"):		
			new_df = clean_db
			new_df['Length'] = new_df['Article'].str.len() 
			
			st.write("###### Author Stats")
			new_df['Author'].value_counts().plot(kind='bar')
			st.pyplot()

			new_df['Author'].value_counts().plot.pie(autopct="%1.1f%%")
			st.pyplot()

		if st.checkbox("WordCloud"):
			st.write("###### Word Cloud")
			text = ', '.join(clean_db['Article'])
			
			# Create and generate a word cloud image:
			wordcloud = WordCloud().generate(text)

			# Display the generated image:
			plt.imshow(wordcloud, interpolation='bilinear')
			plt.axis("off")
			st.pyplot()			

		if st.checkbox("BarH Plot"):
			with st.container():
				st.write("###### Length of Articles")
				new_df = clean_db
				new_df['Length'] = new_df['Article'].str.len() 
				barh_plot = new_df.plot.barh(x='Author',y='Length',figsize=(10,10))				
				st.pyplot()

if __name__ == '__main__':
	main()