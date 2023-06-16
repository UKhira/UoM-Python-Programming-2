import pandas as p
import numpy as n

# create
a_dict = {"1st":1, "2nd":3, "3rd":5, "4th":7, "5th":9}
ser = p.Series(a_dict)
print(ser)

print()
# range access
print(ser[0:3])

print()

# Access: index number
print(ser[1])

print()

# Access: index label
print(ser["2nd"])