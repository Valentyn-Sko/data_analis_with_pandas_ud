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


df2 = df.resample('3D', how='mean')
print(df2.head())

df3 = df.resample('1M', how='mean')
print(df3.head())

df4 = df.resample('12M', how='mean')
print(df4.head())

df2['Adjusted Close'].plot()
df3['Adjusted Close'].plot()
df4['Adjusted Close'].plot()
df['Adjusted Close'].plot()
plt.show()

