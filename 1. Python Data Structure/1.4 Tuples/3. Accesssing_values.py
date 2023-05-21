my_tuple = (10, 20, 30, 40, 50, 60)
print(my_tuple[0])
print(my_tuple[4])

# Negative indexing
print(my_tuple[-1])
print(my_tuple[-3])

# Slicing
print(my_tuple[0:3])
print(my_tuple[:3])

print(my_tuple[2:])
print(my_tuple[:-1])


# Nested tuples
new_tuple = (('a','b','c'),(1,2,3))
print(new_tuple[1])
print(new_tuple[0][1])
print(new_tuple[1][2])
print(new_tuple[0][1:3])