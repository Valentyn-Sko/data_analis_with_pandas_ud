import pandas as pd

df = pd.read_csv('FBI-CRIME11.csv')

df['Violent Crime Rate'].to_csv('newcsv2.csv')

df.set_index('Year', inplace = True)

df['Violent Crime Rate'].to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
print(df.head())

df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

df = pd.read_csv('newcsv2.csv', names = ['Date','Violent Crime Rate'], index_col=0)
print(df.head())


df.to_csv('newcsv3.csv')

df.to_csv('newcsv4.csv', header=False)
