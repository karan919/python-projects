import pandas as pd
import numpy as np

# Create dictionary
dictionary = { "Name": ["-", "Mike", "John", "Dave", "Joey"],"Height(m)": [1.75, 1.65, 1.73, np.nan, 1.82],"Score": [70, np.nan, 84, 62, 73] }

#Convert dictionary to dataframe
df = pd.DataFrame(dictionary)
print(df)

print("\nShow Missing values")
print(df.isnull().sum())

# print("\nDeal with missing values")
# df = df.fillna('*')
# print(df)

# print("\nDeal with missing values by adding mean value")
# df["Score"] = df["Score"].fillna(df["Score"].mean())
# print(df)

# print("\n Delete row with missing values")
# df= df.dropna() 
# print(df)

# print("\n Dealing with non stantard values")
df = df.replace(['-','na'], np.nan)
df = df.fillna('*')
print(df)