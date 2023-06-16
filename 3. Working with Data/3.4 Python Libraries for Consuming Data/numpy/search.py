import numpy as np
arr = np.array([1, 1, 2, 3, 4, 1])
print("Original array - ", arr)
a = np.where(arr == 1)
print("Indexes of eleemnt '1' - ", a)