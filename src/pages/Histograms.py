import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd


url = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fwdgrid1.csv?raw=true'
dfswap = pd.read_csv(url,header=[0,1],index_col=0)
dfswap.columns = dfswap.columns.map(''.join)
dfswap = dfswap.tail(-1)
dfswap= dfswap.ffill()
cols = dfswap.columns
#cols.remove('fistcolumn')
for col in cols:
    dfswap[col] = dfswap[col].astype(float)
dfswap=dfswap.round(4)
dfswap.columns = ["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y","3m1y", "3m2y",
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

url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/ufwdgrid1.csv?raw=true'
dfuswap = pd.read_csv(url1,header=[0,1],index_col=0)
dfuswap.columns = dfuswap.columns.map(''.join)
dfuswap = dfuswap.tail(-1)
dfuswap = dfuswap.head(1200)
dfuswap= dfuswap.ffill()
cols1 = dfuswap.columns
#cols.remove('fistcolumn')
for col in cols1:
    dfuswap[col] = dfuswap[col].astype(float)
dfuswap=dfuswap.round(2)
dfuswap.columns = ["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y","3m1y", "3m2y",
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
dfuswap.index.rename('Date', inplace=True)
dfuswap = dfuswap.reset_index(level=0)
dfuswap1 = dfuswap.reset_index(level=0)
dfuswap= dfuswap.ffill()
dfuswap1= dfuswap.ffill()
dfuswap['Date'] = pd.to_datetime(dfuswap['Date'], format='%d/%m/%Y')
dfuswap1['Date'] = pd.to_datetime(dfuswap1['Date'], format='%d/%m/%Y')
dfuswap['Year'] = dfuswap['Year'].astype('int64')
dfuswap["Year"]=dfuswap["Year"].round(0)

url2 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/volgrid1.csv?raw=true'
dfvol = pd.read_csv(url2,header=[0,1],index_col=0)
dfvol.columns = dfvol.columns.map(''.join)
dfvol = dfvol.tail(-1)
dfvol= dfvol.ffill()
cols2 = dfvol.columns
#cols.remove('fistcolumn')
for col in cols2:
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
dfvol1 = dfvol.set_index('Date')
dfvol1=dfvol1.round(1)
dfyear = dfvol["Date"].dt.year
dfvol2 = pd.concat([dfvol, dfyear], axis=1)
dfvol2.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
#dfcorr3['Date'] = pd.to_datetime(dfcorr3['Date']).dt.date
#dfcorr3['Date'] = pd.to_datetime(dfcorr3['Date']).dt.strftime('%d/%m/%y')
dfvol2 = dfvol2.dropna()
dfvol2['Year'] = dfvol2['Year'].astype('int64')
dfvol2["Year"]=dfvol2["Year"].round(0)
dfvol2 = dfvol2.set_index('Date')
dfvol2=dfvol2.round(1)

url3 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/uvolgrid1.csv?raw=true'
dfuvol = pd.read_csv(url3,header=[0,1],index_col=0)
dfuvol.columns = dfuvol.columns.map(''.join)
dfuvol = dfuvol.tail(-1)
dfuvol= dfuvol.ffill()
cols3 = dfuvol.columns
#cols.remove('fistcolumn')
for col in cols3:
    dfuvol[col] = dfuvol[col].astype(float)
dfuvol = dfuvol[dfuvol.columns.drop('YearUnnamed: 109_level_1')]
dfuvol = dfuvol.reset_index(level=0)
dfuvol.columns = ["Date","1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfuvol['Date'] = pd.to_datetime(dfuvol['Date'], format='%d/%m/%Y')
dfuvol1 = dfuvol.set_index('Date')
dfuvol1=dfuvol1.round(1)
#dfuvol1 = dfuvol.head(-66)
dfuyear = dfuvol["Date"].dt.year
dfuvol2 = pd.concat([dfuvol, dfuyear], axis=1)
dfuvol2.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
#dfcorr3['Date'] = pd.to_datetime(dfcorr3['Date']).dt.date
#dfcorr3['Date'] = pd.to_datetime(dfcorr3['Date']).dt.strftime('%d/%m/%y')
dfuvol2 = dfuvol2.dropna()
dfuvol2['Year'] = dfuvol2['Year'].astype('int64')
dfuvol2["Year"]=  dfuvol2["Year"].round(0)
dfuvol2 = dfuvol2.set_index('Date')
dfuvol2=dfuvol2.round(1)

dropdownccy = html.Div([
    dcc.Dropdown(
                    id="vol-dropdownccy",
                    clearable=False,
                    value="EUR",
                    options=["EUR", "USD"],
                    className="ag-theme-balham",
                    style={"height": 30, "width": 70})
])


dropdown = html.Div([
    dcc.Dropdown(
                    id="vol-dropdown",
                    clearable=False,
                    value="1y1y",
                    options=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y", "1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y", "2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y","10y1y", "10y2y", "10y5y", "10y10y", "10y15y", "10y20y", "10y30y",
                             "15y1y", "15y2y", "15y5y",
                          "15y10y", "15y15y", "15y20y", "15y30y", "20y1y", "20y2y", "20y5y",
                          "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham",
                    style={"height": 38, "width": 100})
])

dropdown1 = html.Div([
    dcc.Dropdown(
                    id="vol-dropdown1",
                    clearable=False,
                    value="10y10y",
                    options=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y", "1y1y", "1y2y", "1y5y", "1y10y","1y20y", "1y30y", "2y1y", "2y2y", "2y5y",
                          "2y10y", "2y20y", "2y30y","3y1y", "3y2y", "3y5y",
                          "3y10y", "3y20y", "3y30y","5y1y", "5y2y", "5y5y", "5y10y", "5y20y", "5y30y",
                          "7y1y", "7y2y", "7y5y","7y10y", "7y20y", "7y30y","10y1y", "10y2y", "10y5y", "10y10y", "10y15y", "10y20y", "10y30y",
                             "15y1y", "15y2y", "15y5y",
                          "15y10y", "15y15y", "15y20y", "15y30y", "20y1y", "20y2y", "20y5y",
                          "20y10y", "20y15y", "20y20y", "20y30y"],
                    className="ag-theme-balham",
                    style={"height": 38, "width": 100})
])

hist1graph = dcc.Graph(id='hist1',style={"height": 450, "width": 710,"font-size": '10px'})
hist2graph = dcc.Graph(id='hist2',style={"height": 450, "width": 710,"font-size": '10px'})
hist3graph = dcc.Graph(id='hist3',style={"height": 450, "width": 710,"font-size": '10px'})
hist4graph = dcc.Graph(id='hist4',style={"height": 450, "width": 710,"font-size": '10px'})
hist5graph = dcc.Graph(id='hist5',style={"height": 450, "width": 710,"font-size": '10px'})
hist6graph = dcc.Graph(id='hist6',style={"height": 450, "width": 710,"font-size": '10px'})
hist7graph = dcc.Graph(id='hist7',style={"height": 450, "width": 710,"font-size": '10px'})
hist8graph = dcc.Graph(id='hist8',style={"height": 450, "width": 710,"font-size": '10px'})

@callback(Output("hist1", "figure"), Input("vol-dropdown", "value"),
          Input("vol-dropdownccy", "value"))
def update_figure(vol1, ccy):
    #dffilt = dfswap[dfswap1.Year >= selected_year]
    if ccy == "EUR":
        fig = px.histogram(dfswap, x=vol1,nbins=150,histnorm='percent',
                    title=ccy+' ' + vol1 +' Swap Rates')
        fig.update_layout(font=dict(size=10))
        return fig
    else:
        fig = px.histogram(dfuswap, x=vol1, nbins=150, histnorm='percent',
                    title=ccy+' ' + vol1 +' Swap Rates')
        fig.update_layout(
            font=dict(size=10))
        return fig

@callback(Output("hist3", "figure"), Input("vol-dropdown", "value"),
          Input("vol-dropdownccy", "value"))
def update_figure(vol1, ccy):
    #dffilt = dfswap[dfswap1.Year >= selected_year]
    if ccy == "EUR":
        fig1 = px.histogram(dfswap, x=vol1,nbins=150,histnorm='percent', color = 'Year',title=ccy+' ' + vol1 +' Swap Rates')
        fig1.update_layout(font=dict(size=10))
        return fig1
    else:
        fig1 = px.histogram(dfuswap, x=vol1, nbins=150, histnorm='percent', color ='Year',title=ccy+' ' + vol1 +' Swap Rates')
        fig1.update_layout(font=dict(size=10))
        return fig1

@callback(Output("hist5", "figure"), Input("vol-dropdown", "value"),
          Input("vol-dropdownccy", "value"))
def update_figure(vol1, ccy):
    #dffilt = dfswap[dfswap1.Year >= selected_year]
    if ccy == "EUR":
        fig2 = px.histogram(dfvol2, x=vol1, nbins=150,histnorm='percent',title=ccy+' ' + vol1 +' Norm Vol')
        fig2.update_layout(font=dict(size=10))
        return fig2
    else:
        fig2 = px.histogram(dfuvol2, x=vol1, nbins=150, histnorm='percent',title=ccy+' ' + vol1 +' Norm Vol')
        fig2.update_layout(font=dict(size=10))
        return fig2
@callback(Output("hist6", "figure"), Input("vol-dropdown", "value"),
          Input("vol-dropdownccy", "value"))
def update_figure(vol1, ccy):
    #dffilt = dfswap[dfswap1.Year >= selected_year]
    if ccy == "EUR":
        fig3 = px.histogram(dfvol2, x=vol1, nbins=150,histnorm='percent', color = 'Year',title=ccy+' ' + vol1 +' Norm Vol')
        fig3.update_layout(font=dict(size=10))
        return fig3
    else:
        fig3 = px.histogram(dfuvol2, x=vol1, nbins=150, histnorm='percent', color = 'Year',title=ccy+' ' + vol1 +' Norm Vol')
        fig3.update_layout(font=dict(size=10))
        return fig3
@callback(Output("hist2", "figure"), Input("vol-dropdown1", "value"),
          Input("vol-dropdownccy", "value"))
def update_figure(vol1, ccy):
    #dffilt = dfswap[dfswap1.Year >= selected_year]
    if ccy == "EUR":
        fig4 = px.histogram(dfswap, x=vol1,nbins=150,histnorm='percent',title=ccy+' ' + vol1 +' Swap Rates')
        fig4.update_layout(font=dict(size=10))
        return fig4
    else:
        fig4= px.histogram(dfuswap, x=vol1, nbins=150, histnorm='percent',title=ccy+' ' + vol1 +' Swap Rates')
        fig4.update_layout(font=dict(size=10))
        return fig4
@callback(Output("hist4", "figure"), Input("vol-dropdown1", "value"),
          Input("vol-dropdownccy", "value"))
def update_figure(vol1, ccy):
    #dffilt = dfswap[dfswap1.Year >= selected_year]
    if ccy == "EUR":
        fig5 = px.histogram(dfswap, x=vol1,nbins=150,histnorm='percent', color = 'Year',title=ccy+' ' + vol1 +' Swap Rates')
        fig5.update_layout(font=dict(size=10))
        return fig5
    else:
        fig5 = px.histogram(dfuswap, x=vol1, nbins=150, histnorm='percent', color ='Year',title=ccy+' ' + vol1 +' Swap Rates')
        fig5.update_layout(font=dict(size=10))
        return fig5
@callback(Output("hist7", "figure"), Input("vol-dropdown1", "value"),
          Input("vol-dropdownccy", "value"))
def update_figure(vol1, ccy):
    #dffilt = dfswap[dfswap1.Year >= selected_year]
    if ccy == "EUR":
        fig6 = px.histogram(dfvol2, x=vol1,nbins=150,histnorm='percent',title=ccy+' ' + vol1 +' Norm Vol')
        fig6.update_layout(font=dict(size=10))
        return fig6
    else:
        fig6 = px.histogram(dfuvol2, x=vol1, nbins=150, histnorm='percent',title=ccy+' ' + vol1 +' Norm Vol')
        fig6.update_layout(font=dict(size=10))
        return fig6
@callback(Output("hist8", "figure"), Input("vol-dropdown1", "value"),
          Input("vol-dropdownccy", "value"))
def update_figure(vol1, ccy):
    #dffilt = dfswap[dfswap1.Year >= selected_year]
    if ccy == "EUR":
        fig7 = px.histogram(dfvol2, x=vol1,nbins=150,histnorm='percent', color = 'Year',title=ccy+' ' + vol1 +' Norm Vol')
        fig7.update_layout(font=dict(size=10))
        return fig7
    else:
        fig7 =px.histogram(dfuvol2, x=vol1, nbins=150, histnorm='percent', color ='Year',title=ccy+' ' + vol1 +' Norm Vol')
        fig7.update_layout(font=dict(size=10))
        return fig7

dash.register_page(__name__)
layout = dbc.Container([
    dbc.Row([dbc.Col(html.P("Select Currency:")),
             dbc.Col(dropdownccy),
             dbc.Col(),
             dbc.Col(),
             dbc.Col(),
             dbc.Col(),
             dbc.Col(),
             dbc.Col(),
             dbc.Col(),
             dbc.Col()]),
    dbc.Row([dbc.Col(html.P("Select swap/vol to plot:")),
             dbc.Col(dropdown),
             dbc.Col(),
             dbc.Col(),
             dbc.Col(),
             dbc.Col(),
             dbc.Col(),]),
    dbc.Row([dbc.Col(hist1graph),
             dbc.Col(hist5graph)]),
    dbc.Row([dbc.Col(hist3graph),
             dbc.Col(hist6graph)]),
    dbc.Row([dbc.Col(html.P("Select swap/vol to plot:")),
             dbc.Col(dropdown1),
             dbc.Col(),
             dbc.Col(),
             dbc.Col(),
             dbc.Col(),
             dbc.Col(), ]),
    dbc.Row([dbc.Col(hist2graph),
             dbc.Col(hist7graph)]),
    dbc.Row([dbc.Col(hist4graph),
             dbc.Col(hist8graph)])],
    fluid=True)


