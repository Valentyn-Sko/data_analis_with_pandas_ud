import pandas as pd

starting = {'Col_1':[5,2,4,7],
            'Col_2':[7,8,2,1],
            'Col_3':[10,4,2,1],
            'Col_4':[5,6,7,1],
            'Col_5':[9,9,2,1],
            'Col_6':[7,8,2,1],}

df = pd.DataFrame(starting)
print(df)
print(df.dtypes)
print(df['Col_1'][0])
print(df.Col_1)


