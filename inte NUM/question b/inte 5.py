from scipy.interpolate import splrep, splev

# Example data
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Compute the spline representation
spl = splrep(x, y)

# Generate dense x values for a smooth spline
x_dense = np.linspace(0, 10, 200)
y_spline = splev(x_dense, spl)

# Plotting the data and the spline interpolation
plt.scatter(x, y, label='Data')
plt.plot(x_dense, y_spline, label='Spline interpolation', color='red')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spline Interpolation')
plt.show()
