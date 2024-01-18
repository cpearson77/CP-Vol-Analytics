import dash
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output
import plotly.express as px
from dash import html
import dash_bootstrap_components as dbc
from dash import html
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app =dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY, dbc_css], use_pages=True)
server = app.server

app.layout = html.Div([
    html.Div("CP\'s Vol Analytics Tool"),
    html.Div([
        dcc.Link(page['name']+" | ", href=page['path'])
        for page in dash.page_registry.values()
    ]),
    html.Hr(),
    dash.page_container
]
)

if __name__ =="__main__":
    app.run(debug=True, port =8057)
