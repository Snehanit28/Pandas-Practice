# Sorting data in single coloumn

import pandas as pd

data = {
    "Name" : ['Ram','Shyam','Amit','Aditi','Karan','Aditya','Sonia'],
    "Age" : [25,21,36,28,48,19,20],
    "Salary":[45000,52000,60000,49000,75000,30000,31000]
}
df = pd.DataFrame(data)

df.sort_values(by='Age', ascending=False, inplace=True)   # => sorted 'Age' by descending order
print(df)
                # =>      Name  Age  Salary
                # => 4   Karan   48   75000
                # => 2    Amit   36   60000
                # => 3   Aditi   28   49000
                # => 0     Ram   25   45000
                # => 1   Shyam   21   52000
                # => 6   Sonia   20   31000
                # => 5  Aditya   19   30000
print("----------------------------------------------------------------------------------------------------------------------------------------")
df.sort_values(by='Age', ascending=True, inplace=True)   # => sorted 'Age' by ascending order
print(df)
                # =>      Name  Age  Salary
                # => 5  Aditya   19   30000
                # => 6   Sonia   20   31000
                # => 1   Shyam   21   52000
                # => 0     Ram   25   45000
                # => 3   Aditi   28   49000
                # => 2    Amit   36   60000
                # => 4   Karan   48   75000
print("----------------------------------------------------------------------------------------------------------------------------------------")
