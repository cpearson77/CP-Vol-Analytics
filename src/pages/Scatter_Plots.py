import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd


#dfvol = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
url = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/volgrid1.csv?raw=true'
dfvol = pd.read_csv(url,header=[0,1],index_col=0)
dfvol.columns = dfvol.columns.map(''.join)
dfvol = dfvol.tail(-1)
dfvol = dfvol[0:1345]
dfvol= dfvol.ffill()
dfvol.columns = ["1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
                          "3m3y", "3m5y", "3m7y", "3m10y", "3m15y", "3m20y", "3m30y", "6m1y", "6m2y", "6m3y", "6m5y",
                          "6m7y", "6m10y", "6m15y", "6m20y", "6m30y","9m1y", "9m2y", "9m3y", "9m5y",
                          "9m7y", "9m10y", "9m15y", "9m20y", "9m30y", "1y1y", "1y2y", "1y3y", "1y5y", "1y7y", "1y10y",
                          "1y15y", "1y20y", "1y30y","2y1y", "2y2y", "2y3y", "2y5y",
                          "2y7y", "2y10y", "2y15y", "2y20y", "2y30y","3y1y", "3y2y", "3y3y", "3y5y",
                          "3y7y", "3y10y", "3y15y", "3y20y", "3y30y","5y1y", "5y2y", "5y3y", "5y5y",
                          "5y7y", "5y10y", "5y15y", "5y20y", "5y30y","7y1y", "7y2y", "7y3y", "7y5y",
                          "7y7y", "7y10y", "7y15y", "7y20y", "7y30y","10y1y", "10y2y", "10y3y", "10y5y",
                          "10y7y", "10y10y", "10y15y", "10y20y", "10y30y","15y1y", "15y2y", "15y3y", "15y5y",
                          "15y7y", "15y10y", "15y15y", "15y20y", "15y30y","20y1y", "20y2y", "20y3y", "20y5y",
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y", "Year"]
dfvol.index.rename('Date', inplace=True)

#dfswap = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fwdgrid1.csv?raw=true'
dfswap = pd.read_csv(url1,header=[0,1],index_col=0)
dfswap.columns = dfswap.columns.map(''.join)
dfswap = dfswap.tail(-1)
dfswap = dfswap[0:1345]
dfswap= dfswap.ffill()
dfswap.columns = ["1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
                          "3m3y", "3m5y", "3m7y", "3m10y", "3m15y", "3m20y", "3m30y", "6m1y", "6m2y", "6m3y", "6m5y",
                          "6m7y", "6m10y", "6m15y", "6m20y", "6m30y","9m1y", "9m2y", "9m3y", "9m5y",
                          "9m7y", "9m10y", "9m15y", "9m20y", "9m30y", "1y1y", "1y2y", "1y3y", "1y5y", "1y7y", "1y10y",
                          "1y15y", "1y20y", "1y30y","2y1y", "2y2y", "2y3y", "2y5y",
                          "2y7y", "2y10y", "2y15y", "2y20y", "2y30y","3y1y", "3y2y", "3y3y", "3y5y",
                          "3y7y", "3y10y", "3y15y", "3y20y", "3y30y","5y1y", "5y2y", "5y3y", "5y5y",
                          "5y7y", "5y10y", "5y15y", "5y20y", "5y30y","7y1y", "7y2y", "7y3y", "7y5y",
                          "7y7y", "7y10y", "7y15y", "7y20y", "7y30y","10y1y", "10y2y", "10y3y", "10y5y",
                          "10y7y", "10y10y", "10y15y", "10y20y", "10y30y","15y1y", "15y2y", "15y3y", "15y5y",
                          "15y7y", "15y10y", "15y15y", "15y20y", "15y30y","20y1y", "20y2y", "20y3y", "20y5y",
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y", "Year"]
dfswap.index.rename('Date', inplace=True)
dfswap1 = dfswap.reset_index(level=0)
#dfswap1['Date'] = pd.to_datetime(dfswap1['Date']).dt.strftime('%d/%m/%y')

dropdown4 = html.Div([
    html.P("Select Vol to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown",
                    clearable=False,
                    value="1y1y",
                    options=["1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y","2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y"],
                    className="ag-theme-balham")
])

dropdown5 = html.Div([
    html.P("Select Vol to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown1",
                    clearable=False,
                    value="10y10y",
                    options=["10y1y", "10y2y", "10y5y", "10y10y", "10y15y", "10y20y", "10y30y",
                             "15y1y", "15y2y", "15y5y",
                          "15y10y", "15y15y", "15y20y", "15y30y", "20y1y", "20y2y", "20y5y",
                          "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham")
])

scat1graph = dcc.Graph(id='scat1')
scat2graph = dcc.Graph(id='scat2')


@callback(Output("scat1", "figure"), Input("vol-dropdown", "value"))
def update_figure(vol1):
    return px.scatter(dfswap1, x=dfswap[vol1], y=dfvol[vol1], color='Year',
                  hover_data=["Date"],
                  labels={
                    "x": "Fwd",
                    "y": "Norm Vol",
                    "hover_data": "Date"},)

@callback(Output("scat2", "figure"), Input("vol-dropdown1", "value"))
def update_figure(vol1):
    return px.scatter(dfswap1, x=dfswap[vol1], y=dfvol[vol1], color='Year',
                  hover_data=["Date"],
                  labels={
                    "x": "Fwd",
                    "y": "Norm Vol",
                    "hover_data": "Date"},)


#dash.register_page(__name__)
layout = dbc.Container([
    dbc.Row([dbc.Col(dropdown4),
             dbc.Col(dropdown5),]),
    dbc.Row([dbc.Col(scat1graph),
             dbc.Col(scat2graph)])],
    fluid=True)
