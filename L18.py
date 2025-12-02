# Use of mean(),max(),min(),sum()

import pandas as pd


data = {
    "Name" : ['Ram','Shyam','Amit','Aditi','Karan','Aditya','Sonia'],
    "Age" : [28,21,36,28,48,19,20],
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
            # => 28    94000
            # => 36    60000
            # => 48    75000
            # => Name: Salary, dtype: int64# => 19    50000

grouped1 = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped1)
            # => Age  Name  
            # => 19   Aditya    50000
            # => 20   Sonia     31000
            # => 21   Shyam     50000
            # => 28   Aditi     39000
            # =>      Ram       55000
            # => 36   Amit      60000
            # => 48   Karan     75000
            # => Name: Salary, dtype: int64
