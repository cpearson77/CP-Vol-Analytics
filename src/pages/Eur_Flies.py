import dash
from dash import Dash, dcc, html, Input, Output, callback
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd


dfswap = pd.read_excel(r"C:\Users\charl\Documents\master.xlsx", sheet_name='FwdFly',header=[0],index_col=[0])
dfswap = dfswap.tail(-1)
dfswap= dfswap.ffill()
dfswap.index.rename('Date', inplace=True)
dfswap = dfswap.reset_index(level=0)
dfswap['Year'] = dfswap['Year'].astype('int64')
dfswap["Year"]=dfswap["Year"].round(0)

dfvol = pd.read_excel(r"C:\Users\charl\Documents\master.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
dfvol.columns = dfvol.columns.map(''.join)
dfvol = dfvol.tail(-1)
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
dfvol = dfvol.reset_index(level=0)
dfvol['Year'] = dfvol['Year'].astype('int64')
dfvol["Year"]=dfvol["Year"].round(0)

flygraph = dcc.Graph(id='fly',style={"height": 350, "width": 400})
fly1graph = dcc.Graph(id='fly1',style={"height": 350, "width": 400})
fly2graph = dcc.Graph(id='fly2',style={"height": 350, "width": 400})
fly3graph = dcc.Graph(id='fly3',style={"height": 350, "width": 400})
fly4graph = dcc.Graph(id='fly4',style={"height": 350, "width": 400})
fly5graph = dcc.Graph(id='fly5',style={"height": 350, "width": 400})
fly6graph = dcc.Graph(id='fly6',style={"height": 350, "width": 400})
fly7graph = dcc.Graph(id='fly7',style={"height": 350, "width": 400})
fly8graph = dcc.Graph(id='fly8',style={"height": 350, "width": 400})
fly9graph = dcc.Graph(id='fly9',style={"height": 350, "width": 400})
fly10graph = dcc.Graph(id='fly10',style={"height": 350, "width": 400})
fly11graph = dcc.Graph(id='fly11',style={"height": 350, "width": 400})
fly12graph = dcc.Graph(id='fly12',style={"height": 350, "width": 400})
fly13graph = dcc.Graph(id='fly13',style={"height": 350, "width": 400})
fly14graph = dcc.Graph(id='fly14',style={"height": 350, "width": 400})
fly15graph = dcc.Graph(id='fly15',style={"height": 350, "width": 400})
fly16graph = dcc.Graph(id='fly16',style={"height": 350, "width": 400})
fly17graph = dcc.Graph(id='fly17',style={"height": 350, "width": 400})
fly18graph = dcc.Graph(id='fly18',style={"height": 350, "width": 400})
fly19graph = dcc.Graph(id='fly19',style={"height": 350, "width": 400})
fly20graph = dcc.Graph(id='fly20',style={"height": 350, "width": 400})
fly21graph = dcc.Graph(id='fly21',style={"height": 350, "width": 400})
fly22graph = dcc.Graph(id='fly22',style={"height": 350, "width": 400})
fly23graph = dcc.Graph(id='fly23',style={"height": 350, "width": 400})
fly24graph = dcc.Graph(id='fly24',style={"height": 350, "width": 400})

slide1 = html.Div([
    html.P("Select Lookback:"),
    dcc.Slider(
        dfswap['Year'].min(),
        dfswap['Year'].max(),
        step=None,
        value=dfswap['Year'].max(),
        marks={str(year): str(year) for year in dfswap['Year'].unique()},
        id='year-slider'),
])

@callback(Output("fly", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["1y1y"] - dffilt["1y"] - dffilt["2y1y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="1y 1y1y 2y1y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly1", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["2y1y"] - dffilt["1y1y"] - dffilt["3y1y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="1y1y 2y1y 3y1y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly2", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["3y1y"] - dffilt["2y1y"] - dffilt["4y1y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="2y1y 3y1y 4y1y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly3", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["4y1y"] - dffilt["3y1y"] - dffilt["5y1y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="3y1y 4y1y 5y1y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly4", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["5y1y"] - dffilt["4y1y"] - dffilt["6y1y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="4y1y 5y1y 6y1y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly5", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["6y1y"] - dffilt["5y1y"] - dffilt["7y1y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="5y1y 6y1y 7y1y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly6", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["7y1y"] - dffilt["6y1y"] - dffilt["8y1y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="6y1y 7y1y 8y1y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly7", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["8y1y"] - dffilt["7y1y"] - dffilt["9y1y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="7y1y 8y1y 9y1y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly8", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["5y5y"] - dffilt["5y"] - dffilt["10y5y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="5y 5y5y 10y5y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly9", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["10y5y"] - dffilt["5y5y"] - dffilt["15y5y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="5y5y 10y5y 15y5y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly10", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["15y5y"] - dffilt["10y5y"] - dffilt["20y5y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="10y5y 15y5y 20y5y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly11", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["20y5y"] - dffilt["15y5y"] - dffilt["25y5y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="15y5y 20y5y 25y5y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly12", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfswap[dfswap.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["25y5y"] - dffilt["20y5y"] - dffilt["30y5y"]),
                  labels={
                      "x": "Date",
                      "y": "Fwd"},
                  title="20y5y 25y5y 30y5y Fwd fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly13", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["1y5y"] - dffilt["1y2y"] - dffilt["1y10y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="1y2y 1y5y 1y10y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly14", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["1y10y"] - dffilt["1y5y"] - dffilt["1y30y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="1y5y 1y10y 1y30y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly15", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["1y20y"] - dffilt["1y10y"] - dffilt["1y30y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="1y10y 1y20y 1y30y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly16", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["2y5y"] - dffilt["2y2y"] - dffilt["2y10y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="2y2y 2y5y 2y10y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly17", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["2y10y"] - dffilt["2y5y"] - dffilt["2y30y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="2y5y 2y10y 2y30y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly18", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["2y20y"] - dffilt["2y10y"] - dffilt["2y30y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="2y10y 2y20y 2y30y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly19", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["5y5y"] - dffilt["5y2y"] - dffilt["5y10y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="5y2y 5y5y 5y10y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly20", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["5y10y"] - dffilt["5y5y"] - dffilt["5y30y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="5y5y 5y10y 5y30y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly21", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["5y20y"] - dffilt["5y10y"] - dffilt["5y30y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="5y10y 5y20y 5y30y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly22", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["10y5y"] - dffilt["10y2y"] - dffilt["10y10y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="10y2y 10y5y 10y10y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly23", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["10y10y"] - dffilt["10y5y"] - dffilt["10y30y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="10y5y 10y10y 10y30y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

@callback(Output("fly24", "figure"),
          Input('year-slider', 'value'))
def update_figure(selected_year):
    dffilt = dfvol[dfvol.Year >= selected_year]
    fly = px.line(dffilt, x=dffilt["Date"], y=(2 * dffilt["10y20y"] - dffilt["10y10y"] - dffilt["10y30y"]),
                  labels={
                      "x": "Date",
                      "y": "Vol"},
                  title="10y10y 10y20y 10y30y Vol fly")
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

dash.register_page(__name__)
layout = dbc.Container([
         dbc.Row([dbc.Col(slide1)]),
         dbc.Row([dbc.Col(fly13graph),
                  dbc.Col(fly14graph),
                  dbc.Col(fly15graph)]),
         dbc.Row([dbc.Col(fly16graph),
                  dbc.Col(fly17graph),
                  dbc.Col(fly18graph)]),
         dbc.Row([dbc.Col(fly19graph),
                  dbc.Col(fly20graph),
                  dbc.Col(fly21graph)]),
         dbc.Row([dbc.Col(fly22graph),
                  dbc.Col(fly23graph),
                  dbc.Col(fly24graph)]),
         dbc.Row([dbc.Col(fly8graph),
                  dbc.Col(fly9graph),
                  dbc.Col(fly10graph)]),
         dbc.Row([dbc.Col(fly11graph),
                  dbc.Col(fly12graph),
                  dbc.Col(flygraph)]),
         dbc.Row([dbc.Col(fly1graph),
                  dbc.Col(fly2graph),
                  dbc.Col(fly3graph)]),
         dbc.Row([dbc.Col(fly4graph),
                  dbc.Col(fly5graph),
                  dbc.Col(fly6graph)]),
         dbc.Row([dbc.Col(fly7graph),
                  ])
],fluid=True)

