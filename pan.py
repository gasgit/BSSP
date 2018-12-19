import pandas as pd
import json

# create a new data frame
df = pd.DataFrame()
# data 
x = ['blue', 'green','red', 'yellow']
# add data to dataframe
df["Colors"] = x
# display data frame 
print(df)


# 
# export data frame to json
data = df.to_json()
# create, open and write json data to file
with open('data.json', 'w') as outfile:  
    json.dump(data, outfile)

# 
# create file with ExcelWriter 
writer = pd.ExcelWriter('colors.xlsx')
# create new sheet and export df
df.to_excel(writer, 'Sheet1')
writer.save()
