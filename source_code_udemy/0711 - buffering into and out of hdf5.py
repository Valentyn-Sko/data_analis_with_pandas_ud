import pandas as pd


def buffering_example():
    with open('btceUSD.csv', buffering=1500) as f:
        for line in f:
            print(line)


# buffering_example()
def buffering_with_pandas():
    chunks = pd.read_csv('btceUSD.csv', chunksize=4)
    for c in chunks:
        print(c)


# buffering_with_pandas()
def no_buffering_pandas():
    df = pd.read_csv('btceUSD.csv')
    print(df.head())


# no_buffering_pandas()


def create_hdf_file():
    store = pd.HDFStore('hdfbuffering.h5')
    chunks = pd.read_csv('btceUSD.csv', chunksize=400000, names=['Unix', 'Price', 'Volume'], index_col=0)

    for c in chunks:
        store.append('df', c, format='table')

#create_hdf_file()
hdf = pd.read_hdf('hdfbuffering.h5', 'df', chunksize=4000)
for c in hdf:
    print(c)

hdf = pd.read_hdf('hdfbuffering.h5', 'df')
print(hdf.head())
