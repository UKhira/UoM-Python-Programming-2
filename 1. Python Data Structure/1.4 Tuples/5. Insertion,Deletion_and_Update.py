import sys                                  #to use "sys" module

my_tuple = (10, 20, 40)

# Though tuples and lists seems to be similar, Tuple cannot be assigned items as list
# Cuz, tuples are Immutable
try:
    my_tuple[0] = 50                        # will raise an error
    print(my_tuple)
except Exception as a:
    print(a)


# So does Delete and Update, neither of these methods are possible with tuple


# tuple will consume less memory than lists

my_list = [10, 20, 40]

print(sys.getsizeof(my_list))               #getsizeof = Return the size of an object in bytes.
print(sys.getsizeof(my_tuple))