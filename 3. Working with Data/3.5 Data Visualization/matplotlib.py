import matplotlib.pyplot as plt
import numpy as np

# create two subplots
f, (ax1, ax2) = plt.subplots(1,2)

# plot 1
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
ax1.plot(x1,y1)

# plot 2
x2 = np.aray([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])
ax2.plot(x2,y2)

plt.show()