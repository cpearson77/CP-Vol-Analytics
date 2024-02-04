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
#dfswap = pd.read_excel(r"C:\Users\charl\PycharmProjects\pythonProject\master1.xlsx", sheet_name='Swaps',header=[0],index_col=[0])
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
#dfswap4['Date'] = pd.to_datetime(dfswap4['Date']).dt.date
#dfswap4['Date'] = pd.to_datetime(dfswap4['Date']).dt.strftime('%d/%m/%y')

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
#dfswap7['Date'] = pd.to_datetime(dfswap7['Date']).dt.date
#dfswap7['Date'] = pd.to_datetime(dfswap7['Date']).dt.strftime('%d/%m/%y')

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
#dfswap10['Date'] = pd.to_datetime(dfswap10['Date']).dt.date
#dfswap10['Date'] = pd.to_datetime(dfswap10['Date']).dt.strftime('%d/%m/%y')

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
dffwd4['Date'] = pd.to_datetime(dffwd4['Date']).dt.date
dffwd4['Date'] = pd.to_datetime(dffwd4['Date']).dt.strftime('%d/%m/%y')
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
                  dbc.Col(graph6)])
         ],fluid=True)