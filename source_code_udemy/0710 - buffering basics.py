import pandas as pd


# http://api.bitcoincharts.com/v1/trades.csv?symbol=SYMBOL[&start=UNIXTIME]
#http://api.bitcoincharts.com/v1/csv/


def buffering_example():
    with open('btceUSD.csv', buffering=1500) as f:
        for line in f:
            print(line)


buffering_example()


def buffering_with_pandas():
    chunks = pd.read_csv('btceUSD.csv', chunksize=4)
    for c in chunks:
        print(c)


# buffering_with_pandas()


def no_buffering_pandas():
    df = pd.read_csv('btceUSD.csv')
    print(df.head())


no_buffering_pandas()
