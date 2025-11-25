# Sorting data in multiline columns

import pandas as pd

data = {
    "Name" : ['Ram','Shyam','Amit','Aditi','Karan','Aditya','Sonia'],
    "Age" : [25,21,36,28,48,19,20],
    "Salary":[55000,50000,60000,39000,75000,50000,31000]
}
df = pd.DataFrame(data)

df.sort_values(by="Age", ascending=False, inplace=True)   # => sorted  by descending order
print(df)

df.sort_values(by=["Age","Salary"], ascending=[True,False], inplace=True)   # => sorted  by descending order
print(df)
