import dash
import dash_ag_grid as dag
from dash import Dash, dcc, html, Input, Output, callback, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
from scipy import stats
import math as math

suppress_callback_exceptions=True
dash.register_page(__name__, path='/')

#implied vol
dfvol = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
dfvol = dfvol.tail(-1)
dfvol= dfvol.ffill()
dfvol = dfvol[dfvol.columns.drop('Year')]
dfvol =dfvol.stack(level=0)
dfvol = dfvol.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfvol = dfvol.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfvol=dfvol.round(0)
dfvol = dfvol.drop(index='9m', level=1)
dfvol = dfvol.drop(index='3y', level=1)
dfvol = dfvol.drop(index='7y', level=1)
dfvol = dfvol.drop(index='15y', level=1)
dfvol.columns = ["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"]
#new df so can use old one for vol surface graphs as need index
dfvol3 = dfvol.reset_index(level=1)
dfvol3 = dfvol3.reset_index(level=0)
dfvol3.columns = ["Date","Exp","1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"]
dfvol3['Date'] = pd.to_datetime(dfvol3['Date']).dt.date
dfvol3['Date'] = pd.to_datetime(dfvol3['Date']).dt.strftime('%d/%m/%y')

#implied vol zscore
dfzs = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
dfzs = dfzs.tail(-1)
dfzs= dfzs.ffill()
dfzs = dfzs[dfzs.columns.drop('Year')]
dfzs = dfzs.head(66)
dfzs = stats.zscore(dfzs)
dfzs =dfzs.stack(level=0)
dfzs = dfzs.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfzs = dfzs.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfzs=dfzs.round(1)
dfzs = dfzs.drop(index='9m', level=1)
dfzs = dfzs.drop(index='3y', level=1)
dfzs = dfzs.drop(index='7y', level=1)
dfzs = dfzs.drop(index='15y', level=1)
dfzs = dfzs.reset_index(level=1)
dfzs = dfzs.reset_index(level=0)
dfzs.columns = ["Date", "Exp","1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"]
dfzs['Date'] = pd.to_datetime(dfzs['Date']).dt.date
dfzs['Date'] = pd.to_datetime(dfzs['Date']).dt.strftime('%d/%m/%y')

#swaps
dfswap = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
dfswap = dfswap.tail(-1)
dfswap= dfswap.ffill()
dfswap = dfswap[dfswap.columns.drop('Year')]
dfswap =dfswap.stack(level=0)
dfswap = dfswap.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfswap = dfswap[dfswap.columns.drop('15y')]
dfswap = dfswap.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfswap=dfswap.round(2)
dfswap = dfswap.drop(index='9m', level=1)
dfswap = dfswap.drop(index='3y', level=1)
dfswap = dfswap.drop(index='7y', level=1)
dfswap = dfswap.drop(index='15y', level=1)
dfswap = dfswap.reset_index(level=1)
dfswap = dfswap.reset_index(level=0)
dfswap.columns = ["Date", "Exp","1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"]
dfswap['Date'] = pd.to_datetime(dfswap['Date']).dt.date
dfswap['Date'] = pd.to_datetime(dfswap['Date']).dt.strftime('%d/%m/%y')

#daily implied vol
dfdvol = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
dfdvol = dfdvol.tail(-1)
dfdvol= dfdvol.ffill()
dfdvol = dfdvol[dfdvol.columns.drop('Year')]
dfdvol = dfdvol.div(math.sqrt(252))
dfdvol2 =dfdvol.stack(level=0)
dfdvol2 = dfdvol2.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfdvol2 = dfdvol2.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfdvol2=dfdvol2.round(1)
dfdvol2 = dfdvol2.drop(index='9m', level=1)
dfdvol2 = dfdvol2.drop(index='3y', level=1)
dfdvol2 = dfdvol2.drop(index='7y', level=1)
dfdvol2 = dfdvol2.drop(index='15y', level=1)
dfdvol2 = dfdvol2.reset_index(level=1)
dfdvol2 = dfdvol2.reset_index(level=0)
dfdvol2.columns = ["Date", "Exp","1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"]
dfdvol2['Date'] = pd.to_datetime(dfdvol2['Date']).dt.date
dfdvol2['Date'] = pd.to_datetime(dfdvol2['Date']).dt.strftime('%d/%m/%y')

#realised swap vol
dfdswap = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
dfdswap = dfdswap.tail(-1)
dfdswap1 = dfdswap.head(-66)
index = dfdswap1.index
dfdswap= dfdswap.ffill()
dfdswap = dfdswap[dfdswap.columns.drop('Year')]
dfdswap = (dfdswap-dfdswap.shift(-1))*100
dfdswap = dfdswap.rolling(66).std()
dfdswap = dfdswap.dropna()
dfdswap =dfdswap.reset_index(drop=True)
dfdswap = dfdswap.assign(Date1=index)
dfdswap = dfdswap.set_index('Date1')
dfdswap2 =dfdswap.stack(level=0)
dfdswap2 = dfdswap2.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfdswap2 = dfdswap2[dfdswap2.columns.drop('15y')]
dfdswap2 = dfdswap2.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfdswap2=dfdswap2.round(1)
dfdswap2 = dfdswap2.drop(index='9m', level=1)
dfdswap2 = dfdswap2.drop(index='3y', level=1)
dfdswap2 = dfdswap2.drop(index='7y', level=1)
dfdswap2 = dfdswap2.drop(index='15y', level=1)
dfdswap2 = dfdswap2.reset_index(level=1)
dfdswap2 = dfdswap2.reset_index(level=0)
dfdswap2.columns = ["Date", "Exp","1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"]
dfdswap2['Date'] = pd.to_datetime(dfdswap2['Date']).dt.date
dfdswap2['Date'] = pd.to_datetime(dfdswap2['Date']).dt.strftime('%d/%m/%y')

#impliedrealisedratio
dfdvol1 = dfdvol.head(-66)
dfrat = dfdswap.div(dfdvol1)
dfrat=dfrat.sort_index(ascending=False)
dfrat =dfrat.stack(level=0)
dfrat = dfrat.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfrat = dfrat[dfrat.columns.drop('15y')]
dfrat = dfrat.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfrat=dfrat.round(2)
dfrat = dfrat.drop(index='9m', level=1)
dfrat = dfrat.drop(index='3y', level=1)
dfrat = dfrat.drop(index='7y', level=1)
dfrat = dfrat.drop(index='15y', level=1)
dfrat = dfrat.reset_index(level=1)
dfrat = dfrat.reset_index(level=0)
dfrat.columns = ["Date", "Exp","1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"]
dfrat['Date'] = pd.to_datetime(dfrat['Date']).dt.date
dfrat['Date'] = pd.to_datetime(dfrat['Date']).dt.strftime('%d/%m/%y')

#volsurface line graphs
dfsurf1 = dfvol.head(8)
dfsurf2 = dfvol[40:48]
dfsurf3 = dfvol[176:184]
dfsurf4 = pd.concat([dfsurf1, dfsurf2, dfsurf3])
dfsurf4 = dfsurf4.reset_index(level=1)
dfsurf4 = dfsurf4.reset_index(level=0)
dfsurf4.columns = ["Date", "Expiry", "1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"]
dfsurf4['Date'] = pd.to_datetime(dfsurf4['Date']).dt.date
dfsurf4['Date'] = pd.to_datetime(dfsurf4['Date']).dt.strftime('%d/%m/%y')

#1m lookback vol
dfvol1m = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
dfvol1m = dfvol1m.tail(-1)
dfvol1m= dfvol1m.ffill()
dfvol1m = dfvol1m[dfvol1m.columns.drop('Year')]
dfvol1m = (dfvol1m-dfvol1m.shift(-22))
dfvol1m =dfvol1m.stack(level=0)
dfvol1m = dfvol1m.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfvol1m = dfvol1m.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfvol1m=dfvol1m.round(0)
dfvol1m = dfvol1m.drop(index='9m', level=1)
dfvol1m = dfvol1m.drop(index='3y', level=1)
dfvol1m = dfvol1m.drop(index='7y', level=1)
dfvol1m = dfvol1m.drop(index='15y', level=1)
dfvol1m.columns = ["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"]
dfvol1m = dfvol1m.reset_index(level=1)
dfvol1m = dfvol1m.reset_index(level=0)
dfvol1m.columns = ["Date","Exp","1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"]
dfvol1m['Date'] = pd.to_datetime(dfvol1m['Date']).dt.date
dfvol1m['Date'] = pd.to_datetime(dfvol1m['Date']).dt.strftime('%d/%m/%y')

#1m lookback swap
dfswap1m = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
dfswap1m = dfswap1m.tail(-1)
dfswap1m= dfswap1m.ffill()
dfswap1m = dfswap1m[dfswap1m.columns.drop('Year')]
dfswap1m = (dfswap1m-dfswap1m.shift(-22))*100
dfswap1m =dfswap1m.stack(level=0)
dfswap1m = dfswap1m.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfswap1m = dfswap1m[dfswap1m.columns.drop('15y')]
dfswap1m = dfswap1m.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfswap1m=dfswap1m.round(0)
dfswap1m = dfswap1m.drop(index='9m', level=1)
dfswap1m = dfswap1m.drop(index='3y', level=1)
dfswap1m = dfswap1m.drop(index='7y', level=1)
dfswap1m = dfswap1m.drop(index='15y', level=1)
dfswap1m = dfswap1m.reset_index(level=1)
dfswap1m = dfswap1m.reset_index(level=0)
dfswap1m.columns = ["Date", "Exp","1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"]
dfswap1m['Date'] = pd.to_datetime(dfswap1m['Date']).dt.date
dfswap1m['Date'] = pd.to_datetime(dfswap1m['Date']).dt.strftime('%d/%m/%y')

#1m lookback realised vol
dfdswap1m = (dfdswap-dfdswap.shift(-22))
dfdswap1m =dfdswap1m.stack(level=0)
dfdswap1m = dfdswap1m.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfdswap1m = dfdswap1m[dfdswap1m.columns.drop('15y')]
dfdswap1m = dfdswap1m.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfdswap1m=dfdswap1m.round(1)
dfdswap1m = dfdswap1m.drop(index='9m', level=1)
dfdswap1m = dfdswap1m.drop(index='3y', level=1)
dfdswap1m = dfdswap1m.drop(index='7y', level=1)
dfdswap1m = dfdswap1m.drop(index='15y', level=1)
dfdswap1m = dfdswap1m.reset_index(level=1)
dfdswap1m = dfdswap1m.reset_index(level=0)
dfdswap1m.columns = ["Date", "Exp","1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"]
dfdswap1m['Date'] = pd.to_datetime(dfdswap1m['Date']).dt.date
dfdswap1m['Date'] = pd.to_datetime(dfdswap1m['Date']).dt.strftime('%d/%m/%y')

#3m lookback vol
dfvol3m = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
dfvol3m = dfvol3m.tail(-1)
dfvol3m= dfvol3m.ffill()
dfvol3m = dfvol3m[dfvol3m.columns.drop('Year')]
dfvol3m = (dfvol3m-dfvol3m.shift(-66))
dfvol3m =dfvol3m.stack(level=0)
dfvol3m = dfvol3m.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfvol3m = dfvol3m.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfvol3m=dfvol3m.round(0)
dfvol3m = dfvol3m.drop(index='9m', level=1)
dfvol3m = dfvol3m.drop(index='3y', level=1)
dfvol3m = dfvol3m.drop(index='7y', level=1)
dfvol3m = dfvol3m.drop(index='15y', level=1)
dfvol3m.columns = ["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"]
dfvol3m = dfvol3m.reset_index(level=1)
dfvol3m = dfvol3m.reset_index(level=0)
dfvol3m.columns = ["Date","Exp","1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"]
dfvol3m['Date'] = pd.to_datetime(dfvol3m['Date']).dt.date
dfvol3m['Date'] = pd.to_datetime(dfvol3m['Date']).dt.strftime('%d/%m/%y')

#3m lookback swap
dfswap3m = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
dfswap3m = dfswap3m.tail(-1)
dfswap3m= dfswap3m.ffill()
dfswap3m = dfswap3m[dfswap3m.columns.drop('Year')]
dfswap3m = (dfswap3m-dfswap3m.shift(-66))*100
dfswap3m =dfswap3m.stack(level=0)
dfswap3m = dfswap3m.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfswap3m = dfswap3m[dfswap3m.columns.drop('15y')]
dfswap3m = dfswap3m.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfswap3m=dfswap3m.round(0)
dfswap3m = dfswap3m.drop(index='9m', level=1)
dfswap3m = dfswap3m.drop(index='3y', level=1)
dfswap3m = dfswap3m.drop(index='7y', level=1)
dfswap3m = dfswap3m.drop(index='15y', level=1)
dfswap3m = dfswap3m.reset_index(level=1)
dfswap3m = dfswap3m.reset_index(level=0)
dfswap3m.columns = ["Date", "Exp","1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"]
dfswap3m['Date'] = pd.to_datetime(dfswap3m['Date']).dt.date
dfswap3m['Date'] = pd.to_datetime(dfswap3m['Date']).dt.strftime('%d/%m/%y')

#3m lookback realised vol
dfdswap3m = (dfdswap-dfdswap.shift(-66))
dfdswap3m =dfdswap3m.stack(level=0)
dfdswap3m = dfdswap3m.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfdswap3m = dfdswap3m[dfdswap3m.columns.drop('15y')]
dfdswap3m = dfdswap3m.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfdswap3m=dfdswap3m.round(1)
dfdswap3m = dfdswap3m.drop(index='9m', level=1)
dfdswap3m = dfdswap3m.drop(index='3y', level=1)
dfdswap3m = dfdswap3m.drop(index='7y', level=1)
dfdswap3m = dfdswap3m.drop(index='15y', level=1)
dfdswap3m = dfdswap3m.reset_index(level=1)
dfdswap3m = dfdswap3m.reset_index(level=0)
dfdswap3m.columns = ["Date", "Exp","1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"]
dfdswap3m['Date'] = pd.to_datetime(dfdswap3m['Date']).dt.date
dfdswap3m['Date'] = pd.to_datetime(dfdswap3m['Date']).dt.strftime('%d/%m/%y')

dropdown = html.Div([
    html.P("Select Tail to plot vol surface:"),
    dcc.Dropdown(
                    id="tail-dropdown",
                    clearable=False,
                    value="1y",
                    options=["1y", "2y", "3y", "5y", "7y"],
                    className="ag-theme-balham")
])

dropdown1 = html.Div([
    html.P("Select Tail to plot vol surface:"),
    dcc.Dropdown(
                    id="tail-dropdown1",
                    clearable=False,
                    value="10y",
                    options=["10y", "15y", "20y", "30y"],
                    className="ag-theme-balham")
])

surf1graph = dcc.Graph(id='surf1y',style={"height": 400, "width": 690, "font-size": '10px'})
surf2graph = dcc.Graph(id='surf10y', style={"height": 400, "width": 690, "font-size": '10px'})


@callback(Output("surf1y", "figure"), Input("tail-dropdown", "value"))
def update_figure(tail):
    return px.line(dfsurf4, x="Expiry", y=tail, color='Date')

@callback(Output("surf10y", "figure"), Input("tail-dropdown1", "value"))
def update_figure(tail):
    return px.line(dfsurf4, x="Expiry", y=tail, color='Date')

columnDefs = [
    {"field": "Date","minWidth": 65},
    {"field": "Exp", "minWidth": 15,"filter": False, "cellClass": "bg-info bg-gradient bg-opacity-15"},
    {"field": "1y","filter": False, "cellClass": "bg-warning bg-gradient bg-opacity-15"},
    {"field": "2y","filter": False, "cellClass": "bg-warning bg-gradient bg-opacity-15"},
    {"field": "3y","filter": False, "cellClass": "bg-warning bg-gradient bg-opacity-15"},
    {"field": "5y","filter": False, "cellClass": "bg-success bg-gradient bg-opacity-15"},
    {"field": "7y","filter": False, "cellClass": "bg-success bg-gradient bg-opacity-15"},
    {"field": "10y","filter": False, "cellClass": "bg-success bg-gradient bg-opacity-15"},
    #{"field": "15y","filter": False, "cellClass": "bg-danger bg-gradient bg-opacity-15"},
    {"field": "20y","filter": False, "cellClass": "bg-danger bg-gradient bg-opacity-15"},
    {"field": "30y","filter": False, "cellClass": "bg-danger bg-gradient bg-opacity-15"}
]

columnDefs1 = [
    {"field": "Date","minWidth": 65},
    {"field": "Exp", "minWidth": 20,"filter": False, "cellClass": "bg-info bg-gradient bg-opacity-15"},
    {"field": "1y","filter": False, 'cellStyle': {"styleConditions": [
                {"condition": "params.value >= 3", "style": {"backgroundColor": "#D62728"},},
                {"condition": "params.value >= 2","style": {"backgroundColor": "#EF553B"},},
                {"condition": "params.value >= 0.75","style": {"backgroundColor": "rgb(252,141,98)"},},
                {"condition": "params.value >= -0.75","style": {"backgroundColor": "rgb(230,245,201)"},},
                {"condition": "params.value >= -2","style": {"backgroundColor": "rgb(166,216,84)"},}],
            "defaultStyle": {"backgroundColor": "rgb(102,166,30)"},}},
    {"field": "2y","filter": False, 'cellStyle': {"styleConditions": [
                {"condition": "params.value >= 3", "style": {"backgroundColor": "#D62728"},},
                {"condition": "params.value >= 2","style": {"backgroundColor": "#EF553B"},},
                {"condition": "params.value >= 0.75","style": {"backgroundColor": "rgb(252,141,98)"},},
                {"condition": "params.value >= -0.75","style": {"backgroundColor": "rgb(230,245,201)"},},
                {"condition": "params.value >= -2","style": {"backgroundColor": "rgb(166,216,84)"},}],
            "defaultStyle": {"backgroundColor": "rgb(102,166,30)"},}},
    {"field": "3y","filter": False, 'cellStyle': {"styleConditions": [
                {"condition": "params.value >= 3", "style": {"backgroundColor": "#D62728"},},
                {"condition": "params.value >= 2","style": {"backgroundColor": "#EF553B"},},
                {"condition": "params.value >= 0.75","style": {"backgroundColor": "rgb(252,141,98)"},},
                {"condition": "params.value >= -0.75","style": {"backgroundColor": "rgb(230,245,201)"},},
                {"condition": "params.value >= -2","style": {"backgroundColor": "rgb(166,216,84)"},}],
            "defaultStyle": {"backgroundColor": "rgb(102,166,30)"},}},
    {"field": "5y","filter": False, 'cellStyle': {"styleConditions": [
                {"condition": "params.value >= 3", "style": {"backgroundColor": "#D62728"},},
                {"condition": "params.value >= 2","style": {"backgroundColor": "#EF553B"},},
                {"condition": "params.value >= 0.75","style": {"backgroundColor": "rgb(252,141,98)"},},
                {"condition": "params.value >= -0.75","style": {"backgroundColor": "rgb(230,245,201)"},},
                {"condition": "params.value >= -2","style": {"backgroundColor": "rgb(166,216,84)"},}],
            "defaultStyle": {"backgroundColor": "rgb(102,166,30)"},}},
    {"field": "7y","filter": False, 'cellStyle': {"styleConditions": [
                {"condition": "params.value >= 3", "style": {"backgroundColor": "#D62728"},},
                {"condition": "params.value >= 2","style": {"backgroundColor": "#EF553B"},},
                {"condition": "params.value >= 0.75","style": {"backgroundColor": "rgb(252,141,98)"},},
                {"condition": "params.value >= -0.75","style": {"backgroundColor": "rgb(230,245,201)"},},
                {"condition": "params.value >= -2","style": {"backgroundColor": "rgb(166,216,84)"},}],
            "defaultStyle": {"backgroundColor": "rgb(102,166,30)"},}},
    {"field": "10y","filter": False, 'cellStyle': {"styleConditions": [
                {"condition": "params.value >= 3", "style": {"backgroundColor": "#D62728"},},
                {"condition": "params.value >= 2","style": {"backgroundColor": "#EF553B"},},
                {"condition": "params.value >= 0.75","style": {"backgroundColor": "rgb(252,141,98)"},},
                {"condition": "params.value >= -0.75","style": {"backgroundColor": "rgb(230,245,201)"},},
                {"condition": "params.value >= -2","style": {"backgroundColor": "rgb(166,216,84)"},}],
            "defaultStyle": {"backgroundColor": "rgb(102,166,30)"},}},
    #{"field": "15y","filter": False, "cellClass": "bg-danger bg-gradient bg-opacity-15"},
    {"field": "20y","filter": False, 'cellStyle': {"styleConditions": [
                {"condition": "params.value >= 3", "style": {"backgroundColor": "#D62728"},},
                {"condition": "params.value >= 2","style": {"backgroundColor": "#EF553B"},},
                {"condition": "params.value >= 0.75","style": {"backgroundColor": "rgb(252,141,98)"},},
                {"condition": "params.value >= -0.75","style": {"backgroundColor": "rgb(230,245,201)"},},
                {"condition": "params.value >= -2","style": {"backgroundColor": "rgb(166,216,84)"},}],
            "defaultStyle": {"backgroundColor": "rgb(102,166,30)"},}},
    {"field": "30y","filter": False, 'cellStyle': {"styleConditions": [
                {"condition": "params.value >= 3", "style": {"backgroundColor": "#D62728"},},
                {"condition": "params.value >= 2","style": {"backgroundColor": "#EF553B"},},
                {"condition": "params.value >= 0.75","style": {"backgroundColor": "rgb(252,141,98)"},},
                {"condition": "params.value >= -0.75","style": {"backgroundColor": "rgb(230,245,201)"},},
                {"condition": "params.value >= -2","style": {"backgroundColor": "rgb(166,216,84)"},}],
            "defaultStyle": {"backgroundColor": "rgb(102,166,30)"},}},
]

columnDefs2 = [
    {"field": "Date","minWidth": 65},
    {"field": "Exp", "minWidth": 20,"filter": False, "cellClass": "bg-info bg-gradient bg-opacity-15"},
    {"field": "1y","filter": False, 'cellStyle': {"styleConditions": [
                {"condition": "params.value >= 1.5", "style": {"backgroundColor": "rgb(102,166,30)"},},
                {"condition": "params.value >= 1.2","style": {"backgroundColor": "rgb(166,216,84)"},},
                {"condition": "params.value >= 0.9","style": {"backgroundColor": "rgb(201,219,116)"},},
                {"condition": "params.value >= 0.7","style": {"backgroundColor": "rgb(252,141,98)"},}],
            "defaultStyle": {"backgroundColor": "#EF553B"},}},
    {"field": "2y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 1.5", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 1.2", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
    {"field": "3y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 1.5", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 1.2", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
    {"field": "5y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 1.5", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 1.2", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
    {"field": "7y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 1.5", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 1.2", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
    {"field": "10y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 1.5", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 1.2", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
    #{"field": "15y","filter": False, "cellClass": "bg-danger bg-gradient bg-opacity-15"},
    {"field": "20y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 1.5", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 1.2", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
        "defaultStyle": {"backgroundColor": "#EF553B"}, }},
    {"field": "30y","filter": False, 'cellStyle': {"styleConditions": [
        {"condition": "params.value >= 1.5", "style": {"backgroundColor": "rgb(102,166,30)"}, },
        {"condition": "params.value >= 1.2", "style": {"backgroundColor": "rgb(166,216,84)"}, },
        {"condition": "params.value >= 0.9", "style": {"backgroundColor": "rgb(201,219,116)"}, },
        {"condition": "params.value >= 0.7", "style": {"backgroundColor": "rgb(252,141,98)"}, }],
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
    rowData=dfvol3.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 460, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid2 = dag.AgGrid(
    id="quickstart-grid2",
    columnDefs=columnDefs,
    rowData=dfswap.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 470, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid3 = dag.AgGrid(
    id="quickstart-grid3",
    columnDefs=columnDefs1,
    rowData=dfzs.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 470, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid4 = dag.AgGrid(
    id="quickstart-grid4",
    columnDefs=columnDefs,
    rowData=dfdvol2.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 460, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)
grid5 = dag.AgGrid(
    id="quickstart-grid5",
    columnDefs=columnDefs,
    rowData=dfdswap2.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 470, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)
grid6 = dag.AgGrid(
    id="quickstart-grid6",
    columnDefs=columnDefs2,
    rowData=dfrat.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 470, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid7 = dag.AgGrid(
    id="quickstart-grid",
    columnDefs=columnDefs,
    rowData=dfvol1m.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 460, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid8 = dag.AgGrid(
    id="quickstart-grid",
    columnDefs=columnDefs,
    rowData=dfswap1m.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 460, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid9 = dag.AgGrid(
    id="quickstart-grid",
    columnDefs=columnDefs,
    rowData=dfdswap1m.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 460, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid10 = dag.AgGrid(
    id="quickstart-grid",
    columnDefs=columnDefs,
    rowData=dfvol3m.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 460, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid11 = dag.AgGrid(
    id="quickstart-grid",
    columnDefs=columnDefs,
    rowData=dfswap3m.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 460, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid12 = dag.AgGrid(
    id="quickstart-grid",
    columnDefs=columnDefs,
    rowData=dfdswap3m.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 460, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

layout = dbc.Container([
    dbc.Row([dbc.Col(html.Div('Implied Vol')),
             dbc.Col(html.Div('Fwd Rates')),
             dbc.Col(html.Div('3m Implied Vol Z-score'))]),
    dbc.Row([dbc.Col(grid),
            dbc.Col(grid2),
            dbc.Col(grid3)]),
    dbc.Row([dbc.Col(html.Div('Daily Implied Vol')),
             dbc.Col(html.Div('Daily Realised Vol 3m Lookback')),
             dbc.Col(html.Div('Realised/Implied'))]),
    dbc.Row([dbc.Col(grid4),
            dbc.Col(grid5),
            dbc.Col(grid6)]),
    dbc.Row([dbc.Col(dropdown),
             dbc.Col(dropdown1),]),
    dbc.Row([dbc.Col(surf1graph),
             dbc.Col(surf2graph)]),
    dbc.Row([dbc.Col(html.Div('Implied Vol - 1m Change (Norms)')),
             dbc.Col(html.Div('Fwd Rates - 1m Change (BPs)')),
             dbc.Col(html.Div('Daily Realised Vol (3m lookback) - 1m Change'))]),
    dbc.Row([dbc.Col(grid7),
            dbc.Col(grid8),
            dbc.Col(grid9)]),
    dbc.Row([dbc.Col(html.Div('Implied Vol - 3m Change (Norms)')),
             dbc.Col(html.Div('Fwd Rates - 3m Change (BPs)')),
             dbc.Col(html.Div('Daily Realised Vol (3m lookback) - 3m Change'))]),
    dbc.Row([dbc.Col(grid10),
            dbc.Col(grid11),
            dbc.Col(grid12)]),],fluid=True)
