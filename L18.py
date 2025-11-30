# Use of mean(),max(),min(),sum()

import pandas as pd


data = {
    "Name" : ['Ram','Shyam','Amit','Aditi','Karan','Aditya','Sonia'],
    "Age" : [25,21,36,28,48,19,20],
    "Salary":[55000,50000,60000,39000,75000,50000,31000]
}
df = pd.DataFrame(data)

# avg_salary = df['Salary'].mean()
# print(avg_salary)                 # => 51428.57142857143

grouped = df.groupby("Age")["Salary"].sum()
print(grouped)
            # => Age
            # => 19    50000
            # => 20    31000
            # => 21    50000
            # => 25    55000
            # => 28    39000
            # => 36    60000
            # => 48    75000
            # => Name: Salary, dtype: int64
