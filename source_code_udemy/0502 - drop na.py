import pandas as pd
import pandas.io.data as web
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean


def moving_average(data):
    return mean(data)

def fancy_this(data):
    return mean(data) + mean(data) + 5

style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 1, 1)

att = web.DataReader("T", 'yahoo', start, end)
describe = att.describe()
#print(describe['Open']['std'])

att['50MA'] = pd.rolling_mean(att['Close'], 50)
att['10MA'] = pd.rolling_mean(att['Close'], 10)
att['50STD'] = pd.rolling_std(att['Close'], 50)
att['MA_with_apply'] = pd.rolling_apply(att['Close'], 50, moving_average)
att['apply'] = pd.rolling_apply(att['Close'], 50, fancy_this)

print(att.head())

#att.dropna(inplace=True)

att.dropna(how='all', inplace=True)
print(att.head())




















