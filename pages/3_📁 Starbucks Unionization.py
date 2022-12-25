import streamlit as st
import pandas as pd
import plotly.express as px
#import plotly.graph_objects as go

st.set_page_config(
    page_title="Starbucks Stores Unionization",
    layout = "wide"    
)

hide_menu = """
    <style>
        #MainMenu {Visibility: Hidden}
        footer {Visibility: Hidden}    
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

html_temp = """
    <div style="background-color:{};padding:5px;border-radius:8px">
    <h1 style="color:{};text-align: center;font-size: 24px">Starbucks Stores Unionization</h1>
    </div><br>
"""
st.markdown(html_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

df = pd.read_csv('stores.csv')

# Add Size column for plot bubble size
df['Size'] = 6

# Sort by 'Petition File Date' column
df.sort_values(by=['Petition File Date'], inplace=True)

df['Petition File Date'] = \
    pd.to_datetime(df['Petition File Date']).dt.strftime('%m/%d/%Y')

# Make a new dataframe copy df2 for displaying data
# Original dataframe df is for creating Plotly map
df2 = df.copy()

# Drop unnecessary columns
df2.drop('Size', axis='columns', inplace=True)
df2.drop('NLRB Case Number(s)', axis=1, inplace=True)
df2.drop('lat', axis=1, inplace=True)
df2.drop('lon', axis=1, inplace=True)

# Rename Address column
df2 = df2.rename({'Address': 'Store Address'}, axis=1)

# Color each row based on 'Store Status'
def heatmap(x):                        
    if (x['Store Status']) == 'Union Win':
        color = 'lightgreen'
    elif (x['Store Status']) == 'Union Loss':
        color = 'tomato'
    elif (x['Store Status']) == 'Store Closed':
        color = 'tomato'
    elif (x['Store Status']) == 'Filed':
        color = 'yellow'
    elif (x['Store Status']) == 'Contested':
        color = 'yellow'
    return[f'background-color: {color}']*6

st.dataframe(df2.style.apply(heatmap, axis=1), use_container_width=True)

st.markdown("<h5 style='text-align: center;'>Stores Unionization Map</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>(Source: Starbucks Workers United and CNBC)</h6>", unsafe_allow_html=True)

# Plotly scatter mapbox method
Condition_Color = {'Union Win': 'green', \
    'Union Loss': 'red', \
    'Store Closed': 'red', \
    'Filed': 'yellow', 'Contested': 'yellow'}

fig = px.scatter_mapbox(df,
    lat = df['lat'],
    lon = df['lon'],    
    zoom = 3,
    color=df['Store Status'],     
    color_discrete_map = Condition_Color, 
    category_orders = {'Store Status': ['Union Win', 'Union Loss', 'Store Closed', 'Filed', 'Contested']},
    size = df.Size, 
    size_max = 6, 
    hover_name = df.Address,    
    hover_data = {'Size':False, 'lat':False, 'lon':False, 'Store Status':True},    
    width = 1000,
    height = 667    
)

selection = st.radio(
    "Map Style:",
    ('Open Street Map', 'Carto Positron', 'Stamen Terrain', 'Stamen Watercolor'), 
    index=0, horizontal=True)    

if selection == 'Open Street Map':
    selection = 'open-street-map'
elif selection == 'Carto Positron':
    selection = 'carto-positron'
elif selection == 'Stamen Terrain':
    selection = 'stamen-terrain'
elif selection == 'Stamen Watercolor':
    selection = 'stamen-watercolor'

fig.update_layout(mapbox_style=selection)
fig.update_layout(margin={'r':0, 't':0, 'l':0, 'b':0})

st.plotly_chart(fig)

# Plotly graph object method
#fig = go.Figure()

#df['text'] = df['Address'] + ', ' + df['Store Status']

#fig.add_trace(    
#    go.Scattergeo(
#        locationmode = 'USA-states',
#        lon = df['lon'],
#        lat = df['lat'],
#        text = df['text'],    
#        mode = 'markers',
#        marker = dict(color=SetColor(df))
#    )
#)

#fig.update_layout(
#    title_text = 'Starbucks Stores Unionization',
#    margin = dict(
#        l = 0,
#        t = 40
#    ),
#    width = 900,
#    height = 577,
#    geo = dict(
#        scope = 'usa',
#    )
#)
