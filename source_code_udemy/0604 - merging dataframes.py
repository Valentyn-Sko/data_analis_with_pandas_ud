import pandas as pd

df1 = pd.DataFrame({'Temp': [75, 73, 72, 76],
                    'Humidity': [30, 45, 32, 42],
                    'Precip': [0, 0, 0, 1], })

df2 = pd.DataFrame({'Temp': [75, 73, 72, 76],
                    'Wind': [33, 35, 37, 23],
                    'Cloudy': [1, 0, 1, 1], })

print(pd.merge(df1, df2, on='Temp'))

main_users = pd.DataFrame({'Username': ['James', 'Sanjay', 'Karl', 'Kelly'],
                           'Password': ['P@ssw0rd', '1234', 'pass', 'pw'],
                           'Join_Date': ['Jan', 'Feb', 'Jan', 'March'], })

forum_users = pd.DataFrame({'Username': ['James', 'Sanjay', 'Karl', 'Kelly'],
                            'Post_Count': [500, 521, 76, 888],
                            'User_Status': [0, 1, 0, 2], })

print(pd.merge(main_users, forum_users, on='Username'))
