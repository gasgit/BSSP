import pandas as pd

df = pd.DataFrame()
x = ['blue', 'green','red', 'yellow']
df["Colors"] = x

print(df)

import json

data = df.to_json()

with open('data.json', 'w') as outfile:  
    json.dump(data, outfile)

writer = pd.ExcelWriter('colors.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()