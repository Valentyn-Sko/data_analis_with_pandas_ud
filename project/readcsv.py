import pandas as pd

df = pd.read_csv('test.csv')
print(df.head())
df = df.set_index('State')
df['City'].to_csv('new_csv2.csv')

df = pd.read_csv('new_csv2.csv', names=['State', 'City'], index_col=0)
print(df.head())


