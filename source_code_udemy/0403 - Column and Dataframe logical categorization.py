import pandas as pd
import pandas.io.data as web
import datetime

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 1, 1)

att = web.DataReader("T", 'yahoo', start, end)

print(att.head())
print(50 * "#")

att['Daily_Rise'] = att['Close'] > att['Open']
print(att.head())

att2 = att[(att['Close'] > att['Open'])]

print(att2.head())

att['HL'] = att['High'] - att['Low']

att3 = att[(att['HL'] > 1)]

print(att3.head())
