import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Original array = ", arr)
a = [True, False, True, False, True]
b = arr[a]
print("Filtered array = ", b)
# This will filter arr using a; if index[x] in a is True, then index[x] in arr will added to b
# if index[x] in a is False; then index[x] in arr will not be added to b