import pandas as pd

df = pd.read_csv('new_csv2.csv', names = ['State_', 'City_'], index_col=0)
#print(df.head())

store = pd.HDFStore('hdfstore.h5')
store.put('d1',df,format = 'table', data_colums=True)
#print(store['d1'].shape)
store.close()

hdf =pd.read_hdf('hdfstore.h5','d1')
print(hdf.head())