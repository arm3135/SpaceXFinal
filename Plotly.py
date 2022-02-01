pip3 install pandas dash

wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"

wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/spacex_dash_app.py"

python3 spacex_dash_app.py

import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px


# Read the airline data 
spacex_df = pd.read_csv("spacex_launch_dash.csv")
min_payload = spacex_df['Payload Mass (kg)'].min()
max_payload = spacex_df['Payload Mass (kg)'].max()


# Create a dash aPP
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),


# TASK 1: Add a dropdown list 
# dcc.Dropdown(id='site-dropdown',...)
 dcc.Dropdown(id='site-dropdown',
  options=[
           {'label': 'All Sites', 'value': 'ALL'},
           {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
           {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
           {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
           {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
],
  value='ALL',
placeholder='Select a Launch Site',
  searchable=True
# style={'width':'80%','padding':'3px','font-size':'20px','text-align-last':'center'}
),

 html.Br(),
