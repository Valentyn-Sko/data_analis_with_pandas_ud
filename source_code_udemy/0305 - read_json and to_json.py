import pandas as pd
import urllib.request

df = pd.read_hdf('hdfstore.h5','d1')
df.to_json('example_json.json')
df2 = pd.read_json('example_json.json')
#print(df2.head())

depth_json = urllib.request.urlopen('https://btc-e.com/api/3/depth/btc_usd').read()

depth_df = pd.read_json(depth_json)

print(depth_json)



