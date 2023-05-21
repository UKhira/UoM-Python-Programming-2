# Tuple packing is assigning values to tuple
tuple_1 = ('car', 'pen', 29)

# Tuple unpacking is extracting the content of tuple into variables
a, b, c = tuple_1                   # Elements in tuple will assign to variable a,b and c orderly
print(a)                            # In above step, Number of variable must be equal to number of elements in tuple
print(b)
print(c)

try:
    c,d = tuple_1
    print(c)
except Exception as e:
    print(e)