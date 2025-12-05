# Concatenation

import pandas as pd

df_Region1 = pd.DataFrame({
    'CustomerId':[1,2],
    'Name':["Gopal","Raju"]
})
df_Region2 = pd.DataFrame({
    'CustomerId':[3,4],
    'Name':["Shyam","Ram"]
})
df_concat = pd.concat([df_Region1,df_Region2],ignore_index=True)
print(df_concat)
        # =>    CustomerId   Name
        # => 0           1  Gopal
        # => 1           2   Raju
        # => 2           3  Shyam
        # => 3           4    Ram

df_concat1 = pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)
print(df_concat1)
        # =>    0      1  2      3
        # => 0  1  Gopal  3  Shyam
        # => 1  2   Raju  4    Ram
