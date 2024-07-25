from scipy.stats import linregress

# Example data
x = np.linspace(0, 10, 100)
y = 2.5 * x + np.random.normal(size=x.size)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Plotting the data and the regression line
plt.scatter(x, y, label='Data')
plt.plot(x, slope * x + intercept, color='red', label='Fitted line')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.show()

print(f'Slope: {slope}, Intercept: {intercept}')
