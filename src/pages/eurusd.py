import dash
from dash import Dash, dcc, html, Input, Output, callback
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd


dash.register_page(__name__)
layout = (html.Div('''APP
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
EUR CORR
import dash
from dash import Dash, dcc, html, Input, Output, callback
from dash.dependencies import Input, Output
import dash_ag_grid as dag
from dash import html
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import plotly.express as px
from datetime import date

allow_duplicate=True
suppress_callback_exceptions=True
dash.register_page(__name__)
#grid of corr 22d lookback
#index adjusted by 6 x (no of days -1)
#dfswap = pd.read_excel(rC:"charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='Swaps',header=[0],index_col=[0])
url = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/swap1.csv?raw=true'
dfswap = pd.read_csv(url,header=[0],index_col=0)
dfswap = dfswap.tail(-1)
dfswap.index.rename('Date', inplace=True)
dfswap= dfswap.ffill()
cols9 = dfswap.columns
#cols.remove('fistcolumn')
for col in cols9:
    dfswap[col] = dfswap[col].astype(float)
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
dfcorr2['Date'] = pd.to_datetime(dfcorr2['Date'], format='%d/%m/%Y')
dfyear = dfcorr2["Date"].dt.year
dfcorr3 = pd.concat([dfcorr2, dfyear], axis=1)
dfcorr3.columns = ["Date", "1s2s", "1s5s", "1s10s", "1s20s", "1s30s", "2s5s", "2s10s", "2s20s", "2s30s", "5s10s", "5s20s", "5s30s",
                  "10s20s", "10s30s", "20s30s", "Year"]
#dfcorr3['Date'] = pd.to_datetime(dfcorr3['Date']).dt.date
#dfcorr3['Date'] = pd.to_datetime(dfcorr3['Date']).dt.strftime('%d/%m/%y')
dfcorr3['Year'] = dfcorr3['Year'].astype('int64')
dfcorr3["Year"]=dfcorr3["Year"].round(0)

url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/volgrid1.csv?raw=true'
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
dfvol = dfvol[dfvol.columns.drop('1m1y')]
dfvol = dfvol[dfvol.columns.drop('1m3y')]
dfvol = dfvol[dfvol.columns.drop('1m7y')]
dfvol = dfvol[dfvol.columns.drop('1m15y')]
dfvol = dfvol[dfvol.columns.drop('1m20y')]
dfvol = dfvol[dfvol.columns.drop('3m1y')]
dfvol = dfvol[dfvol.columns.drop('3m3y')]
dfvol = dfvol[dfvol.columns.drop('3m7y')]
dfvol = dfvol[dfvol.columns.drop('3m15y')]
dfvol = dfvol[dfvol.columns.drop('3m20y')]
dfvol = dfvol[dfvol.columns.drop('6m1y')]
dfvol = dfvol[dfvol.columns.drop('6m3y')]
dfvol = dfvol[dfvol.columns.drop('6m7y')]
dfvol = dfvol[dfvol.columns.drop('6m15y')]
dfvol = dfvol[dfvol.columns.drop('6m20y')]
dfvol = dfvol[dfvol.columns.drop('9m1y')]
dfvol = dfvol[dfvol.columns.drop('9m3y')]
dfvol = dfvol[dfvol.columns.drop('9m7y')]
dfvol = dfvol[dfvol.columns.drop('9m15y')]
dfvol = dfvol[dfvol.columns.drop('9m20y')]
dfvol = dfvol[dfvol.columns.drop('1y1y')]
dfvol = dfvol[dfvol.columns.drop('1y3y')]
dfvol = dfvol[dfvol.columns.drop('1y7y')]
dfvol = dfvol[dfvol.columns.drop('1y15y')]
dfvol = dfvol[dfvol.columns.drop('1y20y')]
dfvol = dfvol[dfvol.columns.drop('2y1y')]
dfvol = dfvol[dfvol.columns.drop('2y3y')]
dfvol = dfvol[dfvol.columns.drop('2y7y')]
dfvol = dfvol[dfvol.columns.drop('2y15y')]
dfvol = dfvol[dfvol.columns.drop('2y20y')]
dfvol = dfvol[dfvol.columns.drop('3y1y')]
dfvol = dfvol[dfvol.columns.drop('3y3y')]
dfvol = dfvol[dfvol.columns.drop('3y7y')]
dfvol = dfvol[dfvol.columns.drop('3y15y')]
dfvol = dfvol[dfvol.columns.drop('3y20y')]
dfvol = dfvol[dfvol.columns.drop('5y1y')]
dfvol = dfvol[dfvol.columns.drop('5y3y')]
dfvol = dfvol[dfvol.columns.drop('5y7y')]
dfvol = dfvol[dfvol.columns.drop('5y15y')]
dfvol = dfvol[dfvol.columns.drop('5y20y')]
dfvol = dfvol[dfvol.columns.drop('7y1y')]
dfvol = dfvol[dfvol.columns.drop('7y3y')]
dfvol = dfvol[dfvol.columns.drop('7y7y')]
dfvol = dfvol[dfvol.columns.drop('7y15y')]
dfvol = dfvol[dfvol.columns.drop('7y20y')]
dfvol = dfvol[dfvol.columns.drop('10y1y')]
dfvol = dfvol[dfvol.columns.drop('10y3y')]
dfvol = dfvol[dfvol.columns.drop('10y7y')]
dfvol = dfvol[dfvol.columns.drop('10y15y')]
dfvol = dfvol[dfvol.columns.drop('10y20y')]
dfvol = dfvol[dfvol.columns.drop('15y1y')]
dfvol = dfvol[dfvol.columns.drop('15y3y')]
dfvol = dfvol[dfvol.columns.drop('15y7y')]
dfvol = dfvol[dfvol.columns.drop('15y15y')]
dfvol = dfvol[dfvol.columns.drop('15y20y')]
dfvol = dfvol[dfvol.columns.drop('20y1y')]
dfvol = dfvol[dfvol.columns.drop('20y3y')]
dfvol = dfvol[dfvol.columns.drop('20y7y')]
dfvol = dfvol[dfvol.columns.drop('20y15y')]
dfvol = dfvol[dfvol.columns.drop('20y20y')]
dfvol['Date'] = pd.to_datetime(dfvol['Date'], format='%d/%m/%Y')
dfvol = dfvol.set_index('Date')
dfvol.at['2019-05-16','1y10y'] =39
#dfvol=dfvol.round(0)
dfvol1 = (dfvol-dfvol.shift(-1))*100
dfvol1 = dfvol1.head(-1)
dfvol2 = dfvol1.rolling(66).corr()
dfvol3 = dfvol2.head(-3120)
dfvol3 =dfvol3.reset_index(level=1)
index = dfvol3.index
dfvol4= dfvol2.dropna()
dfvol4=dfvol4.reset_index(level=1)
dfvol4=dfvol4.reset_index(drop=True)
dfvol4= dfvol4.assign(Date=index)
dfvol4= dfvol4.set_index('Date')
dfvol4=dfvol4.reset_index(level =0)
dfvol4.columns = ["Date","Vol", "1m2y", "1m5y", "1m10y","1m30y", "3m2y","3m5y","3m10y","3m30y","6m2y", "6m5y",
                          "6m10y", "6m30y", "9m2y", "9m5y", "9m10y", "9m30y", "1y2y", "1y5y", "1y10y", "1y30y", "2y2y", "2y5y",
                          "2y10y", "2y30y", "3y2y", "3y5y", "3y10y", "3y30y", "5y2y", "5y5y", "5y10y", "5y30y","7y2y", "7y5y",
                          "7y10y", "7y30y", "10y2y", "10y5y", "10y10y", "10y30y", "15y2y", "15y5y",
                           "15y10y", "15y30y", "20y2y", "20y5y", "20y10y", "20y30y"]
dfvol4=dfvol4.round(2)
dfvol4 = dfvol4.head(-2000)
#dfvol4['Date'] = pd.to_datetime(dfvol4['Date']).dt.date
#dfvol4['Date'] = pd.to_datetime(dfvol4['Date']).dt.strftime('%d/%m/%y')
dfvol5 = dfvol4.head(48)
dfvol5 = dfvol5[dfvol5.columns.drop('Date')]
dfvol5= dfvol5.set_index('Vol')

url2 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fwdgrid1.csv?raw=true'
dffwd = pd.read_csv(url2,header=[0,1],index_col=0)
dffwd.columns = dffwd.columns.map(''.join)
dffwd = dffwd.tail(-1)
#bottom entries not clean due to bbg errors
dffwd = dffwd.head(1200)
dffwd= dffwd.ffill()
cols2 = dffwd.columns
#cols.remove('fistcolumn')
for col in cols2:
    dffwd[col] = dffwd[col].astype(float)
dffwd = dffwd[dffwd.columns.drop('YearUnnamed: 109_level_1')]
dffwd = dffwd.reset_index(level=0)
dffwd.columns = ["Date","1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dffwd = dffwd[dffwd.columns.drop('1m1y')]
dffwd = dffwd[dffwd.columns.drop('1m3y')]
dffwd = dffwd[dffwd.columns.drop('1m7y')]
dffwd = dffwd[dffwd.columns.drop('1m15y')]
dffwd = dffwd[dffwd.columns.drop('1m20y')]
dffwd = dffwd[dffwd.columns.drop('3m1y')]
dffwd = dffwd[dffwd.columns.drop('3m3y')]
dffwd = dffwd[dffwd.columns.drop('3m7y')]
dffwd = dffwd[dffwd.columns.drop('3m15y')]
dffwd = dffwd[dffwd.columns.drop('3m20y')]
dffwd = dffwd[dffwd.columns.drop('6m1y')]
dffwd = dffwd[dffwd.columns.drop('6m3y')]
dffwd = dffwd[dffwd.columns.drop('6m7y')]
dffwd = dffwd[dffwd.columns.drop('6m15y')]
dffwd = dffwd[dffwd.columns.drop('6m20y')]
dffwd = dffwd[dffwd.columns.drop('9m1y')]
dffwd = dffwd[dffwd.columns.drop('9m3y')]
dffwd = dffwd[dffwd.columns.drop('9m7y')]
dffwd = dffwd[dffwd.columns.drop('9m15y')]
dffwd = dffwd[dffwd.columns.drop('9m20y')]
dffwd = dffwd[dffwd.columns.drop('1y1y')]
dffwd = dffwd[dffwd.columns.drop('1y3y')]
dffwd = dffwd[dffwd.columns.drop('1y7y')]
dffwd = dffwd[dffwd.columns.drop('1y15y')]
dffwd = dffwd[dffwd.columns.drop('1y20y')]
dffwd = dffwd[dffwd.columns.drop('2y1y')]
dffwd = dffwd[dffwd.columns.drop('2y3y')]
dffwd = dffwd[dffwd.columns.drop('2y7y')]
dffwd = dffwd[dffwd.columns.drop('2y15y')]
dffwd = dffwd[dffwd.columns.drop('2y20y')]
dffwd = dffwd[dffwd.columns.drop('3y1y')]
dffwd = dffwd[dffwd.columns.drop('3y3y')]
dffwd = dffwd[dffwd.columns.drop('3y7y')]
dffwd = dffwd[dffwd.columns.drop('3y15y')]
dffwd = dffwd[dffwd.columns.drop('3y20y')]
dffwd = dffwd[dffwd.columns.drop('5y1y')]
dffwd = dffwd[dffwd.columns.drop('5y3y')]
dffwd = dffwd[dffwd.columns.drop('5y7y')]
dffwd = dffwd[dffwd.columns.drop('5y15y')]
dffwd = dffwd[dffwd.columns.drop('5y20y')]
dffwd = dffwd[dffwd.columns.drop('7y1y')]
dffwd = dffwd[dffwd.columns.drop('7y3y')]
dffwd = dffwd[dffwd.columns.drop('7y7y')]
dffwd = dffwd[dffwd.columns.drop('7y15y')]
dffwd = dffwd[dffwd.columns.drop('7y20y')]
dffwd = dffwd[dffwd.columns.drop('10y1y')]
dffwd = dffwd[dffwd.columns.drop('10y3y')]
dffwd = dffwd[dffwd.columns.drop('10y7y')]
dffwd = dffwd[dffwd.columns.drop('10y15y')]
dffwd = dffwd[dffwd.columns.drop('10y20y')]
dffwd = dffwd[dffwd.columns.drop('15y1y')]
dffwd = dffwd[dffwd.columns.drop('15y3y')]
dffwd = dffwd[dffwd.columns.drop('15y7y')]
dffwd = dffwd[dffwd.columns.drop('15y15y')]
dffwd = dffwd[dffwd.columns.drop('15y20y')]
dffwd = dffwd[dffwd.columns.drop('20y1y')]
dffwd = dffwd[dffwd.columns.drop('20y3y')]
dffwd = dffwd[dffwd.columns.drop('20y7y')]
dffwd = dffwd[dffwd.columns.drop('20y15y')]
dffwd = dffwd[dffwd.columns.drop('20y20y')]
dffwd['Date'] = pd.to_datetime(dffwd['Date'], format='%d/%m/%Y')
dffwd = dffwd.set_index('Date')
dffwd1 = (dffwd-dffwd.shift(-1))
dffwd1 = dffwd1.head(-1)
dffwd2 = dffwd1.rolling(66).corr()
#dffwd=dffwd.round(2)
dffwd3 = dffwd2.head(-3120)
dffwd3 =dffwd3.reset_index(level=1)
index1 = dffwd3.index
dffwd4= dffwd2.dropna()
dffwd4=dffwd4.reset_index(level=1)
dffwd4=dffwd4.reset_index(drop=True)
dffwd4= dffwd4.assign(Date=index1)
dffwd4= dffwd4.set_index('Date')
dffwd4=dffwd4.reset_index(level =0)
dffwd4.columns = ["Date","Fwd", "1m2y", "1m5y", "1m10y","1m30y", "3m2y","3m5y","3m10y","3m30y","6m2y", "6m5y",
                          "6m10y", "6m30y", "9m2y", "9m5y", "9m10y", "9m30y", "1y2y", "1y5y", "1y10y", "1y30y", "2y2y", "2y5y",
                          "2y10y", "2y30y", "3y2y", "3y5y", "3y10y", "3y30y", "5y2y", "5y5y", "5y10y", "5y30y","7y2y", "7y5y",
                          "7y10y", "7y30y", "10y2y", "10y5y", "10y10y", "10y30y", "15y2y", "15y5y",
                           "15y10y", "15y30y", "20y2y", "20y5y", "20y10y", "20y30y"]
dffwd4=dffwd4.round(2)
#dffwd4['Date'] = pd.to_datetime(dffwd4['Date']).dt.date
#dffwd4['Date'] = pd.to_datetime(dffwd4['Date']).dt.strftime('%d/%m/%y')
dffwd5 = dffwd4.head(48)
dffwd5 = dffwd5[dffwd5.columns.drop('Date')]
dffwd5= dffwd5.set_index('Fwd')




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
fig1 = px.imshow(dfvol5, text_auto=True)
fig1.update_layout(
        font=dict(size=10),
        margin=dict(t=0, b=0, l=0, r=0))
graph1 = dcc.Graph(figure=fig1, style={"height": 1500, "width": 1400})
graph2 = dcc.Graph(id='swaptionfig',style={"height": 500, "width": 700})
graph3 = dcc.Graph(id='swaptionfig1',style={"height": 500, "width": 700})
fig2 = px.imshow(dffwd5, text_auto=True)
fig2.update_layout(
        font=dict(size=10),
        margin=dict(t=0, b=0, l=0, r=0))
graph4 = dcc.Graph(figure=fig2, style={"height": 1500, "width": 1400})
graph5 = dcc.Graph(id='fwdfig',style={"height": 500, "width": 700})
graph6 = dcc.Graph(id='fwdfig1',style={"height": 500, "width": 700})

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

dropdown3 = html.Div([
    html.P("Select swaption One to plot correlation:"),
    dcc.Dropdown(
                    id="swaption-dropdown",
                    clearable=False,
                    value="1y10y",
                    options=["1m2y", "1m5y", "1m10y","1m30y", "3m2y","3m5y","3m10y","3m30y","6m2y", "6m5y",
                          "6m10y", "6m30y", "9m2y", "9m5y", "9m10y", "9m30y", "1y2y", "1y5y", "1y10y", "1y30y", "2y2y", "2y5y",
                          "2y10y", "2y30y", "3y2y", "3y5y", "3y10y", "3y30y", "5y2y", "5y5y", "5y10y", "5y30y","7y2y", "7y5y",
                          "7y10y", "7y30y", "10y2y", "10y5y", "10y10y", "10y30y", "15y2y", "15y5y",
                           "15y10y", "15y30y", "20y2y", "20y5y", "20y10y", "20y30y"],
                    className="ag-theme-balham")
                    #style={"height": 20, "width": 100})
])

dropdown4 = html.Div([
    html.P("Select swaption Two to plot correlation:"),
    dcc.Dropdown(
                    id="swaption-dropdown1",
                    clearable=False,
                    value="1y30y",
                    options=["1m2y", "1m5y", "1m10y","1m30y", "3m2y","3m5y","3m10y","3m30y","6m2y", "6m5y",
                          "6m10y", "6m30y", "9m2y", "9m5y", "9m10y", "9m30y", "1y2y", "1y5y", "1y10y", "1y30y", "2y2y", "2y5y",
                          "2y10y", "2y30y", "3y2y", "3y5y", "3y10y", "3y30y", "5y2y", "5y5y", "5y10y", "5y30y","7y2y", "7y5y",
                          "7y10y", "7y30y", "10y2y", "10y5y", "10y10y", "10y30y", "15y2y", "15y5y",
                           "15y10y", "15y30y", "20y2y", "20y5y", "20y10y", "20y30y"],
                    className="ag-theme-balham")
                    #style={"height": 20, "width": 100})
])

dropdown5 = html.Div([
    html.P("Select swaption One to plot correlation:"),
    dcc.Dropdown(
                    id="swaption-dropdown2",
                    clearable=False,
                    value="1y10y",
                    options=["1m2y", "1m5y", "1m10y","1m30y", "3m2y","3m5y","3m10y","3m30y","6m2y", "6m5y",
                          "6m10y", "6m30y", "9m2y", "9m5y", "9m10y", "9m30y", "1y2y", "1y5y", "1y10y", "1y30y", "2y2y", "2y5y",
                          "2y10y", "2y30y", "3y2y", "3y5y", "3y10y", "3y30y", "5y2y", "5y5y", "5y10y", "5y30y","7y2y", "7y5y",
                          "7y10y", "7y30y", "10y2y", "10y5y", "10y10y", "10y30y", "15y2y", "15y5y",
                           "15y10y", "15y30y", "20y2y", "20y5y", "20y10y", "20y30y"],
                    className="ag-theme-balham")
                    #style={"height": 20, "width": 100})
])

dropdown6 = html.Div([
    html.P("Select swaption Two to plot correlation:"),
    dcc.Dropdown(
                    id="swaption-dropdown3",
                    clearable=False,
                    value="1y30y",
                    options=["1m2y", "1m5y", "1m10y","1m30y", "3m2y","3m5y","3m10y","3m30y","6m2y", "6m5y",
                          "6m10y", "6m30y", "9m2y", "9m5y", "9m10y", "9m30y", "1y2y", "1y5y", "1y10y", "1y30y", "2y2y", "2y5y",
                          "2y10y", "2y30y", "3y2y", "3y5y", "3y10y", "3y30y", "5y2y", "5y5y", "5y10y", "5y30y","7y2y", "7y5y",
                          "7y10y", "7y30y", "10y2y", "10y5y", "10y10y", "10y30y", "15y2y", "15y5y",
                           "15y10y", "15y30y", "20y2y", "20y5y", "20y10y", "20y30y"],
                    className="ag-theme-balham")
                    #style={"height": 20, "width": 100})
])

dropdown7 = html.Div([
    html.P("Select Fwd One to plot correlation:"),
    dcc.Dropdown(
                    id="fwd-dropdown",
                    clearable=False,
                    value="5y5y",
                    options=["1m2y", "1m5y", "1m10y","1m30y", "3m2y","3m5y","3m10y","3m30y","6m2y", "6m5y",
                          "6m10y", "6m30y", "9m2y", "9m5y", "9m10y", "9m30y", "1y2y", "1y5y", "1y10y", "1y30y", "2y2y", "2y5y",
                          "2y10y", "2y30y", "3y2y", "3y5y", "3y10y", "3y30y", "5y2y", "5y5y", "5y10y", "5y30y","7y2y", "7y5y",
                          "7y10y", "7y30y", "10y2y", "10y5y", "10y10y", "10y30y", "15y2y", "15y5y",
                           "15y10y", "15y30y", "20y2y", "20y5y", "20y10y", "20y30y"],
                    className="ag-theme-balham")
                    #style={"height": 20, "width": 100})
])

dropdown8 = html.Div([
    html.P("Select Fwd Two to plot correlation:"),
    dcc.Dropdown(
                    id="fwd-dropdown1",
                    clearable=False,
                    value="5y10y",
                    options=["1m2y", "1m5y", "1m10y","1m30y", "3m2y","3m5y","3m10y","3m30y","6m2y", "6m5y",
                          "6m10y", "6m30y", "9m2y", "9m5y", "9m10y", "9m30y", "1y2y", "1y5y", "1y10y", "1y30y", "2y2y", "2y5y",
                          "2y10y", "2y30y", "3y2y", "3y5y", "3y10y", "3y30y", "5y2y", "5y5y", "5y10y", "5y30y","7y2y", "7y5y",
                          "7y10y", "7y30y", "10y2y", "10y5y", "10y10y", "10y30y", "15y2y", "15y5y",
                           "15y10y", "15y30y", "20y2y", "20y5y", "20y10y", "20y30y"],
                    className="ag-theme-balham")
                    #style={"height": 20, "width": 100})
])

dropdown9 = html.Div([
    html.P("Select Fwd One to plot correlation:"),
    dcc.Dropdown(
                    id="fwd-dropdown2",
                    clearable=False,
                    value="10y10y",
                    options=["1m2y", "1m5y", "1m10y","1m30y", "3m2y","3m5y","3m10y","3m30y","6m2y", "6m5y",
                          "6m10y", "6m30y", "9m2y", "9m5y", "9m10y", "9m30y", "1y2y", "1y5y", "1y10y", "1y30y", "2y2y", "2y5y",
                          "2y10y", "2y30y", "3y2y", "3y5y", "3y10y", "3y30y", "5y2y", "5y5y", "5y10y", "5y30y","7y2y", "7y5y",
                          "7y10y", "7y30y", "10y2y", "10y5y", "10y10y", "10y30y", "15y2y", "15y5y",
                           "15y10y", "15y30y", "20y2y", "20y5y", "20y10y", "20y30y"],
                    className="ag-theme-balham")
                    #style={"height": 20, "width": 100})
])

dropdown10 = html.Div([
    html.P("Select Fwd Two to plot correlation:"),
    dcc.Dropdown(
                    id="fwd-dropdown3",
                    clearable=False,
                    value="10y10y",
                    options=["1m2y", "1m5y", "1m10y","1m30y", "3m2y","3m5y","3m10y","3m30y","6m2y", "6m5y",
                          "6m10y", "6m30y", "9m2y", "9m5y", "9m10y", "9m30y", "1y2y", "1y5y", "1y10y", "1y30y", "2y2y", "2y5y",
                          "2y10y", "2y30y", "3y2y", "3y5y", "3y10y", "3y30y", "5y2y", "5y5y", "5y10y", "5y30y","7y2y", "7y5y",
                          "7y10y", "7y30y", "10y2y", "10y5y", "10y10y", "10y30y", "15y2y", "15y5y",
                           "15y10y", "15y30y", "20y2y", "20y5y", "20y10y", "20y30y"],
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
        font=dict(size=10))
    return fig

@callback(Output("swaptionfig", "figure"),
          Input("swaption-dropdown", "value"),Input('swaption-dropdown1', 'value'))
def update_figure(vol1, vol2):
    dfvfilt = dfvol4[dfvol4.Vol == vol1]
    #return px.line(dfcorr2, x="Date", y=pair)
    trace1 = go.Scatter(x=dfvfilt['Date'],
                        y=dfvfilt[vol2],
                        name=vol1 +'&'+ vol2 + ' Corr',
                        yaxis='y1',
                        line_color='rgb(102,166,30)')
    data = [trace1]
    layout = go.Layout(yaxis=dict(title=vol1 +'&'+ vol2 + ' Corr'),
                       yaxis2=dict(title='',
                                   overlaying='y',
                                   side='right'))

    swaptionfig = go.Figure(data=data, layout=layout)
    swaptionfig.update_layout(
        font=dict(size=10))
    return swaptionfig

@callback(Output("swaptionfig1", "figure"),
          Input("swaption-dropdown2", "value"),Input('swaption-dropdown3', 'value'))
def update_figure(vol1, vol2):
    dfvfilt = dfvol4[dfvol4.Vol == vol1]
    #return px.line(dfcorr2, x="Date", y=pair)
    trace1 = go.Scatter(x=dfvfilt['Date'],
                        y=dfvfilt[vol2],
                        name=vol1 +'&'+ vol2 + ' Corr',
                        yaxis='y1',
                        line_color='rgb(252,141,98)')
    data = [trace1]
    layout = go.Layout(yaxis=dict(title= vol1 +'&'+ vol2 + ' Corr'),
                       yaxis2=dict(title='',
                                   overlaying='y',
                                   side='right'))

    swaptionfig1 = go.Figure(data=data, layout=layout)
    swaptionfig1.update_layout(
        font=dict(size=10),)
        #xaxis=dict(autorange="reversed"))
    return swaptionfig1

@callback(Output("fwdfig", "figure"),
          Input("fwd-dropdown", "value"),Input('fwd-dropdown1', 'value'))
def update_figure(fwd1, fwd2):
    dfvfilt = dffwd4[dffwd4.Fwd == fwd1]
    #return px.line(dfcorr2, x="Date", y=pair)
    trace1 = go.Scatter(x=dfvfilt['Date'],
                        y=dfvfilt[fwd2],
                        name=fwd1 +'&'+ fwd2 + ' Corr',
                        yaxis='y1',
                        line_color='Yellow')
    data = [trace1]
    layout = go.Layout(yaxis=dict(title= fwd1 +'&'+ fwd2 + ' Corr'),
                       yaxis2=dict(title='',
                                   overlaying='y',
                                   side='right'))

    fwdfig = go.Figure(data=data, layout=layout)
    fwdfig.update_layout(
        font=dict(size=10))
    return fwdfig

@callback(Output("fwdfig1", "figure"),
          Input("fwd-dropdown2", "value"),Input('fwd-dropdown3', 'value'))
def update_figure(fwd1, fwd2):
    dfvfilt = dffwd4[dffwd4.Fwd == fwd1]
    #return px.line(dfcorr2, x="Date", y=pair)
    trace1 = go.Scatter(x=dfvfilt['Date'],
                        y=dfvfilt[fwd2],
                        name=fwd1 +'&'+ fwd2 + ' Corr',
                        yaxis='y1',
                        line_color='Purple')
    data = [trace1]
    layout = go.Layout(yaxis=dict(title= fwd1 +'&'+ fwd2 + ' Corr'),
                       yaxis2=dict(title='',
                                   overlaying='y',
                                   side='right'))

    fwdfig1 = go.Figure(data=data, layout=layout)
    fwdfig1.update_layout(
        font=dict(size=10))
    return fwdfig1


layout = dbc.Container([
         dbc.Row([dbc.Col(html.H1('EUR Swap & Vol Correlation'))]),
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
         dbc.Row([dbc.Col(html.P('Swaption Correlation:'))]),
         dbc.Row([dbc.Col(graph1)]),
         dbc.Row([dbc.Col(dropdown3),
                  dbc.Col(dropdown5)]),
         dbc.Row([dbc.Col(dropdown4),
                  dbc.Col(dropdown6)]),
         dbc.Row([dbc.Col(graph2),
                  dbc.Col(graph3)]),
         dbc.Row([dbc.Col(html.P('Fwd Rate Correlation:'))]),
         dbc.Row([dbc.Col(graph4)]),
         dbc.Row([dbc.Col(dropdown7),
                  dbc.Col(dropdown9)]),
         dbc.Row([dbc.Col(dropdown8),
                  dbc.Col(dropdown10)]),
         dbc.Row([dbc.Col(graph5),
                  dbc.Col(graph6)],
                  ],fluid=True))
EUR FLIES
import dash
from dash import Dash, dcc, html, Input, Output, callback
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd


#dfswap = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdFly',header=[0],index_col=[0])
url = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fly1.csv?raw=true'
dfswap = pd.read_csv(url,header=[0],index_col=0)
dfswap = dfswap.tail(-1)
dfswap= dfswap.ffill()
cols = dfswap.columns
#cols.remove('fistcolumn')
for col in cols:
    dfswap[col] = dfswap[col].astype(float)
dfswap.index.rename('Date', inplace=True)
dfswap = dfswap.reset_index(level=0)
dfswap['Date'] = pd.to_datetime(dfswap['Date'], format='%d/%m/%Y')
dfswap['Year'] = dfswap['Year'].astype('int64')
dfswap["Year"]=dfswap["Year"].round(0)

#dfvol = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/volgrid1.csv?raw=true'
dfvol = pd.read_csv(url1,header=[0,1],index_col=0)
dfvol.columns = dfvol.columns.map(''.join)
dfvol = dfvol.tail(-1)
dfvol= dfvol.ffill()
cols1 = dfvol.columns
#cols.remove('fistcolumn')
for col in cols1:
    dfvol[col] = dfvol[col].astype(float)
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
dfvol['Date'] = pd.to_datetime(dfvol['Date'], format='%d/%m/%Y')
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
                  title="1y 1y1y 2y1y Fwd fly",color_discrete_sequence=["pink"])
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
                  title="1y1y 2y1y 3y1y Fwd fly",color_discrete_sequence=["orange"])
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
                  title="2y1y 3y1y 4y1y Fwd fly",color_discrete_sequence=["blue"])
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
                  title="3y1y 4y1y 5y1y Fwd fly",color_discrete_sequence=["green"])
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
                  title="4y1y 5y1y 6y1y Fwd fly",color_discrete_sequence=["red"])
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
                  title="5y1y 6y1y 7y1y Fwd fly",color_discrete_sequence=["purple"])
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
                  title="6y1y 7y1y 8y1y Fwd fly",color_discrete_sequence=["yellow"])
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
                  title="7y1y 8y1y 9y1y Fwd fly",color_discrete_sequence=["black"])
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
                  title="5y 5y5y 10y5y Fwd fly",color_discrete_sequence=["grey"])
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
                  title="5y5y 10y5y 15y5y Fwd fly",color_discrete_sequence=["gold"])
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
                  title="10y5y 15y5y 20y5y Fwd fly",color_discrete_sequence=["red"])
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
                  title="15y5y 20y5y 25y5y Fwd fly",color_discrete_sequence=["orange"])
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
                  title="20y5y 25y5y 30y5y Fwd fly",color_discrete_sequence=["purple"])
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
                  title="1y2y 1y5y 1y10y Vol fly",color_discrete_sequence=["green"])
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
                  title="1y5y 1y10y 1y30y Vol fly",color_discrete_sequence=["blue"])
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
                  title="1y10y 1y20y 1y30y Vol fly",color_discrete_sequence=["red"])
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
                  title="2y2y 2y5y 2y10y Vol fly",color_discrete_sequence=["gold"])
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
                  title="2y5y 2y10y 2y30y Vol fly",color_discrete_sequence=["yellow"])
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
                  title="2y10y 2y20y 2y30y Vol fly",color_discrete_sequence=["grey"])
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
                  title="5y2y 5y5y 5y10y Vol fly",color_discrete_sequence=["pink"])
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
                  title="5y5y 5y10y 5y30y Vol fly",color_discrete_sequence=["orange"])
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
                  title="5y10y 5y20y 5y30y Vol fly",color_discrete_sequence=["green"])
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
                  title="10y2y 10y5y 10y10y Vol fly",color_discrete_sequence=["purple"])
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
                  title="10y5y 10y10y 10y30y Vol fly",color_discrete_sequence=["blue"])
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
                  title="10y10y 10y20y 10y30y Vol fly",color_discrete_sequence=["yellow"])
    fly.update_layout(
        font=dict(size=10),
        margin=dict(l=5, r=5, t=20, b=20))
    return fly

dash.register_page(__name__)
layout = dbc.Container([
         dbc.Row([dbc.Col(html.H1('EUR Vol & Swap Flies'))]),
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
EUR TIME SERIES
import dash
from dash import Dash, dcc, html, Input, Output, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
import plotly.graph_objects as go
import math as math

suppress_callback_exceptions=True
#dfswap = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
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

#dfvol = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/volgrid1.csv?raw=true'
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
dfvol=dfvol.round(1)
dfvol1 = dfvol.head(-66)

#for realised vol
#dfdswap = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
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

graph1 = dcc.Graph(id='fig1',style={"height": 450, "width": 710})
graph2 = dcc.Graph(id='fig2',style={"height": 450, "width": 710})
graph3 = dcc.Graph(id='fig3',style={"height": 450, "width": 710})
graph4 = dcc.Graph(id='fig4',style={"height": 450, "width": 710})
graph5 = dcc.Graph(id='fig5',style={"height": 450, "width": 710})
graph6 = dcc.Graph(id='fig6',style={"height": 450, "width": 710})

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

@callback(Output("fig1", "figure"),
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
    #fig1.update_traces(mode="markers+lines", hovertemplate=None)
    fig1.update_layout(
        font=dict(size=10)
    )
    return fig1

@callback(Output("fig2", "figure"),
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
@callback(Output("fig3", "figure"),
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
@callback(Output("fig4", "figure"),
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
@callback(Output("fig5", "figure"),
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
@callback(Output("fig6", "figure"),
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
    dbc.Row([dbc.Col(html.Div('EUR Historic Swap and Vol Data'))]),
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
EUR VOL SURFACE
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
#dfvol = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
url = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/volgrid1.csv?raw=true'
dfvol = pd.read_csv(url,header=[0,1],index_col=0)
dfvol = dfvol.tail(-1)
dfvol= dfvol.ffill()
dfvol = dfvol[dfvol.columns.drop('Year')]
cols11 = dfvol.columns
#cols.remove('fistcolumn')
for col in cols11:
    dfvol[col] = dfvol[col].astype(float)
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
#dfzs = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
#url = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/volgrid1.csv?raw=true'
dfzs = pd.read_csv(url,header=[0,1],index_col=0)
dfzs = dfzs.tail(-1)
dfzs= dfzs.ffill()
dfzs = dfzs[dfzs.columns.drop('Year')]
dfzs = dfzs.head(66)
cols = dfzs.columns
#cols.remove('fistcolumn')
for col in cols:
    dfzs[col] = dfzs[col].astype(float)
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
#dfswap = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fwdgrid1.csv?raw=true'
dfswap = pd.read_csv(url1,header=[0,1],index_col=0)
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
#dfdvol = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
#url = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/volgrid1.csv?raw=true'
dfdvol = pd.read_csv(url,header=[0,1],index_col=0)
dfdvol = dfdvol.tail(-1)
dfdvol= dfdvol.ffill()
dfdvol = dfdvol[dfdvol.columns.drop('Year')]
cols1 = dfdvol.columns
#cols.remove('fistcolumn')
for col in cols1:
    dfdvol[col] = dfdvol[col].astype(float)
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
#dfdswap = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
#url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fwdgrid1.csv?raw=true'
dfdswap = pd.read_csv(url1,header=[0,1],index_col=0)
dfdswap = dfdswap.tail(-1)
dfdswap1 = dfdswap.head(-66)
index = dfdswap1.index
dfdswap= dfdswap.ffill()
dfdswap = dfdswap[dfdswap.columns.drop('Year')]
cols2 = dfdswap.columns
#cols.remove('fistcolumn')
for col in cols2:
    dfdswap[col] = dfdswap[col].astype(float)
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
dfdswap = dfdswap.reset_index(level=0)
dfdswap['Date1'] = pd.to_datetime(dfdswap['Date1'], format='%d/%m/%Y')
dfdvol1 = dfdvol1.reset_index(level=0)
dfdvol1['index'] = pd.to_datetime(dfdvol1['index'], format='%d/%m/%Y')
dfdswap = dfdswap.set_index('Date1')
dfdvol1 = dfdvol1.set_index('index')
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

dfcsurf1 = dfswap.head(1)
dfcsurf2 = dfswap[8:9]
dfcsurf3 = dfswap[40:41]
dfcsurf4 = pd.concat([dfcsurf1, dfcsurf2, dfcsurf3])
dfcsurf4 = dfcsurf4.reset_index(level=0)
dfcsurf4 = dfcsurf4[dfcsurf4.columns.drop('index')]
#dfcsurf4 = dfcsurf4[dfcsurf4.columns.drop('Year')]
#dfcsurf4['Date'] = pd.to_datetime(dfcsurf4['Date'], format='%d/%m/%Y')
#dfcsurf4['Date'] = pd.to_datetime(dfcsurf4['Date'], format='%d/%m/%Y')
dfcsurf5 = dfcsurf4.transpose()
header = ("Today", "1 week ago", "1 month ago")
dfcsurf5.columns = header
dfcsurf6 = dfcsurf5.tail(-1)
dfcsurf6 = dfcsurf6.tail(-1)
dfcsurf7 = dfcsurf6.head(9)
cols = dfcsurf7.columns
#cols.remove('fistcolumn')
for col in cols:
    dfcsurf7[col] = dfcsurf7[col].astype(float)


url7 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fly1.csv?raw=true'
dffswap = pd.read_csv(url7,header=[0],index_col=0)
dffswap = dffswap.tail(-1)
dffswap= dffswap.ffill()
cols = dffswap.columns
#cols.remove('fistcolumn')
for col in cols:
    dffswap[col] = dffswap[col].astype(float)
dffswap.index.rename('Date', inplace=True)
dffswap = dffswap.reset_index(level=0)
dffswap['Date'] = pd.to_datetime(dffswap['Date'], format='%d/%m/%Y')
dffswap['Year'] = dffswap['Year'].astype('int64')
dffswap["Year"]=dffswap["Year"].round(0)
dffswap = dffswap[dffswap.columns.drop('Year')]
dffswap = dffswap[dffswap.columns.drop('5y')]
dffswap = dffswap[dffswap.columns.drop('5y5y')]
dffsurf1 = dffswap.head(1)
dffsurf2 = dffswap[5:6]
dffsurf3 = dffswap[22:23]
dffsurf4 = pd.concat([dffsurf1, dffsurf2, dffsurf3])
dffsurf4 = dffsurf4.reset_index(level=0)
dffsurf4 = dffsurf4[dffsurf4.columns.drop('index')]
dffsurf4['Date'] = pd.to_datetime(dffsurf4['Date'], format='%d/%m/%Y')
dffsurf4['Date'] = pd.to_datetime(dffsurf4['Date'], format='%d/%m/%Y')
dffsurf5 = dffsurf4.transpose()
header = ("Today", "1 week ago", "1 month ago")
dffsurf5.columns = header
dffsurf6 = dffsurf5.tail(-1)
dffsurf6

#1m lookback vol
#dfvol1m = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
#url = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/volgrid1.csv?raw=true'
dfvol1m = pd.read_csv(url,header=[0,1],index_col=0)
dfvol1m = dfvol1m.tail(-1)
dfvol1m= dfvol1m.ffill()
dfvol1m = dfvol1m[dfvol1m.columns.drop('Year')]
cols3 = dfvol1m.columns
#cols.remove('fistcolumn')
for col in cols3:
    dfvol1m[col] = dfvol1m[col].astype(float)
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
#dfswap1m = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
#url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fwdgrid1.csv?raw=true'
dfswap1m = pd.read_csv(url1,header=[0,1],index_col=0)
dfswap1m = dfswap1m.tail(-1)
dfswap1m= dfswap1m.ffill()
dfswap1m = dfswap1m[dfswap1m.columns.drop('Year')]
cols4 = dfswap1m.columns
#cols.remove('fistcolumn')
for col in cols4:
    dfswap1m[col] = dfswap1m[col].astype(float)
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
#dfvol3m = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
url = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/volgrid1.csv?raw=true'
dfvol3m = pd.read_csv(url,header=[0,1],index_col=0)
dfvol3m = dfvol3m.tail(-1)
dfvol3m= dfvol3m.ffill()
dfvol3m = dfvol3m[dfvol3m.columns.drop('Year')]
cols5 = dfvol3m.columns
#cols.remove('fistcolumn')
for col in cols5:
    dfvol3m[col] = dfvol3m[col].astype(float)
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
#dfswap3m = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
#url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fwdgrid1.csv?raw=true'
dfswap3m = pd.read_csv(url1,header=[0,1],index_col=0)
dfswap3m = dfswap3m.tail(-1)
dfswap3m= dfswap3m.ffill()
dfswap3m = dfswap3m[dfswap3m.columns.drop('Year')]
cols6 = dfswap3m.columns
#cols.remove('fistcolumn')
for col in cols6:
    dfswap3m[col] = dfswap3m[col].astype(float)
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

dropdown2 = html.Div([
    html.P("Select Spot or Fwd Curve"),
    dcc.Dropdown(
                    id="tail-dropdown2",
                    clearable=False,
                    value="Fwd",
                    options=["Spot", "Fwd"],
                    className="ag-theme-balham",
                    style={"height": 38, "width": 690})
])

surf1graph = dcc.Graph(id='surf1y',style={"height": 400, "width": 690, "font-size": '10px'})
surf2graph = dcc.Graph(id='surf10y', style={"height": 400, "width": 690, "font-size": '10px'})
surf3graph = dcc.Graph(id='curve', style={"height": 400, "width": 690, "font-size": '10px'})


@callback(Output("surf1y", "figure"), Input("tail-dropdown", "value"))
def update_figure(tail):
    fig2 = px.line(dfsurf4, x="Expiry", y=tail, color='Date')
    fig2.update_layout(
            font=dict(size=10))
    return fig2

@callback(Output("surf10y", "figure"), Input("tail-dropdown1", "value"))
def update_figure(tail):
    fig1 = px.line(dfsurf4, x="Expiry", y=tail, color='Date')
    fig1.update_layout(
        font=dict(size=10))
    return fig1

@callback(Output("curve", "figure"), Input("tail-dropdown2", "value"))
def update_figure(curve):
    if curve == "Spot":
        fig = px.line(dfcsurf7,labels={
                      "index": "Swap",
                      "value": "Swap Rate",
                      "variable": "Date"})
        fig.update_layout(
            font=dict(size=10))
        return fig
    else:
        fig = px.line(dffsurf6, labels={
            "index": "Swap",
            "value": "Swap Rate",
            "variable": "Date"})
        fig.update_layout(
            font=dict(size=10))
        return fig



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
    className="ag-theme-balham",
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
    dbc.Row([dbc.Col(html.H1('EUR Vol Surface'))]),
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
            dbc.Col(grid12)]),
    dbc.Row([dbc.Col(dropdown2)]),
    dbc.Row([dbc.Col(surf3graph)]),
],fluid=True)
HISTOGRAMS
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
SCATT PLOTS
import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd


#dfvol = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='VolGrid',header=[0,1],index_col=[0])
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

#dfswap = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
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

#dfswap = pd.read_excel(r"C:\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='FwdGrid',header=[0,1],index_col=[0])
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
XMKT
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
import plotly.graph_objects as go

suppress_callback_exceptions=True



url1 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/volgrid1.csv?raw=true'
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
dfvol = dfvol.head(600)
url = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/uvolgrid1.csv?raw=true'
dfuvol = pd.read_csv(url,header=[0,1],index_col=0)
dfuvol.columns = dfuvol.columns.map(''.join)
dfuvol = dfuvol.tail(-1)
dfuvol= dfuvol.ffill()
cols2 = dfuvol.columns
#cols.remove('fistcolumn')
for col in cols2:
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
dfuvol = dfuvol.set_index('Date')
dfuvol = dfuvol.head(600)
dfdiff = dfuvol.subtract(dfvol, fill_value=0)
dfdiff = dfdiff.reset_index(level=0)
dfdiff.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
                          "20y7y", "20y10y", "20y15y", "20y20y", "20y30y"]
dfdiff1 = dfdiff[dfdiff["Date"].isin(dfvol["Date"])]
dfyear = dfdiff1["Date"].dt.year
dfdiff2 = pd.concat([dfdiff1, dfyear], axis=1)
dfdiff2.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfdiff2['Year'] = dfdiff2['Year'].astype('int64')
dfdiff2["Year"]=dfdiff2["Year"].round(0)
#dfdiff2 = dfdiff2.set_index('Date')

#forwards
url2 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fwdgrid1.csv?raw=true'
dffwd = pd.read_csv(url2,header=[0,1],index_col=0)
dffwd.columns = dffwd.columns.map(''.join)
dffwd = dffwd.tail(-1)
dffwd= dffwd.ffill()
cols3 = dffwd.columns
#cols.remove('fistcolumn')
for col in cols3:
    dffwd[col] = dffwd[col].astype(float)
dffwd = dffwd[dffwd.columns.drop('YearUnnamed: 109_level_1')]
dffwd = dffwd.reset_index(level=0)
dffwd.columns = ["Date","1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dffwd['Date'] = pd.to_datetime(dffwd['Date'], format='%d/%m/%Y')
dffwd = dffwd.set_index('Date')
dffwd = dffwd.head(600)
url3 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/ufwdgrid1.csv?raw=true'
dfufwd = pd.read_csv(url3,header=[0,1],index_col=0)
dfufwd.columns = dfufwd.columns.map(''.join)
dfufwd = dfufwd.tail(-1)
dfufwd= dfufwd.ffill()
cols4 = dfufwd.columns
#cols.remove('fistcolumn')
for col in cols4:
    dfufwd[col] = dfufwd[col].astype(float)
dfufwd = dfufwd[dfufwd.columns.drop('YearUnnamed: 109_level_1')]
dfufwd = dfufwd.reset_index(level=0)
dfufwd.columns = ["Date","1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfufwd['Date'] = pd.to_datetime(dfufwd['Date'], format='%d/%m/%Y')
dfufwd = dfufwd.set_index('Date')
dfufwd = dfufwd.head(600)
dfdifff = dfufwd.subtract(dffwd, fill_value=0)
dfdifff = dfdifff.reset_index(level=0)
dfdifff.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dffwd = dffwd.reset_index(level=0)
dffwd.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfufwd = dfufwd.reset_index(level=0)
dfufwd.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfdifff = dfdifff[dfdifff["Date"].isin(dffwd["Date"])]
dfdifff1 = dfdifff[dfdifff["Date"].isin(dfufwd["Date"])]
dfyear1 = dfdifff1["Date"].dt.year
dfdifff2 = pd.concat([dfdifff1, dfyear1], axis=1)
dfdifff2.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfdifff2['Year'] = dfdifff2['Year'].astype('int64')
dfdifff2["Year"]=dfdifff2["Year"].round(0)
#dfdiff2 = dfdiff2.set_index('Date')

#realised vol
#url2 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/fwdgrid1.csv?raw=true'
dfdswap = pd.read_csv(url2,header=[0,1],index_col=0)
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
dfdswap.head(600)
#url3 = 'https://github.com/cpearson77/CP-Vol-Analytics/blob/main/ufwdgrid1.csv?raw=true'
dfudswap = pd.read_csv(url3,header=[0,1],index_col=0)
dfudswap = dfudswap.tail(-1)
dfudswap1 = dfudswap.head(-66)
index = dfudswap1.index
dfudswap= dfudswap.ffill()
dfudswap = dfudswap[dfudswap.columns.drop('Year')]
cols8 = dfudswap.columns
#cols.remove('fistcolumn')
for col in cols8:
    dfudswap[col] = dfudswap[col].astype(float)
dfudswap = (dfudswap-dfudswap.shift(-1))*100
dfudswap = (dfudswap.rolling(66).std())*(math.sqrt(252))
dfudswap = dfudswap.dropna()
dfudswap =dfudswap.reset_index(drop=True)
dfudswap = dfudswap.assign(Date1=index)
dfudswap['Date1'] = pd.to_datetime(dfudswap['Date1'], format='%d/%m/%Y')
dfudswap = dfudswap.set_index('Date1')
dfudswap.columns = dfudswap.columns.map(''.join)
dfudswap=dfudswap.round(0)
dfudswap.columns = ["1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfudswap.head(600)
dfrdifff = dfudswap.subtract(dfdswap, fill_value=0)
dfrdifff = dfrdifff.reset_index(level=0)
dfrdifff.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfdswap = dfdswap.reset_index(level=0)
dfdswap.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfudswap = dfudswap.reset_index(level=0)
dfudswap.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfrdifff = dfrdifff[dfrdifff["Date"].isin(dfdswap["Date"])]
dfrdifff1 = dfrdifff[dfrdifff["Date"].isin(dfudswap["Date"])]
dfryear1 = dfrdifff1["Date"].dt.year
dfrdifff2 = pd.concat([dfrdifff1, dfryear1], axis=1)
dfrdifff2.columns = ["Date", "1m1y", "1m2y", "1m3y", "1m5y", "1m7y", "1m10y", "1m15y", "1m20y", "1m30y","3m1y", "3m2y",
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
dfrdifff2['Year'] = dfrdifff2['Year'].astype('int64')
dfrdifff2["Year"]=dfrdifff2["Year"].round(0)
#dfdiff2 = dfdiff2.set_index('Date')

#translating into grid format for vols
dfdiff3 = dfdiff2.set_index('Date')
dfdiff3 = dfdiff3[dfdiff3.columns.drop('Year')]
header=[["a1m", "a1m", "a1m", "a1m", "a1m", "a1m", "a1m", "a1m", "a1m","b3m", "b3m",
                          "b3m", "b3m", "b3m", "b3m", "b3m", "b3m", "b3m", "c6m", "c6m", "c6m", "c6m",
                          "c6m", "c6m", "c6m", "c6m", "c6m","d9m", "d9m", "d9m", "d9m",
                          "d9m", "d9m", "d9m", "d9m", "d9m", "e1y", "e1y", "e1y", "e1y", "e1y", "e1y",
                          "e1y", "e1y", "e1y","f2y", "f2y", "f2y", "f2y",
                          "f2y", "f2y", "f2y", "f2y", "f2y","g3y", "g3y", "g3y", "g3y",
                          "g3y", "g3y", "g3y", "g3y", "g3y","h5y", "h5y", "h5y", "h5y",
                          "h5y", "h5y", "h5y", "h5y", "h5y","i7y", "i7y", "i7y", "i7y",
                          "i7y", "i7y", "i7y", "i7y", "i7y","j10y", "j10y", "j10y", "j10y",
                          "j10y", "j10y", "j10y", "j10y", "j10y","k15y", "k15y", "k15y", "k15y",
                          "k15y", "k15y", "k15y", "k15y", "k15y","l20y", "l20y", "l20y", "l20y",
                          "l20y", "l20y", "l20y", "l20y", "l20y"],["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y","1y", "2y",
                          "3y", "5y", "7y", "10y", "15y", "20y", "30y", "1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y", "1y", "2y", "3y", "5y", "7y", "10y",
                          "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y"]]
dfdiff3.columns = header
#dfdiff4 = dfdiff3.loc[reversed(dfdiff3.index)]
dfdiff4 =dfdiff3.stack(level=0)
dfdiff4 = dfdiff4.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfdiff4 = dfdiff4[dfdiff4.columns.drop('15y')]
dfdiff4 = dfdiff4.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfdiff4=dfdiff4.round(1)
dfdiff4 = dfdiff4.drop(index='9m', level=1)
dfdiff4 = dfdiff4.drop(index='3y', level=1)
dfdiff4 = dfdiff4.drop(index='7y', level=1)
dfdiff4 = dfdiff4.drop(index='15y', level=1)
dfdiff4 = dfdiff4.reset_index(level=1)
dfdiff4 = dfdiff4.reset_index(level=0)
dfdiff4.columns = ["Date", "Exp","1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"]
dfdiff4['Date'] = pd.to_datetime(dfdiff4['Date']).dt.date
dfdiff4['Date'] = pd.to_datetime(dfdiff4['Date']).dt.strftime('%d/%m/%y')

#zscore of implied vols
dfzs = dfdiff3.head(66)
#cols = dfzs.columns
#cols.remove('fistcolumn')
#for col in cols:
    #dfzs[col] = dfzs[col].astype(float)
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

#translating into grid format for fwds
dfdifff3 = dfdifff2.set_index('Date')
dfdifff3 = dfdifff3[dfdifff3.columns.drop('Year')]
header=[["a1m", "a1m", "a1m", "a1m", "a1m", "a1m", "a1m", "a1m", "a1m","b3m", "b3m",
                          "b3m", "b3m", "b3m", "b3m", "b3m", "b3m", "b3m", "c6m", "c6m", "c6m", "c6m",
                          "c6m", "c6m", "c6m", "c6m", "c6m","d9m", "d9m", "d9m", "d9m",
                          "d9m", "d9m", "d9m", "d9m", "d9m", "e1y", "e1y", "e1y", "e1y", "e1y", "e1y",
                          "e1y", "e1y", "e1y","f2y", "f2y", "f2y", "f2y",
                          "f2y", "f2y", "f2y", "f2y", "f2y","g3y", "g3y", "g3y", "g3y",
                          "g3y", "g3y", "g3y", "g3y", "g3y","h5y", "h5y", "h5y", "h5y",
                          "h5y", "h5y", "h5y", "h5y", "h5y","i7y", "i7y", "i7y", "i7y",
                          "i7y", "i7y", "i7y", "i7y", "i7y","j10y", "j10y", "j10y", "j10y",
                          "j10y", "j10y", "j10y", "j10y", "j10y","k15y", "k15y", "k15y", "k15y",
                          "k15y", "k15y", "k15y", "k15y", "k15y","l20y", "l20y", "l20y", "l20y",
                          "l20y", "l20y", "l20y", "l20y", "l20y"],["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y","1y", "2y",
                          "3y", "5y", "7y", "10y", "15y", "20y", "30y", "1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y", "1y", "2y", "3y", "5y", "7y", "10y",
                          "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y","1y", "2y", "3y", "5y",
                          "7y", "10y", "15y", "20y", "30y"]]
dfdifff3.columns = header
dfdifff4 = dfdifff3.loc[reversed(dfdifff3.index)]
dfdifff4 = dfdifff3.loc[reversed(dfdifff3.index)]
dfdifff4 =dfdifff4.stack(level=0)
dfdifff4 = dfdifff4.reindex(columns=["1y", "2y", "3y", "5y", "7y", "10y", "15y", "20y", "30y"])
dfdifff4 = dfdifff4[dfdifff4.columns.drop('15y')]
dfdifff4 = dfdifff4.rename(index={'a1m': '1m', 'b3m': '3m','c6m': '6m', 'd9m': '9m', 'e1y': '1y', 'f2y': '2y', 'g3y': '3y', 'h5y': '5y',
                     'i7y': '7y', 'j10y': '10y', 'k15y': '15y', 'l20y': '20y'})
dfdifff4=dfdifff4.round(2)
dfdifff4 = dfdifff4.drop(index='9m', level=1)
dfdifff4 = dfdifff4.drop(index='3y', level=1)
dfdifff4 = dfdifff4.drop(index='7y', level=1)
dfdifff4 = dfdifff4.drop(index='15y', level=1)
dfdifff4 = dfdifff4.reset_index(level=1)
dfdifff4 = dfdifff4.reset_index(level=0)
dfdifff4.columns = ["Date", "Exp","1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"]
dfdifff4['Date'] = pd.to_datetime(dfdifff4['Date']).dt.date
dfdifff4['Date'] = pd.to_datetime(dfdifff4['Date']).dt.strftime('%d/%m/%y')

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
    {"field": "30y","filter": False, "cellClass": "bg-danger bg-gradient bg-opacity-15"}]

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
    rowData=dfdiff4.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 460, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid1 = dag.AgGrid(
    id="quickstart-grid",
    columnDefs=columnDefs,
    rowData=dfdifff4.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 460, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

grid2 = dag.AgGrid(
    id="quickstart-grid",
    columnDefs=columnDefs,
    rowData=dfzs.to_dict("records"),
    #columnSize="autoSize",
    defaultColDef=defaultColDef,
    style={"height": 270, "width": 460, "font-size": '10px'},
    dashGridOptions = {"rowHeight": 25},
    className="ag-theme-balham"
)

dropdown = html.Div([
    html.P("Select vol spread to plot"),
    dcc.Dropdown(
                    id="vol-dropdown1",
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

dropdown1 = html.Div([
    html.P("Select vol spread to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown2",
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

slide1 = html.Div([
    html.P("Select Lookback:"),
    dcc.Slider(
        dfdiff2['Year'].min(),
        dfdiff2['Year'].max(),
        step=None,
        value=dfdiff2['Year'].min(),
        marks={str(year): str(year) for year in dfdiff2['Year'].unique()},
        id='year-slider'),
])

graph = dcc.Graph(id='xmkt1',style={"height": 450, "width": 700})
graph1 = dcc.Graph(id='xmkt2',style={"height": 450, "width": 700})
graph2 = dcc.Graph(id='xmkt3',style={"height": 550, "width": 1400})
graph3 = dcc.Graph(id='xmkt4',style={"height": 550, "width": 1400})
@callback(Output("xmkt1", "figure"),
          Input("vol-dropdown1", "value"),Input('year-slider', 'value'))
def update_figure(vol, selected_year):
    dffilt = dfdiff2[dfdiff2.Year >= selected_year]
    trace1 = go.Scatter(x=dffilt['Date'],
                        y=dfvol[vol],
                        name='EUR '+vol+' Implied Vol',
                        yaxis='y1')
    trace2 = go.Scatter(x=dffilt['Date'],
                        y=dfuvol[vol],
                        name='USD '+vol+' Implied Vol',
                        yaxis='y1')
    trace3 = go.Scatter(x=dffilt['Date'],
                        y=dffilt[vol],
                        name='USD - EUR '+vol+' Imp Vol',
                        yaxis='y1')
    trace4 = go.Scatter(x=dffilt['Date'],
                        y=dffwd[vol],
                        name='EUR ' + vol + ' Fwd',
                        yaxis='y2')
    trace5 = go.Scatter(x=dffilt['Date'],
                        y=dfufwd[vol],
                        name='USD ' + vol + ' Fwd',
                        yaxis='y2')
    trace6 = go.Scatter(x=dffilt['Date'],
                        y=dfdifff2[vol],
                        name='USD - EUR ' + vol + ' Fwd',
                        yaxis='y2')
    trace7 = go.Scatter(x=dffilt['Date'],
                        y=dfdswap[vol],
                        name='EUR ' + vol + ' Realised Vol',
                        yaxis='y1')
    trace8 = go.Scatter(x=dffilt['Date'],
                        y=dfudswap[vol],
                        name='USD ' + vol + ' Realised Vol',
                        yaxis='y1')
    trace9 = go.Scatter(x=dffilt['Date'],
                        y=dfrdifff2[vol],
                        name='USD - EUR ' + vol + ' Real Vol',
                        yaxis='y1')
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9]
    layout = go.Layout(yaxis=dict(title='Vol'),
                       yaxis2=dict(title='Fwd',
                                   overlaying='y',
                                   side='right'))
    xmkt1 = go.Figure(data=data, layout=layout)
    xmkt1.update_layout(
        font=dict(size=10))
    return xmkt1

@callback(Output("xmkt2", "figure"),
          Input("vol-dropdown2", "value"),Input('year-slider', 'value'))
def update_figure(vol, selected_year):
    dffilt = dfdiff2[dfdiff2.Year >= selected_year]
    trace1 = go.Scatter(x=dffilt['Date'],
                        y=dfvol[vol],
                        name='EUR '+vol+' Implied Vol',
                        yaxis='y1')
    trace2 = go.Scatter(x=dffilt['Date'],
                        y=dfuvol[vol],
                        name='USD '+vol+' Implied Vol',
                        yaxis='y1')
    trace3 = go.Scatter(x=dffilt['Date'],
                        y=dffilt[vol],
                        name='USD - EUR ' +vol+' Imp Vol',
                        yaxis='y1')
    trace4 = go.Scatter(x=dffilt['Date'],
                        y=dffwd[vol],
                        name='EUR ' + vol + ' Fwd',
                        yaxis='y2')
    trace5 = go.Scatter(x=dffilt['Date'],
                        y=dfufwd[vol],
                        name='USD ' + vol + ' Fwd',
                        yaxis='y2')
    trace6 = go.Scatter(x=dffilt['Date'],
                        y=dfdifff2[vol],
                        name=vol + ' Fwd ',
                        yaxis='y2')
    trace7 = go.Scatter(x=dffilt['Date'],
                        y=dfdswap[vol],
                        name='EUR ' + vol + ' Realised Vol',
                        yaxis='y1')
    trace8 = go.Scatter(x=dffilt['Date'],
                        y=dfudswap[vol],
                        name='USD ' + vol + ' Realised Vol',
                        yaxis='y1')
    trace9 = go.Scatter(x=dffilt['Date'],
                        y=dfrdifff2[vol],
                        name='USD - EUR ' + vol + ' Real Vol',
                        yaxis='y1')
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9]
    layout = go.Layout(yaxis=dict(title='Vol'),
                       yaxis2=dict(title='Fwd',
                                   overlaying='y',
                                   side='right'))
    xmkt2 = go.Figure(data=data, layout=layout)
    xmkt2.update_layout(
        font=dict(size=10))
    return xmkt2

@callback(Output("xmkt3", "figure"),Input("vol-dropdown1", "value"),
          Input("vol-dropdown2", "value"),Input('year-slider', 'value'))
def update_figure(vol,vol1, selected_year):
    dffilt = dfdiff2[dfdiff2.Year >= selected_year]
    trace1 = go.Scatter(x=dffilt['Date'],
                        y=dffilt[vol],
                        name='USD - EUR '+vol+' Implied Vol',
                        yaxis='y1')
    trace2 = go.Scatter(x=dffilt['Date'],
                        y=dffilt[vol1],
                        name='USD - EUR '+vol1+' Implied Vol',
                        yaxis='y1')
    trace3 = go.Scatter(x=dffilt['Date'],
                        y=dffilt[vol]-dffilt[vol1],
                        name=vol+'-'+vol1+ ' Xmkt Vol Spread',
                        yaxis='y1')
    trace4 = go.Scatter(x=dffilt['Date'],
                        y=dfdifff2[vol],
                        name='USD - EUR ' + vol + ' Fwd',
                        yaxis='y2')
    trace5 = go.Scatter(x=dffilt['Date'],
                        y=dfdifff2[vol1],
                        name='USD - EUR ' + vol1 + ' Fwd',
                        yaxis='y2')
    trace6 = go.Scatter(x=dffilt['Date'],
                        y=dfdifff2[vol]-dfdifff2[vol1],
                        name=vol+'-'+vol1+' Xmkt Fwd Spread',
                        yaxis='y2')
    trace7 = go.Scatter(x=dffilt['Date'],
                        y=dfrdifff2[vol],
                        name='USD - EUR ' + vol + ' Realised Vol',
                        yaxis='y1')
    trace8 = go.Scatter(x=dffilt['Date'],
                        y=dfrdifff2[vol1],
                        name='USD - EUR ' + vol1 + ' Realised Vol',
                        yaxis='y1')
    trace9 = go.Scatter(x=dffilt['Date'],
                        y=dfrdifff2[vol]-dfrdifff2[vol1],
                        name= vol+'-'+vol1+' Xmkt Realised Vol Spread',
                        yaxis='y1')
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9]
    layout = go.Layout(yaxis=dict(title='Vol'),
                       yaxis2=dict(title='Fwd',
                                   overlaying='y',
                                   side='right'))
    xmkt3 = go.Figure(data=data, layout=layout)
    xmkt3.update_layout(
        font=dict(size=10))
    return xmkt3

@callback(Output("xmkt4", "figure"),Input("vol-dropdown1", "value"),
          Input("vol-dropdown2", "value"),Input('year-slider', 'value'))
def update_figure(vol,vol1, selected_year):
    dffilt = dfdiff2[dfdiff2.Year >= selected_year]
    trace1 = go.Scatter(x=dffilt['Date'],
                        y=dfvol[vol]-dfvol[vol1],
                        name=vol+'-'+vol1+ ' EUR Implied Vol',
                        yaxis='y1')
    trace2 = go.Scatter(x=dffilt['Date'],
                        y=dfuvol[vol]- dfuvol[vol1],
                        name=vol+'-'+vol1+ ' USD Implied Vol',
                        yaxis='y1')
    trace3 = go.Scatter(x=dffilt['Date'],
                        y=dffilt[vol]-dffilt[vol1],
                        name=vol+'-'+vol1+ ' Xmkt Vol Spread',
                        yaxis='y1')
    trace4 = go.Scatter(x=dffilt['Date'],
                        y=dffwd[vol]-dffwd[vol1],
                        name= vol+'-'+vol1+ ' EUR Fwd',
                        yaxis='y2')
    trace5 = go.Scatter(x=dffilt['Date'],
                        y=dfufwd[vol] - dfufwd[vol1],
                        name=vol + '-' + vol1 + ' USD Fwd',
                        yaxis='y2')
    trace6 = go.Scatter(x=dffilt['Date'],
                        y=dfdifff2[vol]-dfdifff2[vol1],
                        name=vol+'-'+vol1+' Xmkt Fwd Spread',
                        yaxis='y2')
    trace7 = go.Scatter(x=dffilt['Date'],
                        y=dfdswap[vol] - dfdswap[vol1],
                        name=vol + '-' + vol1 + ' EUR Realised Vol',
                        yaxis='y1')
    trace8 = go.Scatter(x=dffilt['Date'],
                        y=dfudswap[vol] - dfudswap[vol1],
                        name=vol + '-' + vol1 + ' USD Realised Vol',
                        yaxis='y1')
    trace9 = go.Scatter(x=dffilt['Date'],
                        y=dfrdifff2[vol]-dfrdifff2[vol1],
                        name= vol+'-'+vol1+' Xmkt Realised Vol Spread',
                        yaxis='y1')
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9]
    layout = go.Layout(yaxis=dict(title='Vol'),
                       yaxis2=dict(title='Fwd',
                                   overlaying='y',
                                   side='right'))
    xmkt4 = go.Figure(data=data, layout=layout)
    xmkt4.update_layout(
        font=dict(size=10))
    return xmkt4

dash.register_page(__name__)
layout = dbc.Container([
    dbc.Row([dbc.Col(html.Div('USD - EUR Implied Vol')),
             dbc.Col(html.Div('USD - EUR Fwd Rates')),
             dbc.Col(html.Div('3m Implied Vol Spread Z-score'))]),
    dbc.Row([dbc.Col(grid),
            dbc.Col(grid1),
            dbc.Col(grid2)]),
    dbc.Row([dbc.Col(dropdown),
             dbc.Col(dropdown1),]),
    dbc.Row([dbc.Col(graph),
             dbc.Col(graph1)]),
    dbc.Row([dbc.Col(slide1),]),
    dbc.Row([dbc.Col(graph2),]),
    dbc.Row([dbc.Col(graph3),]),
], fluid=True)'''))
