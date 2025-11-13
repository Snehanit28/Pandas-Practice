import pandas as pd

data = {
    "Name" : ['Ram','Shyam','Amit','Aditi','Karan','Aditya','Sonia'],
    "Age" : [25,21,36,28,48,19,20],
    "City" : ['Nagpur','Mumbai','Delhi','Panjab','UP','Bihar','Kolkata'],
    "Salary":[45000,52000,60000,49000,75000,30000,35000],
    "Performance Score":[85,79,82,87,98,92,80]
}
df = pd.DataFrame(data)

print(f'Shape : {df.shape}')        # => Shape : (7, 5)
print(df.columns)      # => Index(['Name', 'Age', 'City', 'Salary', 'Performance Score'], dtype='object')
