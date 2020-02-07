import pandas as pd
import urllib.request

df = pd.read_csv('test.csv')

print(df.head())

df['City'].to_json('example_json.json')
# print(df['City'])
df2 = pd.read_json('example_json.json', typ='series')
print(df2.head())

# bad link
depth_json = urllib.request.urlopen('https://btc-e.com/api/3/depth/btc_usd').read()
depth_json = pd.read_json(depth_json)
print(depth_json)
