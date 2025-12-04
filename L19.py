# Merging

import pandas as pd 

#customer dataframe

customerdata = {
    'CustomerId' : [1,2,3,4],
    'Name' : ['Ramesh','Suresh','Kalpesh','Jagesh']
}
df1 = pd.DataFrame(customerdata)

orders = {
    'CustomerId' : [1,2,3,5],
    'OrderAmount' : [250,367,267,458]
}
df2 = pd.DataFrame(orders)

df_merge = pd.merge(df1,df2, on= "CustomerId",how= "inner")
print(df_merge)
        # =>    CustomerId     Name  OrderAmount
        # => 0           1   Ramesh          250
        # => 1           2   Suresh          367
        # => 2           3  Kalpesh          267

df_merge1 = pd.merge(df1,df2, on= "CustomerId",how= "outer")
print(df_merge1)
        # =>    CustomerId     Name  OrderAmount
        # => 0           1   Ramesh        250.0
        # => 1           2   Suresh        367.0
        # => 2           3  Kalpesh        267.0
        # => 3           4   Jagesh          NaN
        # => 4           5      NaN        458.0

df_merge2 = pd.merge(df1,df2, on= "CustomerId",how= "left")
print(df_merge2)
        # =>    CustomerId     Name  OrderAmount
        # => 0           1   Ramesh        250.0
        # => 1           2   Suresh        367.0
        # => 2           3  Kalpesh        267.0
        # => 3           4   Jagesh          NaN

df_merge3 = pd.merge(df1,df2, on= "CustomerId",how= "right")
print(df_merge3)
        # =>    CustomerId     Name  OrderAmount
        # => 0           1   Ramesh          250
        # => 1           2   Suresh          367
        # => 2           3  Kalpesh          267
        # => 3           5      NaN          458

#cross