import numpy as np
import matplotlib.pyplot as plt

# Define the data points
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([5.5, 43.1, 128, 290.7, 498.4, 978.67])

# Fit a 4th degree polynomial to the data
p = np.polyfit(x, y, 4)

# Generate x values for the fitted polynomial curve
x2 = np.arange(1, 6.1, 0.1)

# Evaluate the polynomial at each x2 value
y2 = np.polyval(p, x2)

# Plot the original data points and the fitted polynomial curve
plt.plot(x, y, 'o', label='Data points')
plt.plot(x2, y2, label='Fitted polynomial')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
