import streamlit as st
import pandas as pd
import numpy as np
import networkx as nx
import plotly.graph_objs as go
from  PIL import Image

hide_menu = """
    <style>
        #MainMenu {Visibility: Hidden}
        footer {Visibility: Hidden}    
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 28px">Simple Network Graph Demo</h1>
    </div><br>
    """
st.markdown(html_temp.format('lightblue','black'),unsafe_allow_html=True)

with st.expander("About the App", expanded=True):
    st.subheader("The network graph app was built with Streamlit and Plotly to generate an interactive" \
                " network graph with different layout choices.")
    
    uploaded_file = st.file_uploader('Select a file:',type=['csv'], help='Select only CSV file with 2 columns of data')    
 
if uploaded_file is not None:  
    try:   
        df=pd.read_csv(uploaded_file)  
        A = list(df["Source"].unique())
        B = list(df["Target"].unique())
        node_list = set(A+B)
        G = nx.Graph() #Use the Graph API to create an empty network graph object
        
        #Add nodes and edges to the graph object
        for i in node_list:
            G.add_node(i)
        for i,j in df.iterrows():
            G.add_edges_from([(j["Source"],j["Target"])])    

        #Create three input widgets that allow users to specify their preferred layout and color schemes
        col1, col2, col3 = st.columns( [1, 1, 1])
        with col1:
            layout= st.selectbox('Choose a network layout',('Random Layout','Spring Layout','Shell Layout','Spectral Layout'), 2)
        with col2:
            color=st.selectbox('Choose color of the nodes', ('Blue','Red','Green','Rainbow','Red-Blue'), 0)      
        with col3:
            title=st.text_input('Add a chart title')

        #Get the position of each node depending on the user' choice of layout
        if layout=='Random Layout':
            pos = nx.random_layout(G) 
        elif layout=='Spring Layout':
            pos = nx.spring_layout(G, k=5, iterations=50)
        elif  layout=='Shell Layout':
            pos = nx.shell_layout(G)            
        elif  layout=='Spectral Layout':
            pos = nx.spectral_layout(G) 

        #Use different color schemes for the node colors depending on he user input
        if color=='Blue':
            colorscale='blues'    
        elif color=='Red':
            colorscale='reds'
        elif color=='Green':
            colorscale='greens'
        elif color=='Rainbow':
            colorscale='rainbow'
        elif color=='Red-Blue':
            colorscale='rdbu'        

        #Add positions of nodes to the graph
        for n, p in pos.items():
            G.nodes[n]['pos'] = p
        
        edge_trace = go.Scatter(
            x=[],
            y=[],
            line=dict(width=1,color='#888'),
            hoverinfo='none',
            mode='lines')

        for edge in G.edges():
            x0, y0 = G.nodes[edge[0]]['pos']
            x1, y1 = G.nodes[edge[1]]['pos']
            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])
        
        #Adding nodes to plotly scatter plot
        go.Scatter()
        node_trace = go.Scatter(
            x=[],
            y=[],
            text=[],
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale=colorscale, 
                color=[],
                size=20,
                colorbar=dict(
                    thickness=10,
                    title='# Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line=dict(width=0)))

        for node in G.nodes():
            x, y = G.nodes[node]['pos']
            node_trace['x'] += tuple([x])
            node_trace['y'] += tuple([y])

        for node, adjacencies in enumerate(G.adjacency()):
            node_trace['marker']['color']+=tuple([len(adjacencies[1])]) #Coloring each node based on the number of connections 
            node_info = adjacencies[0] +' # of connections: '+str(len(adjacencies[1]))
            node_trace['text']+=tuple([node_info])
        
        #Plot the final figure
        fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title=title, #title takes input from the user
                        title_x=0.45,
                        titlefont=dict(size=25),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

        st.plotly_chart(fig, use_container_width=True) #Show the graph in streamlit
    except:
        st.error('\N{cross mark} Invalid data structure: Only 2 columns of data allowed')
