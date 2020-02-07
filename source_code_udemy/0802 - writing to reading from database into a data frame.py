import pandas as pd
import sqlite3

def populate_DB():
    chunks = pd.read_csv('btceUSD.csv', chunksize=400000)
    for chunk in chunks:
        chunk.columns = ['Unix', 'Price', 'Volume']
        with sqlite3.connect('tutorial.db') as conn:
            chunk.to_sql('Bitcoin', conn, if_exists= 'append')

#populate_DB()

def pull_from_DB():
    with sqlite3.connect('tutorial.db') as conn:
        df = pd.read_sql('SELECT * FROM Bitcoin LIMIT 1000000', con=conn, index_col="index",columns = ['unix','price','volume'])

    return df
df = pull_from_DB()

print(df.head())

            
            

