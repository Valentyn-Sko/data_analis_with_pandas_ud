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

##att['High'].plot()
##att['Low'].plot()

att[['High','Low']].plot()
plt.legend()
plt.show()

att.plot()
plt.legend()
plt.show()




