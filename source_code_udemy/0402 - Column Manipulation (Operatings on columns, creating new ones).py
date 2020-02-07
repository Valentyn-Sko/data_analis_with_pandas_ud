import pandas as pd
import pandas_datareader as web
import datetime

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 1, 1)

att = web.DataReader("T", 'yahoo', start, end)

print(att.head())
print(50*"#")
att['Open_original'] = att['Open']
att['High'] = att['High'] / 10

print(att.head())

att['High_minus_low'] = att['High'] - att['Low']

print(att.head())











