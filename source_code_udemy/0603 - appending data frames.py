import pandas as pd

df1 = pd.DataFrame({'Temp': [75, 73, 72, 76],
                    'Humidity': [30, 45, 32, 42],
                    'Precip': [0, 0, 0, 1], },
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'Temp': [76, 79, 77, 77],
                    'Humidity': [33, 35, 37, 23],
                    'Precip': [1, 0, 1, 1], },
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'Temp': [77, 79, 81, 76],
                    'Humidity': [40, 42, 42, 43],
                    'Precip': [0, 1, 1, 1], },
                   index=[8, 9, 10, 11])

df4 = pd.DataFrame({'Temp': [77, 79, 81, 76],
                    'Humidity': [40, 42, 42, 43],
                    'Wind': [15, 11, 12, 13], },
                   index=[8, 9, 10, 11])

df5 = pd.DataFrame({'Pressure': [77, 79, 81, 76],
                    'Cloudy': [1, 0, 0, 1],
                    'Wind': [15, 11, 12, 13], },
                   index=[0, 1, 2, 3])

appended = df1.append(df2)
print(appended)

values = [81, 36, 0]

s = pd.Series(values, index=['Temp', 'Humidity', 'Precip'])
print(s)

df6 = df1.append(s, ignore_index=True)
print(df6)

df1.append(s, ignore_index=True)    #didn't update df1 without  =
print(df1)
