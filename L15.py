# Estimated value using linear()

import pandas as pd

data = { 
    "Time":[1,2,3,4,5,6],
    "Value":[10,20,None,40,None,60]
    }

df = pd.DataFrame(data)
print(df)
print("----------------------------------------------------------------------------------------------------------------------------------------")

df['Value'] = df['Value'].interpolate(method='linear')
print(df)                 # => it is only used in numerical data

            # =>    Time  Value
            # => 0     1   10.0
            # => 1     2   20.0
            # => 2     3   30.0
            # => 3     4   40.0
            # => 4     5   50.0
            # => 5     6   60.0 
