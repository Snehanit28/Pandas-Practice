# Filtering rows based on some condition

import pandas as pd

data ={
    "Name" : ['Ram','Shyam','Amit','Aditi','Karan','Aditya','Sonia'],
    "Age" : [25,21,36,28,48,19,20],
    "City" : ['Nagpur','Mumbai','Delhi','Panjab','UP','Bihar','Kolkata'],
    "Salary":[45000,52000,60000,49000,75000,30000,35000],
    "Performance Score":[85,79,82,87,98,92,80]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary']>50000]
print(high_salary)

# Using AND condition

filtered_and = df[(df['Age']>30) & (df['Salary']>50000)]
print(filtered_and)

# Using OR condition

filtered_or = df[(df['Age']>35) | (df['Performance Score']>90)]
print(filtered_or)