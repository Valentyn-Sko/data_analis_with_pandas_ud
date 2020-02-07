import pandas as pd
import datetime
import pandas_datareader as web

import matplotlib.pyplot as plt
from matplotlib import style

# starting = {'Col_1': [5, 2, 4, 7],
#            'Col_2': [7, 8, 2, 1],
#            'Col_3': [10, 4, 2, 1],
#            'Col_4': [5, 6, 7, 1],
#            'Col_5': [9, '9', 2, 1],
#            'Col_6': [7, 8, 2, 1],
#            'Name': [1, 2, 3, 4]}
#
# df = pd.DataFrame(starting)
# print(df.head())
#
# print(df.index)
# print(df.set_index('Name'))


style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 6, 4)

att = web.DataReader('T', 'yahoo', start, end)

print(att.head())

# att['Adj Close'].plot()
att[['High', 'Low']].plot()
plt.legend()
plt.show()
