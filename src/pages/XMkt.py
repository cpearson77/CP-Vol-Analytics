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

dropdown1 = html.Div([
    html.P("Select vol spread to plot:"),
    dcc.Dropdown(
                    id="vol-dropdown2",
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
                        name='USD - EUR '+vol+' Implied Vol',
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
    dbc.Row([dbc.Col(graph2),
             ]),
], fluid=True)