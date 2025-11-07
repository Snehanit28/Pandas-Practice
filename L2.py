import pandas as pd

data ={
    "Name" : ['Ram','Shyam','Amit'],
    "Age" : [10,20,30],
    "City" : ['Nagpur','Mumbai','Delhi']
}

df = pd.DataFrame(data)
print(df)
            #     Name  Age    City
            # 0    Ram   10  Nagpur
            # 1  Shyam   20  Mumbai
            # 2   Amit   30   Delhi

df.to_csv("Output.csv", index = False) # it creates a new csv file in our folder, here Output is the name of this csv file and index=False remove the inex(0,1,2) from the data
# For excel file we wrote df.to_excel("Output.xlsx", index = False)
# For json file we wrote df.to_json("Output.json", index = False)


#  Output.csv ---

# Name,Age,City
# Ram,10,Nagpur
# Shyam,20,Mumbai
# Amit,30,Delhi