# Missing data

import pandas as pd

data ={
    "Name" : ['Ram',None,'Amit','Aditi','Karan','Aditya','Sonia'],
    "Age" : [25,36,28,None,48,19,20],
    "Salary":[45000,60000,49000,75000,None,30000,31000],
    "Performance Score":[85,None,82,87,98,92,80]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull())

print(df.isnull().sum())

