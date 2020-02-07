import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

def pct_diff(v1, v2):
    pct = ((v2-v1) / v1) * 100.0
    return pct
    
df = pd.read_pickle('df3.pickle')
df.set_index('Year', inplace=True)
df.sort_index(inplace=True)
print(df.head())

df['Pct_Diff_bot_5_vs_Top_5'] = list(map(pct_diff, df['Bottom fifth'], df['Top fifth']))
df['Pct_Diff_bot_5_vs_Top_5'].plot()
plt.show()


















    
