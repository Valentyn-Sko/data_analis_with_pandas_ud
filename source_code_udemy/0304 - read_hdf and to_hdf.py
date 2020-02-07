import pandas as pd

df = pd.read_csv('newcsv4.csv', names=['Date', 'Violent_Crime_Rate'], index_col = 0)
print(df.head())

store = pd.HDFStore('hdfstore.h5')
print(store)

store.put('d1', df, format='table', data_columns=True)

print(store['d1'].shape)
store.close()

hdf = pd.read_hdf('hdfstore.h5','d1')

print(hdf)


