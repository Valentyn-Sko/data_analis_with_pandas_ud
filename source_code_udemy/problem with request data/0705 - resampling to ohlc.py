import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df = pd.read_pickle('df.pickle')
df.sort('Date', inplace= True)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print(df.head())


df2 = df['Adjusted Close'].resample('D', how='ohlc', fill_method='ffill')

#df2.dropna(inplace=True)

print(df2.head())

if df2.isnull().values.sum() > 1:
    print('We contain NAN data!')



