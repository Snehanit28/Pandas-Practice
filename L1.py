import pandas as pd

df = pd.read_csv("./sales_data_sample.csv", encoding = "latin1") # if without encoding through some error then we wrote encoding = "latin1" or encoding = "utf-8"
# For excel file we wrote df = pd.read_excel("./sales_data_sample.xlsx")
# For json file we wrote df = pd.read_json("./sales_data_sample.json")

print(df) 
           # 1           10121               34      81.35  ...          Henriot              Paul    Small
           # 2           10134               41      94.74  ...         Da Cunha            Daniel   Medium
           # 3           10145               45      83.26  ...            Young             Julie   Medium
           # 4           10159               49     100.00  ...            Brown             Julie   Medium
           # ...           ...              ...        ...  ...              ...               ...      ...
           # 2818        10350               20     100.00  ...           Freyre             Diego    Small
           # 2819        10373               29     100.00  ...        Koskitalo            Pirkko   Medium
           # 2820        10386               43     100.00  ...           Freyre             Diego   Medium
           # 2821        10397               34      62.24  ...           Roulet           Annette    Small
           # 2822        10414               47      65.52  ...          Yoshido              Juri   Medium