import pandas as pd
import datetime
import pandas.io.data as web

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 7, 28)

att = web.DataReader("T", "yahoo", start, end)

print(att.head())

highs = att['High'].tolist()
print(highs[-10])

highz = att['High'][-10]
#print(highz[-10])




