# # Pandas = Data ko control karne ka tool
# # STEP 1: Pandas import + basic structure
# import pandas as pd 

# # STEP 2: Series kya hoti hai
# # series = 1D data (single coloumn )
# s = pd.Series([10,20,30,40,50])
# print(s)

# # STEP 3: DataFrame
# # DataFrame = table (rows + columns)

# data = {
#     "Name": ["swati","sweta","geeta","anita"],
#     "Age": [28, 29, 26, 25]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())

import pandas as pd 

df = pd.read_excel("/mnt/c/Users/ewgpasu/OneDrive - Ericsson/Desktop/data.xlsx")
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)