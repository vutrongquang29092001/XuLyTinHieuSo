# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# Bài 2
# setting the x - coordinates
x = np.linspace(0, 2*np.pi,256);
# setting the corresponding y - coordinates
y = 1/ (1 -0.87 * np.exp(-1j * x));

# plotting the points
plt.subplot(2,1,1);
plt.plot(x, abs(y))

# function to show the plot


y2 = 1 -  np.exp(-1j * x);

plt.subplot(2,1,2);
plt.plot(x, abs(y2))
plt.show()



