import dash
from dash import Dash, dcc, html, Input, Output, callback
from dash.dependencies import Input, Output
import dash_ag_grid as dag
import plotly.express as px
from dash import html
import dash_bootstrap_components as dbc
from dash import html
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
import math as math
import dash_bootstrap_components as dbc

suppress_callback_exceptions=True
dash.register_page(__name__)

#grid of corr 22d lookback
#index adjusted by 6 x (no of days -1)
dfswap = pd.read_excel(r"C:\Users\charl\Documents\master.xlsx", sheet_name='Swaps',header=[0],index_col=[0])
dfswap = dfswap.tail(-1)
dfswap.index.rename('Date', inplace=True)
dfswap= dfswap.ffill()
dfswap1 = (dfswap-dfswap.shift(-1))*100
dfswap1 = dfswap1.head(-1)
dfswap2 = dfswap1.rolling(22).corr()
dfswap3 = dfswap2.head(-126)
dfswap3 =dfswap3.reset_index(level=1)
index = dfswap3.index
dfswap4= dfswap2.dropna()
dfswap4=dfswap4.reset_index(level=1)
dfswap4=dfswap4.reset_index(drop=True)
dfswap4= dfswap4.assign(Date=index)
dfswap4= dfswap4.set_index('Date')
dfswap4=dfswap4.reset_index(level =0)
dfswap4.columns = ["Date", "Swap", "1y", "2y", "5y", "10y", "20y", "30y"]
dfswap4=dfswap4.round(2)
dfswap4['Date'] = pd.to_datetime(dfswap4['Date']).dt.date
dfswap4['Date'] = pd.to_datetime(dfswap4['Date']).dt.strftime('%d/%m/%y')

#grid of corr 66d lookback
dfswap5 = dfswap1.rolling(66).corr()
dfswap6 = dfswap5.head(-390)
dfswap6 =dfswap6.reset_index(level=1)
index = dfswap6.index
dfswap7= dfswap5.dropna()
dfswap7=dfswap7.reset_index(level=1)
dfswap7=dfswap7.reset_index(drop=True)
dfswap7= dfswap7.assign(Date=index)
dfswap7= dfswap7.set_index('Date')
dfswap7=dfswap7.reset_index(level =0)
dfswap7.columns = ["Date", "Swap", "1y", "2y", "5y", "10y", "20y", "30y"]
dfswap7=dfswap7.round(2)
dfswap7['Date'] = pd.to_datetime(dfswap7['Date']).dt.date
dfswap7['Date'] = pd.to_datetime(dfswap7['Date']).dt.strftime('%d/%m/%y')

#grid of corr 132d lookback
dfswap8 = dfswap1.rolling(132).corr()
dfswap9 = dfswap8.head(-786)
dfswap9 =dfswap9.reset_index(level=1)
index = dfswap9.index
dfswap10= dfswap8.dropna()
dfswap10=dfswap10.reset_index(level=1)
dfswap10=dfswap10.reset_index(drop=True)
dfswap10= dfswap10.assign(Date=index)
dfswap10= dfswap10.set_index('Date')
dfswap10=dfswap10.reset_index(level =0)
dfswap10.columns = ["Date", "Swap", "1y", "2y", "5y", "10y", "20y", "30y"]
dfswap10=dfswap10.round(2)
dfswap10['Date'] = pd.to_datetime(dfswap10['Date']).dt.date
dfswap10['Date'] = pd.to_datetime(dfswap10['Date']).dt.strftime('%d/%m/%y')

#df for graphs 3m lookback
dfc1 = dfswap1["1y"].rolling(66).corr(dfswap1["2y"])
dfc2 = dfswap1["1y"].rolling(66).corr(dfswap1["5y"])
dfc3 = dfswap1["1y"].rolling(66).corr(dfswap1["10y"])
dfc4 = dfswap1["1y"].rolling(66).corr(dfswap1["20y"])
dfc5 = dfswap1["1y"].rolling(66).corr(dfswap1["30y"])
dfc6 = dfswap1["2y"].rolling(66).corr(dfswap1["5y"])
dfc7 = dfswap1["2y"].rolling(66).corr(dfswap1["10y"])
dfc8 = dfswap1["2y"].rolling(66).corr(dfswap1["20y"])
dfc9 = dfswap1["2y"].rolling(66).corr(dfswap1["30y"])
dfc10 = dfswap1["5y"].rolling(66).corr(dfswap1["10y"])
dfc11 = dfswap1["5y"].rolling(66).corr(dfswap1["20y"])
dfc12 = dfswap1["5y"].rolling(66).corr(dfswap1["30y"])
dfc13 = dfswap1["10y"].rolling(66).corr(dfswap1["20y"])
dfc14 = dfswap1["10y"].rolling(66).corr(dfswap1["30y"])
dfc15 = dfswap1["20y"].rolling(66).corr(dfswap1["30y"])
dfcorr = pd.concat([dfc1, dfc2, dfc3, dfc4, dfc5, dfc6, dfc7, dfc8, dfc9, dfc10, dfc11, dfc12, dfc13, dfc14, dfc15],
                    axis=1)
dfcorr1 = dfcorr.head(-65)
index = dfcorr1.index
dfcorr2= dfcorr.dropna()
#dfswap4=dfswap4.reset_index(level=1)
dfcorr2=dfcorr2.reset_index(drop=True)
dfcorr2= dfcorr2.assign(Date=index)
dfcorr2= dfcorr2.set_index('Date')
dfcorr2= dfcorr2.reset_index(level=0)
dfcorr2.columns = ["Date", "1s2s", "1s5s", "1s10s", "1s20s", "1s30s", "2s5s", "2s10s", "2s20s", "2s30s", "5s10s", "5s20s", "5s30s",
                  "10s20s", "10s30s", "20s30s"]
dfcorr2=dfcorr2.round(2)
dfyear = dfcorr2["Date"].dt.year
dfcorr3 = pd.concat([dfcorr2, dfyear], axis=1)
dfcorr3.columns = ["Date", "1s2s", "1s5s", "1s10s", "1s20s", "1s30s", "2s5s", "2s10s", "2s20s", "2s30s", "5s10s", "5s20s", "5s30s",
                  "10s20s", "10s30s", "20s30s", "Year"]
dfcorr3['Date'] = pd.to_datetime(dfcorr3['Date']).dt.date
dfcorr3['Date'] = pd.to_datetime(dfcorr3['Date']).dt.strftime('%d/%m/%y')
dfcorr3['Year'] = dfcorr3['Year'].astype('int64')
dfcorr3["Year"]=dfcorr3["Year"].round(0)

columnDefs = [
    {"field": "Date","minWidth": 65},
    {"field": "Swap", "minWidth": 15,"filter": False, "cellClass": "bg-info bg-gradient bg-opacity-15"},
    {"field": "1y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.5", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.2", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
    {"field": "2y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.5", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.2", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
    {"field": "5y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.5", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.2", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
    {"field": "10y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.5", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.2", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
    {"field": "20y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.5", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.2", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
    {"field": "30y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.5", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.2", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
   ]

defaultColDef = {
    "flex": 1,
    "minWidth": 10,
    "filter": True,
    "floatingFilter": True,
    "resizable": True,
}

grid = dag.AgGrid(
    id="quickstart-grid",
    columnDefs=columnDefs,
    rowData=dfswap4.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 220, "width": 450, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid1 = dag.AgGrid(
    id="quickstart-grid1",
    columnDefs=columnDefs,
    rowData=dfswap7.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 220, "width": 450, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid2 = dag.AgGrid(
    id="quickstart-grid1",
    columnDefs=columnDefs,
    rowData=dfswap10.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 220, "width": 450, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

graph = dcc.Graph(id='fig',style={"height": 500, "width": 1300})

dropdown = html.Div([
    html.P("Select Swap Correlation to plot:"),
    dcc.Dropdown(
                    id="swap-dropdown",
                    clearable=False,
                    value="5s10s",
                    options=["1s2s", "1s5s", "1s10s", "1s20s", "1s30s", "2s5s", "2s10s", "2s20s", "2s30s", "5s10s", "5s20s", "5s30s",
                  "10s20s","10s30s", "20s30s"],
                    className="ag-theme-balham")
                    #style={"height": 20, "width": 100})
])

dropdown1 = html.Div([
    html.P("Select Swap Correlation to plot:"),
    dcc.Dropdown(
                    id="swap-dropdown1",
                    clearable=False,
                    value="10s30s",
                    options=["1s2s", "1s5s", "1s10s", "1s20s", "1s30s", "2s5s", "2s10s", "2s20s", "2s30s", "5s10s", "5s20s", "5s30s",
                  "10s20s","10s30s", "20s30s"],
                    className="ag-theme-balham")
                    #style={"height": 20, "width": 100})
])

dropdown2 = html.Div([
    html.P("Select Swap Correlation to plot:"),
    dcc.Dropdown(
                    id="swap-dropdown2",
                    clearable=False,
                    value="2s10s",
                    options=["1s2s", "1s5s", "1s10s", "1s20s", "1s30s", "2s5s", "2s10s", "2s20s", "2s30s", "5s10s", "5s20s", "5s30s",
                  "10s20s","10s30s", "20s30s"],
                    className="ag-theme-balham")
                    #style={"height": 20, "width": 100})
])

slide = html.Div([
    html.P("Select Lookback:"),
    dcc.Slider(
        dfcorr3['Year'].min(),
        dfcorr3['Year'].max(),
        step=None,
        value=dfcorr3['Year'].min(),
        marks={str(year): str(year) for year in dfcorr3['Year'].unique()},
        id='year-slider'),
])

@callback(Output("fig", "figure"),
          Input("swap-dropdown", "value"),Input("swap-dropdown1", "value"),
          Input("swap-dropdown2", "value"),Input('year-slider', 'value'))
def update_figure(pair, pair1, pair2, selected_year):
    dffilt = dfcorr3[dfcorr3.Year >= selected_year]
    #return px.line(dfcorr2, x="Date", y=pair)
    trace1 = go.Scatter(x=dffilt['Date'],
                        y=dffilt[pair],
                        name=pair + ' Corr',
                        yaxis='y1')
    trace2 = go.Scatter(x=dffilt['Date'],
                        y=dffilt[pair1],
                        name=pair1 + ' Corr',
                        yaxis='y1')
    trace3 = go.Scatter(x=dffilt['Date'],
                        y=dffilt[pair2],
                        name=pair2 + ' Corr',
                        yaxis='y1')
    trace4 = go.Scatter(x=dffilt['Date'],
                        y=dfswap['1y'],
                        name='1y',
                        yaxis='y2')
    trace5 = go.Scatter(x=dffilt['Date'],
                        y=dfswap['2y'],
                        name='2y',
                        yaxis='y2')
    trace6 = go.Scatter(x=dffilt['Date'],
                        y=dfswap['5y'],
                        name='5y',
                        yaxis='y2')
    trace7 = go.Scatter(x=dffilt['Date'],
                        y=dfswap['10y'],
                        name='10y',
                        yaxis='y2')
    trace8 = go.Scatter(x=dffilt['Date'],
                        y=dfswap['20y'],
                        name='20y',
                        yaxis='y2')
    trace9 = go.Scatter(x=dffilt['Date'],
                        y=dfswap['30y'],
                        name='30y',
                        yaxis='y2')
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9]
    layout = go.Layout(yaxis=dict(title='Corr'),
                       yaxis2=dict(title='Swap',
                                   overlaying='y',
                                   side='right'))

    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(
        font=dict(size=10),
        xaxis = dict(autorange="reversed"))
    return fig


layout = dbc.Container([
         dbc.Row([dbc.Col(html.P("1m correlation lookback")),
                  dbc.Col(html.P("3m correlation lookback")),
                  dbc.Col(html.P("6m correlation lookback"))]),
         dbc.Row([dbc.Col(grid),
                  dbc.Col(grid1),
                  dbc.Col(grid2)]),
         dbc.Row([dbc.Col(dropdown),
                  dbc.Col(dropdown1),
                  dbc.Col(dropdown2)]),
         dbc.Row([dbc.Col(graph)]),
         dbc.Row([dbc.Col(slide)]),
         ],fluid=True)