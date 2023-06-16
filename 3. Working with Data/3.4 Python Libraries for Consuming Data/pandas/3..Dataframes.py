import pandas as lib

data = {
    "Calories": [420, 380, 390],
    "Duration": [50, 40, 45]
    }

# load data into dataframe object
df = lib.DataFrame(data)

print(df)
print()

# select column
print(df["Calories"])           # format : df[column_name]
print()

# set calories column as the index
df.set_index("Calories", inplace=True)
print(df)
print()

# select row by label
print(df.loc[420])                # format : df.loc[label]
# i.e.: this will print the row under "420" label
# note this consider the label not the index
print()

# Reset the index
df.reset_index(inplace=True)
print(df)
print()

# select row by integer location
print(df.iloc[1])               # format : df.iloc[index]
print()

# slice rows
print(df[1:3])
print()

# select rows by boolean vector
x = df["Calories"] > 385          # format : df[boolean_vector]
print(df[x])




