# Adding columns

import pandas as pd

data ={
    "Name" : ['Ram','Shyam','Amit','Aditi','Karan','Aditya','Sonia'],
    "Age" : [25,21,36,28,48,19,20],
    "Salary":[45000,52000,60000,49000,75000,30000,35000],
    "Performance Score":[85,79,82,87,98,92,80]
}

df = pd.DataFrame(data)

df["Bonus"] = df['Salary']*0.1
print(df)

#using insert()

df.insert(0,"Employee No.",[1,2,3,4,5,6,7])
print(df)

df.insert(3,"City",['Nagpur','Mumbai','Delhi','Panjab','UP','Bihar','Kolkata'])
print(df)