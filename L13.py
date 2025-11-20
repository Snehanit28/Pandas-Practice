#  Handling missing data using dropna()

import pandas as pd

data ={
    "Name" : ['Ram',None,'Amit','Aditi','Karan','Aditya','Sonia'],
    "Age" : [25,36,28,None,48,19,20],
    "Salary":[45000,60000,49000,75000,None,30000,31000],
    "Performance Score":[85,None,82,87,98,92,80]
}

df = pd.DataFrame(data)
print(df)
                # =>     Name    Age   Salary  Performance Score
                # => 0   Ram    25.0  45000.0               85.0
                # => 1   None   36.0  60000.0                NaN
                # => 2   Amit   28.0  49000.0               82.0
                # => 3   Aditi   NaN  75000.0               87.0
                # => 4   Karan  48.0      NaN               98.0
                # => 5  Aditya  19.0  30000.0               92.0
                # => 6   Sonia  20.0  31000.0               80.0
print('--------------------------------------------------------------------------------------------------------------------------------')
df.dropna(inplace=True)
print(df)                #remove which have missing values

                # =>     Name    Age   Salary  Performance Score
                # => 0   Ram    25.0  45000.0               85.0
                # => 2   Amit   28.0  49000.0               82.0
                # => 5  Aditya  19.0  30000.0               92.0
                # => 6   Sonia  20.0  31000.0               80.0
print('--------------------------------------------------------------------------------------------------------------------------------')
df.dropna(axis=0,inplace=True)
print(df)               #remove rows which have missing values
print('--------------------------------------------------------------------------------------------------------------------------------')
df.dropna(axis=1,inplace=True)
print(df)               #remove columns which have missing values
print('--------------------------------------------------------------------------------------------------------------------------------')