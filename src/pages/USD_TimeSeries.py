import dash
from dash import Dash, dcc, html, Input, Output, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
import plotly.graph_objects as go
import math as math

suppress_callback_exceptions=True
#dfswap = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
url = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/ufwdgrid1.csv?raw=true'
dfswap = pd.read_csv(url,header=[0,1],index_col=0)
dfswap.columns = dfswap.columns.map(''.join)
dfswap = dfswap.tail(-1)
dfswap= dfswap.ffill()
cols = dfswap.columns
#cols.remove('fistcolumn')
for col in cols:
    dfswap[col] = dfswap[col].astype(float)
dfswap=dfswap.round(2)
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
dfswap = dfswap.reset_index(level=0)
dfswap1 = dfswap.reset_index(level=0)
dfswap= dfswap.ffill()
dfswap1= dfswap.ffill()
dfswap['Date'] = pd.to_datetime(dfswap['Date'], format='%d/%m/%Y')
dfswap1['Date'] = pd.to_datetime(dfswap1['Date'], format='%d/%m/%Y')
dfswap['Year'] = dfswap['Year'].astype('int64')
dfswap["Year"]=dfswap["Year"].round(0)

#dfvol = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/uvolgrid1.csv?raw=true'
dfvol = pd.read_csv(url1,header=[0,1],index_col=0)
dfvol.columns = dfvol.columns.map(''.join)
dfvol = dfvol.tail(-1)
dfvol= dfvol.ffill()
cols1 = dfvol.columns
#cols.remove('fistcolumn')
for col in cols1:
    dfvol[col] = dfvol[col].astype(float)
dfvol = dfvol[dfvol.columns.drop('YearUnnamed: 109_level_1')]
dfvol = dfvol.reset_index(level=0)
dfvol.columns = ["Date","1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y"]
dfvol['Date'] = pd.to_datetime(dfvol['Date'], format='%d/%m/%Y')
dfvol = dfvol.set_index('Date')
dfvol=dfvol.round(0)
dfvol1 = dfvol.head(-66)

#for realised vol
#dfdswap = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
dfdswap = pd.read_csv(url,header=[0,1],index_col=0)
dfdswap = dfdswap.tail(-1)
dfdswap1 = dfdswap.head(-66)
index = dfdswap1.index
dfdswap= dfdswap.ffill()
dfdswap = dfdswap[dfdswap.columns.drop('Year')]
cols7 = dfdswap.columns
#cols.remove('fistcolumn')
for col in cols7:
    dfdswap[col] = dfdswap[col].astype(float)
dfdswap = (dfdswap-dfdswap.shift(-1))*100
dfdswap = (dfdswap.rolling(66).std())*(math.sqrt(252))
dfdswap = dfdswap.dropna()
dfdswap =dfdswap.reset_index(drop=True)
dfdswap = dfdswap.assign(Date1=index)
dfdswap['Date1'] = pd.to_datetime(dfdswap['Date1'], format='%d/%m/%Y')
dfdswap = dfdswap.set_index('Date1')
dfdswap.columns = dfdswap.columns.map(''.join)
dfdswap=dfdswap.round(0)
dfdswap.columns = ["1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y"]
#removes data that is not in swap array to avoid massive jumps
dfimpr = dfvol1.subtract(dfdswap, fill_value=0)
dfimpr = dfimpr.loc[reversed(dfimpr.index)]
dfimpr1 = dfimpr.reset_index(level=0)
dfimpr1.columns = ["Date","1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y"]
dfdswap2 = dfdswap.reset_index(level=0)
dfdswap2.columns = ["Date","1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y"]
dfimpr2 = dfimpr1[dfimpr1["Date"].isin(dfdswap2["Date"])]
dfimpr2 = dfimpr2.set_index('Date')

slide1 = html.Div([
    html.P("Select Lookback:"),
    dcc.Slider(
        dfswap['Year'].min(),
        dfswap['Year'].max(),
        step=None,
        value=dfswap['Year'].min(),
        marks={str(year): str(year) for year in dfswap['Year'].unique()},
        id='year-slider'),
])

slide2 = html.Div([
    html.P("Select Lookback:"),
    dcc.Slider(
        dfswap['Year'].min(),
        dfswap['Year'].max(),
        step=None,
        value=dfswap['Year'].min(),
        marks={str(year): str(year) for year in dfswap['Year'].unique()},
        id='year-slider1'),
])

slide3 = html.Div([
    html.P("Select Lookback:"),
    dcc.Slider(
        dfswap['Year'].min(),
        dfswap['Year'].max(),
        step=None,
        value=dfswap['Year'].min(),
        marks={str(year): str(year) for year in dfswap['Year'].unique()},
        id='year-slider2'),
])

slide4 = html.Div([
    html.P("Select Lookback:"),
    dcc.Slider(
        dfswap['Year'].min(),
        dfswap['Year'].max(),
        step=None,
        value=dfswap['Year'].min(),
        marks={str(year): str(year) for year in dfswap['Year'].unique()},
        id='year-slider3'),
])

graph1 = dcc.Graph(id='fig11',style={"height": 450, "width": 710})
graph2 = dcc.Graph(id='fig12',style={"height": 450, "width": 710})
graph3 = dcc.Graph(id='fig13',style={"height": 450, "width": 710})
graph4 = dcc.Graph(id='fig14',style={"height": 450, "width": 710})
graph5 = dcc.Graph(id='fig15',style={"height": 450, "width": 710})
graph6 = dcc.Graph(id='fig16',style={"height": 450, "width": 710})

dropdown = html.Div([
    html.P("Select Vol to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown3",
                    clearable=False,
                    value="1y1y",
                    options=["1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y","2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y"],
                    className="ag-theme-balham")
                    #style={"height": 20, "width": 100})
])

dropdown1 = html.Div([
    html.P("Select Vol to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown4",
                    clearable=False,
                    value="10y10y",
                    options=["10y1y", "10y2y", "10y3y", "10y5y",
                          "10y7y", "10y10y", "10y15y", "10y20y", "10y30y","15y1y", "15y2y", "15y3y", "15y5y",
                          "15y7y", "15y10y", "15y15y", "15y20y", "15y30y","20y1y", "20y2y", "20y3y", "20y5y",
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham")
])

dropdown2 = html.Div([
    html.P("Select first leg to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown5",
                    clearable=False,
                    value="1y1y",
                    options=["1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y","2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y","10y1y", "10y2y", "10y3y", "10y5y",
                          "10y7y", "10y10y", "10y15y", "10y20y", "10y30y","15y1y", "15y2y", "15y3y", "15y5y",
                          "15y7y", "15y10y", "15y15y", "15y20y", "15y30y","20y1y", "20y2y", "20y3y", "20y5y",
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham")
])

dropdown3 = html.Div([
    html.P("Select second leg to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown6",
                    clearable=False,
                    value="1y10y",
                    options=["1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y","2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y","10y1y", "10y2y", "10y3y", "10y5y",
                          "10y7y", "10y10y", "10y15y", "10y20y", "10y30y","15y1y", "15y2y", "15y3y", "15y5y",
                          "15y7y", "15y10y", "15y15y", "15y20y", "15y30y","20y1y", "20y2y", "20y3y", "20y5y",
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham")
])

dropdown4 = html.Div([
    html.P("Select first leg to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown7",
                    clearable=False,
                    value="1y2y",
                    options=["1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y","2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y","10y1y", "10y2y", "10y3y", "10y5y",
                          "10y7y", "10y10y", "10y15y", "10y20y", "10y30y","15y1y", "15y2y", "15y3y", "15y5y",
                          "15y7y", "15y10y", "15y15y", "15y20y", "15y30y","20y1y", "20y2y", "20y3y", "20y5y",
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham")
])

dropdown5 = html.Div([
    html.P("Select second (belly) leg to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown8",
                    clearable=False,
                    value="1y5y",
                    options=["1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y","2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y","10y1y", "10y2y", "10y3y", "10y5y",
                          "10y7y", "10y10y", "10y15y", "10y20y", "10y30y","15y1y", "15y2y", "15y3y", "15y5y",
                          "15y7y", "15y10y", "15y15y", "15y20y", "15y30y","20y1y", "20y2y", "20y3y", "20y5y",
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham")
])

dropdown6 = html.Div([
    html.P("Select third leg to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown9",
                    clearable=False,
                    value="1y10y",
                    options=["1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y","2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y","10y1y", "10y2y", "10y3y", "10y5y",
                          "10y7y", "10y10y", "10y15y", "10y20y", "10y30y","15y1y", "15y2y", "15y3y", "15y5y",
                          "15y7y", "15y10y", "15y15y", "15y20y", "15y30y","20y1y", "20y2y", "20y3y", "20y5y",
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham")
])

@callback(Output("fig11", "figure"),
          Input("vol-dropdown3", "value"),Input('year-slider', 'value'))
def update_figure(vol, selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    trace1 = go.Scatter(x=dffilt['Date'],
                        y=dfvol[vol],
                        name=vol+' Implied Vol',
                        yaxis='y1')
    trace2 = go.Scatter(x=dffilt['Date'],
                        y=dfdswap[vol],
                        name=vol+' Realised Vol',
                        yaxis='y1')
    trace3 = go.Scatter(x=dffilt['Date'],
                        y=dfswap[vol],
                        name=vol+' Fwd',
                        yaxis='y2')
    trace4 = go.Scatter(x=dffilt['Date'],
                        y=dfimpr2[vol],
                        name=vol+' Imp-Real Vol',
                        yaxis='y1')
    data = [trace1, trace2, trace3, trace4]
    layout = go.Layout(yaxis=dict(title='Vol'),
                       yaxis2=dict(title='Fwd',
                                   overlaying='y',
                                   side='right'))
    fig1 = go.Figure(data=data, layout=layout)
    fig1.update_layout(
        font=dict(size=10))
    return fig1

@callback(Output("fig12", "figure"),
          Input("vol-dropdown4", "value"),Input('year-slider1', 'value'))
def update_figure(vol, selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    trace1 = go.Scatter(x=dffilt['Date'],
                        y=dfvol[vol],
                        name=vol+' Implied Vol',
                        yaxis='y1')
    trace2 = go.Scatter(x=dffilt['Date'],
                        y=dfdswap[vol],
                        name=vol+' Realised Vol',
                        yaxis='y1')
    trace3 = go.Scatter(x=dffilt['Date'],
                        y=dfswap[vol],
                        name=vol+' Fwd',
                        yaxis='y2')
    trace4 = go.Scatter(x=dffilt['Date'],
                        y=(dfimpr2[vol]),
                        name=vol+' Imp-Real Vol',
                        yaxis='y1')
    data = [trace1, trace2, trace3, trace4]
    layout = go.Layout(yaxis=dict(title='Vol'),
                       yaxis2=dict(title='Fwd',
                                   overlaying='y',
                                   side='right'))
    fig1 = go.Figure(data=data, layout=layout)
    fig1.update_layout(
        font=dict(size=10))
    return fig1
#callback for two input graph
@callback(Output("fig13", "figure"),
          Input("vol-dropdown5", "value"),Input("vol-dropdown6", 'value'),
          Input('year-slider2', 'value'))
def update_figure(vol, vol1, selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    trace1 = go.Scatter(x=dffilt['Date'],
                        y=dfvol[vol],
                        name=vol+" Implied Vol",
                        yaxis='y1')
    trace2 = go.Scatter(x=dffilt['Date'],
                        y=dfvol[vol1],
                        name=vol1+" Implied Vol",
                        yaxis='y1')
    trace3 = go.Scatter(x=dffilt['Date'],
                        y=dfswap[vol],
                        name=vol+' Fwd',
                        yaxis='y2')
    trace4 = go.Scatter(x=dffilt['Date'],
                        y=dfswap[vol1],
                        name=vol1+" Fwd",
                        yaxis='y2')
    trace5 = go.Scatter(x=dffilt['Date'],
                        y=dfdswap[vol],
                        name=vol + ' Realised Vol',
                        yaxis='y1')
    trace6 = go.Scatter(x=dffilt['Date'],
                        y=dfdswap[vol1],
                        name=vol1 + " Realised Vol",
                        yaxis='y1')
    data = [trace1, trace2, trace3, trace4, trace5, trace6]
    layout = go.Layout(yaxis=dict(title='Vol'),
                       yaxis2=dict(title='Fwd',
                                   overlaying='y',
                                   side='right'))
    fig2 = go.Figure(data=data, layout=layout)
    fig2.update_layout(
        font=dict(size=10))
    return fig2
#callback for diff graph
@callback(Output("fig14", "figure"),
          Input("vol-dropdown5", "value"),Input("vol-dropdown6", 'value'),
          Input('year-slider2', 'value'))
def update_figure(vol, vol1, selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    trace1 = go.Scatter(x=dffilt['Date'],
                        y=(dfvol[vol]-dfvol[vol1]),
                        name=vol+" - "+vol1+" Implied Vol",
                        yaxis='y1')
    trace2 = go.Scatter(x=dffilt['Date'],
                        y=(dfswap[vol]-dfswap[vol1]),
                        name=vol+" - "+vol1+" Fwd",
                        yaxis='y2')
    trace3 = go.Scatter(x=dffilt['Date'],
                        y=dfdswap[vol]-dfdswap[vol1],
                        name=vol+" - "+vol1+" Realised Vol",
                        yaxis='y1')
    data = [trace1, trace2, trace3]
    layout = go.Layout(yaxis=dict(title='Vol'),
                       yaxis2=dict(title='Fwd',
                                   overlaying='y',
                                   side='right'))
    fig2 = go.Figure(data=data, layout=layout)
    fig2.update_layout(
        font=dict(size=10))
    return fig2

#callback for three input fly graph
@callback(Output("fig15", "figure"),
          Input("vol-dropdown7", "value"),Input("vol-dropdown8", 'value'),
          Input("vol-dropdown9", 'value'),Input('year-slider3', 'value'))
def update_figure(vol, vol1, vol2, selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    trace1 = go.Scatter(x=dffilt['Date'],
                        y=dfvol[vol],
                        name=vol+" Implied Vol",
                        yaxis='y1')
    trace2 = go.Scatter(x=dffilt['Date'],
                        y=dfvol[vol1],
                        name=vol1+" Implied Vol",
                        yaxis='y1')
    trace3 = go.Scatter(x=dffilt['Date'],
                        y=dfvol[vol2],
                        name=vol2 + " Implied Vol",
                        yaxis='y1')
    trace4 = go.Scatter(x=dffilt['Date'],
                        y=dfswap[vol],
                        name=vol+' Fwd',
                        yaxis='y2')
    trace5 = go.Scatter(x=dffilt['Date'],
                        y=dfswap[vol1],
                        name=vol1+" Fwd",
                        yaxis='y2')
    trace6 = go.Scatter(x=dffilt['Date'],
                        y=dfswap[vol2],
                        name=vol2 + " Fwd",
                        yaxis='y2')
    trace7 = go.Scatter(x=dffilt['Date'],
                        y=dfdswap[vol],
                        name=vol + ' Realised Vol',
                        yaxis='y1')
    trace8 = go.Scatter(x=dffilt['Date'],
                        y=dfdswap[vol1],
                        name=vol1 + " Realised Vol",
                        yaxis='y1')
    trace9 = go.Scatter(x=dffilt['Date'],
                        y=dfdswap[vol2],
                        name=vol2 + " Realised Vol",
                        yaxis='y1')
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9]
    layout = go.Layout(yaxis=dict(title='Vol'),
                       yaxis2=dict(title='Fwd',
                                   overlaying='y',
                                   side='right'))
    fig2 = go.Figure(data=data, layout=layout)
    fig2.update_layout(
        font=dict(size=10))
    return fig2
#callback for fly diff graph
@callback(Output("fig16", "figure"),
          Input("vol-dropdown7", "value"),Input("vol-dropdown8", 'value'),
          Input("vol-dropdown9", 'value'),Input('year-slider3', 'value'))
def update_figure(vol, vol1, vol2, selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    trace1 = go.Scatter(x=dffilt['Date'],
                        y=(2*dfvol[vol1]-dfvol[vol]-dfvol[vol2]),
                        name=vol+" "+vol1+" "+vol2+" Imp Vol Fly",
                        yaxis='y1')
    trace2 = go.Scatter(x=dffilt['Date'],
                        y=(2*dfswap[vol1] - dfswap[vol] - dfswap[vol2]),
                        name=vol+" "+vol1+" " +vol2+" Fwd Fly",
                        yaxis='y2')
    trace3 = go.Scatter(x=dffilt['Date'],
                        y=(2*dfdswap[vol1]-dfdswap[vol]-dfdswap[vol2]),
                        name=vol+" "+vol1+" "+vol2+" Real Vol Fly",
                        yaxis='y1')
    data = [trace1, trace2, trace3]
    layout = go.Layout(yaxis=dict(title='Vol'),
                       yaxis2=dict(title='Fwd',
                                   overlaying='y',
                                   side='right'))
    fig2 = go.Figure(data=data, layout=layout)
    fig2.update_layout(
        font=dict(size=10))
    return fig2

dash.register_page(__name__)

layout = dbc.Container([
    dbc.Row([dbc.Col(html.Div('USD Historic Swap and Vol Data'))]),
    dbc.Row([dbc.Col(dropdown),
             dbc.Col(dropdown1)]),
    dbc.Row([dbc.Col(graph1),
             dbc.Col(graph2)]),
    dbc.Row([dbc.Col(slide1),
            dbc.Col(slide2)]),
    dbc.Row([dbc.Col(dropdown2),
            dbc.Col(dropdown3)]),
    dbc.Row([dbc.Col(graph3),
             dbc.Col(graph4)]),
    dbc.Row([dbc.Col(slide3)]),
    dbc.Row([dbc.Col(dropdown4),
            dbc.Col(dropdown5),
            dbc.Col(dropdown6)]),
    dbc.Row([dbc.Col(graph5),
             dbc.Col(graph6)]),
    dbc.Row([dbc.Col(slide4)])]
    ,fluid=True)
