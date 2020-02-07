import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

bridge_readings = {'Distance_mm': [50012, 50015, 50009, 5024012, 50007, 50016, 50014]}

df = pd.DataFrame(bridge_readings)
#df.plot()
#plt.show()
# rolmean = timeseries.rolling(window=24).mean() # 24 hours on each day
#    rolstd = timeseries.rolling(window=24).std()
#
stats = df.describe()
print(stats)
print(stats.Distance_mm['std'])
#            df.rolling(2).std()
#df['std'] = pd.rolling_std(df['Distance_mm'], 2)
df['std'] = df['Distance_mm'].rolling(2).std()
#
print(df.head())
#
df = df[(df['std'] < 50)]
#
print(df.head())
#
df['Distance_mm'].plot()
plt.show()
#
