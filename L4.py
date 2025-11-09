import pandas as pd

df = pd.read_csv("./sales_data_sample.csv", encoding="latin1")

print(df.info())   # Display the data set of info

print("-----------------------------------------------------------------------------------------------------------------------------------------------")


data ={
    "Name" : ['Ram','Shyam','Amit'],
    "Age" : [10,20,30],
    "City" : ['Nagpur','Mumbai','Delhi']
}

df1 = pd.DataFrame(data)

print(df1.info())