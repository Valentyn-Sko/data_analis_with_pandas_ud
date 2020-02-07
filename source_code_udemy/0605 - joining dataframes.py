import pandas as pd


df1 = pd.DataFrame({'Temp':[75, 73, 72, 76],
                    'Humidity':[30,45,32,42],
                    'Precip':[0,0,0,1],})

df2 = pd.DataFrame({'Temp':[75, 73, 72, 76],
                    'Wind':[33,35,37,23],
                    'Cloudy':[1, 0, 1, 1],})


print(pd.merge(df1,df2, on='Temp'))

main_users = pd.DataFrame({'Username':['James','Sanjay','Karl','Kelly','Carl'],
                           'Password':['P@ssw0rd','1234','pass','pw','2rfj2jf2'],
                           'Join_Date':['Jan','Feb','Jan','March','April'],})

forum_users = pd.DataFrame({'Username':['James','Sanjay','Karl','Kelly'],
                           'Post_Count':[500,521,76,888],
                           'User_Status':[0,1,0,2],})

print(pd.merge(main_users, forum_users, on='Username'))

main_users.set_index('Username', inplace = True)
forum_users.set_index('Username', inplace = True)

joined = main_users.join(forum_users)
print(joined)


main_users = pd.DataFrame({'Username':['James','Sanjay','Karl','Kelly','Carl'],
                           'Password':['P@ssw0rd','1234','pass','pw','2rfj2jf2'],
                           'Join_Date':['Jan','Feb','Jan','March','April'],})

forum_users = pd.DataFrame({'Username':['James','Sanjay','Karl','Kelly'],
                           'Post_Count':[500,521,76,888],
                           'User_Status':[0,1,0,2],})



merged = pd.merge(main_users, forum_users, on='Username')
merged.set_index('Username', inplace = True)
print(merged)

merged = pd.merge(main_users, forum_users, on='Username', how='left')
merged.set_index('Username', inplace = True)
print(merged)









