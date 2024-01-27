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
cols = dfvol.columns
#cols.remove('fistcolumn')
for col in cols:
    dfvol[col] = dfvol[col].astype(float)
dfvol = dfvol.reset_index(level=0)
dfvol.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfvol['Date'] = pd.to_datetime(dfvol['Date'], format='%d/%m/%Y')
dfvol = dfvol.set_index('Date')
dfvol=dfvol.round(1)
dfvol.index.rename('Date', inplace=True)

#dfswap = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fwdgrid1.csv?raw=true'
dfswap = pd.read_csv(url1,header=[0,1],index_col=0)
dfswap.columns = dfswap.columns.map(''.join)
dfswap = dfswap.tail(-1)
dfswap = dfswap[0:1345]
dfswap= dfswap.ffill()
cols1 = dfswap.columns
#cols.remove('fistcolumn')
for col in cols1:
    dfswap[col] = dfswap[col].astype(float)
dfswap = dfswap.reset_index(level=0)
dfswap.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfswap['Date'] = pd.to_datetime(dfswap['Date'], format='%d/%m/%Y')
dfswap = dfswap.set_index('Date')
dfswap=dfswap.round(2)
#dfswap.index.rename('Date', inplace=True)
dfswap1 = dfswap.reset_index(level=0)
dfswap1['Date'] = pd.to_datetime(dfswap1['Date']).dt.strftime('%d/%m/%y')
dfswap1['Year'] = dfswap1['Year'].astype('int64')
dfswap1["Year"] = dfswap1["Year"].round(0)

slide1 = html.Div([
    html.P("Select Lookback:"),
    dcc.Slider(
        dfswap1['Year'].min(),
        dfswap1['Year'].max(),
        step=None,
        value=dfswap1['Year'].min(),
        marks={str(year): str(year) for year in dfswap1['Year'].unique()},
        id='year-slider'),
])

dropdown4 = html.Div([
    html.P("Select EUR Vol to plot:"),
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
    html.P("Select EUR Vol to plot:"),
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

scat1graph = dcc.Graph(id='scat1',style={"height": 450, "width": 710})
scat2graph = dcc.Graph(id='scat2',style={"height": 450, "width": 710})


@callback(Output("scat1", "figure"), Input("vol-dropdown", "value"),
          Input('year-slider', 'value'))
def update_figure(vol1, selected_year):
    dffilt = dfswap1[dfswap1.Year >= selected_year]
    rows = dffilt.shape[0]
    dfswap2 = dfswap[0:rows]
    dfvol2 = dfvol[0:rows]
    return px.scatter(dffilt, x=dfswap2[vol1], y=dfvol2[vol1], trendline="ols",color='Year',
                  hover_data=["Date"],
                  labels={
                    "x": vol1 + " Fwd",
                    "y": vol1 + " Norm Vol",
                    "hover_data": "Date"},)

@callback(Output("scat2", "figure"), Input("vol-dropdown1", "value"),
          Input('year-slider', 'value'))
def update_figure(vol1, selected_year):
    dffilt = dfswap1[dfswap1.Year >= selected_year]
    rows = dffilt.shape[0]
    dfswap2 = dfswap[0:rows]
    dfvol2 = dfvol[0:rows]
    return px.scatter(dffilt, x=dfswap2[vol1], y=dfvol2[vol1], trendline="ols", color='Year',
                  hover_data=["Date"],
                  labels={
                    "x": vol1 + " Fwd",
                    "y": vol1 + " Norm Vol",
                    "hover_data": "Date"},)

url2 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/uvolgrid1.csv?raw=true'
dfuvol = pd.read_csv(url2,header=[0,1],index_col=0)
dfuvol.columns = dfuvol.columns.map(''.join)
dfuvol = dfuvol.tail(-1)
dfuvol = dfuvol[0:620]
dfuvol= dfuvol.ffill()
cols3 = dfuvol.columns
#cols.remove('fistcolumn')
for col in cols3:
    dfuvol[col] = dfuvol[col].astype(float)
dfuvol = dfuvol.reset_index(level=0)
dfuvol.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfuvol['Date'] = pd.to_datetime(dfuvol['Date'], format='%d/%m/%Y')
dfuvol = dfuvol.set_index('Date')
dfuvol=dfuvol.round(1)
dfuvol.index.rename('Date', inplace=True)

#dfswap = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
url3 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/ufwdgrid1.csv?raw=true'
dfuswap = pd.read_csv(url3,header=[0,1],index_col=0)
dfuswap.columns = dfuswap.columns.map(''.join)
dfuswap = dfuswap.tail(-1)
dfuswap = dfuswap[0:620]
dfuswap= dfuswap.ffill()
cols5 = dfuswap.columns
#cols.remove('fistcolumn')
for col in cols5:
    dfuswap[col] = dfuswap[col].astype(float)
dfuswap = dfuswap.reset_index(level=0)
dfuswap.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfuswap['Date'] = pd.to_datetime(dfuswap['Date'], format='%d/%m/%Y')
dfuswap = dfuswap.set_index('Date')
dfuswap=dfuswap.round(2)
#dfswap.index.rename('Date', inplace=True)
dfuswap1 = dfuswap.reset_index(level=0)
dfuswap1['Date'] = pd.to_datetime(dfuswap1['Date']).dt.strftime('%d/%m/%y')

dropdown6 = html.Div([
    html.P("Select USD Vol to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown2",
                    clearable=False,
                    value="1y1y",
                    options=["1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y","2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y"],
                    className="ag-theme-balham")
])

dropdown7 = html.Div([
    html.P("Select USD Vol to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown3",
                    clearable=False,
                    value="10y10y",
                    options=["10y1y", "10y2y", "10y5y", "10y10y", "10y15y", "10y20y", "10y30y",
                             "15y1y", "15y2y", "15y5y",
                          "15y10y", "15y15y", "15y20y", "15y30y", "20y1y", "20y2y", "20y5y",
                          "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham")
])

scat3graph = dcc.Graph(id='scat3',style={"height": 450, "width": 710})
scat4graph = dcc.Graph(id='scat4',style={"height": 450, "width": 710})

dropdown8 = html.Div([
    html.P("Select first EUR leg"),
    dcc.Dropdown(
                    id="vol-dropdown8",
                    clearable=False,
                    value="1y10y",
                    options=["1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y","2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y","10y1y", "10y2y", "10y5y", "10y10y", "10y15y", "10y20y", "10y30y",
                          "15y1y", "15y2y", "15y5y", "15y10y", "15y15y", "15y20y", "15y30y", "20y1y", "20y2y", "20y5y",
                          "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham")
])

dropdown9 = html.Div([
    html.P("Select first leg of EUR spread to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown9",
                    clearable=False,
                    value="5y10y",
                    options=["1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y","2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y","10y1y", "10y2y", "10y5y", "10y10y", "10y15y", "10y20y", "10y30y",
                             "15y1y", "15y2y", "15y5y",
                          "15y10y", "15y15y", "15y20y", "15y30y", "20y1y", "20y2y", "20y5y",
                          "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham")
])

dropdown10 = html.Div([
    html.P("Select second leg of EUR spread to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown10",
                    clearable=False,
                    value="2y10y",
                    options=["1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y","2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y","10y1y", "10y2y", "10y5y", "10y10y", "10y15y", "10y20y", "10y30y",
                             "15y1y", "15y2y", "15y5y",
                          "15y10y", "15y15y", "15y20y", "15y30y", "20y1y", "20y2y", "20y5y",
                          "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham")
])

scat5graph = dcc.Graph(id='scat5',style={"height": 450, "width": 1400})

@callback(Output("scat3", "figure"), Input("vol-dropdown2", "value"),
          Input('year-slider', 'value'))
def update_figure(vol1, selected_year):
    dffilt = dfuswap1[dfuswap1.Year >= selected_year]
    rows = dffilt.shape[0]
    dfuswap2 = dfswap[0:rows]
    dfuvol2 = dfvol[0:rows]
    return px.scatter(dffilt, x=dfuswap2[vol1], y=dfuvol2[vol1], trendline="ols" ,color='Year',
                  hover_data=["Date"],
                  labels={
                    "x": vol1 + " Fwd",
                    "y": vol1 + " Norm Vol",
                    "hover_data": "Date"},)

@callback(Output("scat4", "figure"), Input("vol-dropdown3", "value"),
          Input('year-slider', 'value'))
def update_figure(vol1, selected_year):
    dffilt = dfuswap1[dfuswap1.Year >= selected_year]
    rows = dffilt.shape[0]
    dfuswap2 = dfswap[0:rows]
    dfuvol2 = dfvol[0:rows]
    return px.scatter(dffilt, x=dfuswap2[vol1], y=dfuvol2[vol1], trendline="ols", color='Year',
                  hover_data=["Date"],
                  labels={
                    "x": vol1 + " Fwd",
                    "y": vol1 + " Norm Vol",
                    "hover_data": "Date"},)

@callback(Output("scat5", "figure"), Input("vol-dropdown8", "value"),
Input("vol-dropdown9", "value"),Input("vol-dropdown10", "value"),
          Input('year-slider', 'value'))
def update_figure(vol,vol1,vol2, selected_year):
    dffilt = dfswap1[dfswap1.Year >= selected_year]
    rows = dffilt.shape[0]
    #dfuswap2 = dfswap[0:rows]
    dfvol2 = dfvol[0:rows]
    return px.scatter(dffilt, x=dfvol2[vol], y=dfvol2[vol1]-dfvol2[vol2], trendline="ols", color='Year',
                  hover_data=["Date"],
                  labels={
                    "x": vol +' Norm Vol',
                    "y": vol1+' - '+vol2+' Norm Vol',
                    "hover_data": "Date"},)

dash.register_page(__name__)
layout = dbc.Container([
    dbc.Row([dbc.Col(slide1)]),
    dbc.Row([dbc.Col(dropdown4),
             dbc.Col(dropdown6),]),
    dbc.Row([dbc.Col(scat1graph),
             dbc.Col(scat3graph)]),
    dbc.Row([dbc.Col(dropdown5),
             dbc.Col(dropdown7),]),
    dbc.Row([dbc.Col(scat2graph),
             dbc.Col(scat4graph)]),
    dbc.Row([dbc.Col(dropdown8),
             dbc.Col(dropdown9),
             dbc.Col(dropdown10)]),
    dbc.Row([dbc.Col(scat5graph)])],
    fluid=True)
