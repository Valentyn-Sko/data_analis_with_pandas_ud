import pandas as pd
import urllib.request

import matplotlib.pyplot as plt

def pickle_data():
    read = urllib.request.urlopen('https://www.quandl.com/api/v1/datasets/YAHOO/AAPL.csv')
    df = pd.read_csv(read)
    print(df.head())
    df.to_pickle('df.pickle')

#pickle_data()

df = pd.read_pickle('df.pickle')
df.sort('Date', inplace=True)
df.set_index('Date', inplace=True)
df = df['Adjusted Close']
print(df.head())

##df.plot()
##plt.show()


df = pd.read_pickle('df.pickle')
print(df.head())
df.sort('Open', inplace = True)
print(df.head())




