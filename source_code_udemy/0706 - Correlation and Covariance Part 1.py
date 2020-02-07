import pandas as pd
import urllib.request


#https://www.quandl.com/api/v1/datasets/FBI/CRIME11.csv

#https://www.quandl.com/api/v1/datasets/UKONS/LMS_LFN2_A.csv

#https://www.quandl.com/api/v1/datasets/ECPI/INCOME_C.csv?trim_start=1980-12-31

#https://www.quandl.com/api/v1/datasets/ODA/USA_NGDPPC.csv

def pickle_data():
    read = urllib.request.urlopen('https://www.quandl.com/api/v1/datasets/FBI/CRIME11.csv')
    df = pd.read_csv(read)
    print(df.head())
    df.to_pickle('df.pickle')

    read = urllib.request.urlopen('https://www.quandl.com/api/v1/datasets/UKONS/LMS_LFN2_A.csv')
    df = pd.read_csv(read)
    print(df.head())
    df.to_pickle('df2.pickle')

    read = urllib.request.urlopen('https://www.quandl.com/api/v1/datasets/ECPI/INCOME_C.csv?trim_start=1980-12-31')
    df = pd.read_csv(read)
    print(df.head())
    df.to_pickle('df3.pickle')

    read = urllib.request.urlopen('https://www.quandl.com/api/v1/datasets/ODA/USA_NGDPPC.csv')
    df = pd.read_csv(read)
    print(df.head())
    df.to_pickle('df4.pickle')


#pickle_data()

df = pd.read_pickle('df.pickle')
df2 = pd.read_pickle('df2.pickle')
df3 = pd.read_pickle('df3.pickle')
df4 = pd.read_pickle('df4.pickle')

print(df3.corr())

print(df.corr())



















    
