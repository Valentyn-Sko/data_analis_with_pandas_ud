import pandas as pd
import pandas.io.data as web
import datetime

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 1, 1)

att = web.DataReader("T", 'yahoo', start, end)

#print(att.head())
#print(50*"#")
describe = att.describe()
#print(describe)
#print(describe['Open'])
print(describe['Open']['std'])



















