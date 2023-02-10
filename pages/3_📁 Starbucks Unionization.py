import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Starbucks Unionization",
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
    <h1 style="color:{};text-align: center;font-size: 24px">Starbucks Unionization</h1>
    </div><br>
"""
st.markdown(html_temp.format('#e2f0fb','black'),unsafe_allow_html=True)

df = pd.read_csv('stores.csv')

st.markdown("<h5 style='text-align: center;'>Stores Unionization Map</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>(Source: Starbucks Workers United and CNBC)</h6>", unsafe_allow_html=True)
plot_spot = st.empty()

# Add Size column for plot bubble size
df['Size'] = 6

# Sort by 'Petition File Date' column
df.sort_values(by=['Petition File Date'], inplace=True)

df['Petition File Date'] = \
    pd.to_datetime(df['Petition File Date']).dt.strftime('%m/%d/%Y')

# Make a new dataframe copy df2 for displaying data
# Original dataframe df is for creating Plotly map
df2 = df.copy()

# Drop unnecessary columns in df
df.drop('Size', axis='columns', inplace=True)
df.drop('NLRB Case Number(s)', axis=1, inplace=True)
df.drop('lat', axis=1, inplace=True)
df.drop('lon', axis=1, inplace=True)

# Replace NaN cell values with blank values
df = df.fillna('')

# Rename Address column
df = df.rename({'Address': 'Store Address'}, axis=1)

filter = st.radio('**Show store status:**',
                    options=('All', 'Union Win', 'Union Loss', 'Store Closed', 'Filed', 'Contested'), 
                    horizontal=True)

if filter == 'Union Win':
    df = df[(df['Store Status'] == 'Union Win')]
    df2 = df2[(df2['Store Status'] == 'Union Win')]    
elif filter == 'Union Loss':
    df = df[(df['Store Status'] == 'Union Loss')]
    df2 = df2[(df2['Store Status'] == 'Union Loss')]    
elif filter == 'Store Closed':
    df = df[(df['Store Status'] == 'Store Closed')]
    df2 = df2[(df2['Store Status'] == 'Store Closed')]    
elif filter == 'Filed':
    df = df[(df['Store Status'] == 'Filed')]
    df2 = df2[(df2['Store Status'] == 'Filed')]
elif filter == 'Contested':
    df = df[(df['Store Status'] == 'Contested')]
    df2 = df2[(df2['Store Status'] == 'Contested')]
else:
    df = df
    df2 = df2

selection = st.radio(
    "**Map Style:**",
    ('Open Street Map', 'Carto Positron', 'Stamen Terrain', 'Stamen Watercolor'), 
    index=0, horizontal=True) 
if selection == 'Open Street Map':
    selected = 'open-street-map'
elif selection == 'Carto Positron':
    selected = 'carto-positron'
elif selection == 'Stamen Terrain':
    selected = 'stamen-terrain'
elif selection == 'Stamen Watercolor':
    selected = 'stamen-watercolor'

# Color each row based on 'Store Status'
def heatmap(x):                        
    if (x['Store Status']) == 'Union Win':
        color = 'lightgreen'
    elif (x['Store Status']) == 'Union Loss':
        color = 'tomato'
    elif (x['Store Status']) == 'Store Closed':
        color = 'tomato'
    elif (x['Store Status']) == 'Filed':
        color = 'gold'
    elif (x['Store Status']) == 'Contested':
        color = 'gold'
    return[f'background-color: {color}']*6

with st.expander('Show stores data', expanded=False):
    st.dataframe(df.style.apply(heatmap, axis=1), use_container_width=True)

# Plotly scatter mapbox method
Condition_Color = {'Union Win': 'lightgreen', \
    'Union Loss': 'tomato', \
    'Store Closed': 'tomato', \
    'Filed': 'yellow', 'Contested': 'yellow'}

fig = px.scatter_mapbox(df2,
    lat = df2['lat'],
    lon = df2['lon'],    
    zoom = 3,     
    color = 'Store Status',
    color_discrete_map = Condition_Color,      
    category_orders = {'Store Status': ['Union Win', 'Union Loss', 'Store Closed', 'Filed', 'Contested']},
    size = 'Size',     
    size_max = 6, 
    hover_name = 'Address',    
    hover_data = {'Size':False, 'lat':False, 'lon':False, 'Store Status':True},    
    width = 1000,
    height = 667,    
    mapbox_style = selected
)

fig.update_layout(margin={'r':0, 't':30, 'l':0, 'b':0})

with plot_spot:
    st.plotly_chart(fig)
