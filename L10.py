# Updating values

import pandas as pd

data ={
    "Name" : ['Ram','Shyam','Amit','Aditi','Karan','Aditya','Sonia'],
    "Age" : [25,21,36,28,48,19,20],
    "Salary":[45000,52000,60000,49000,75000,30000,31000],
    "Performance Score":[85,79,82,87,98,92,80]
}                                                              #  small data set 

df = pd.DataFrame(data)

df.loc[5,'Salary'] = 35000
df.loc[2,'Salary'] = 61000
print(df)

df['Salary'] = df['Salary']*1.05
print(df)