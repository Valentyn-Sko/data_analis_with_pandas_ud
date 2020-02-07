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

##df['Pct_Diff_bot_5_vs_Top_5_again'] = ((df['Top fifth'] - df['Bottom fifth']) / df['Bottom fifth']) * 100
##print(df.head())

df['Pct_Diff_mid_5_vs_top_5'] = list(map(pct_diff, df['Middle fifth'], df['Top fifth']))
df['Pct_Diff_4th_5_vs_top_5'] = list(map(pct_diff, df['Fourth fifth'], df['Top fifth']))
df['Pct_Diff_2nd_5_vs_top_5'] = list(map(pct_diff, df['Second fifth'], df['Top fifth']))






df['Pct_Diff_bot_5_vs_Top_5'].plot(label='Bottom 5th')
df['Pct_Diff_mid_5_vs_top_5'].plot(label='Middle 5th')
df['Pct_Diff_4th_5_vs_top_5'].plot(label='Fourth 5th')
df['Pct_Diff_2nd_5_vs_top_5'].plot(label='Second 5th')
plt.legend(loc=6)
plt.show()


















    
