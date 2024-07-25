from scipy.optimize import curve_fit

# Example data
x_data = np.linspace(0, 4, 50)
y_data = 2.5 * np.sin(1.5 * x_data) + np.random.normal(size=x_data.size)

# Define the model function
def model(x, a, b):
    return a * np.sin(b * x)

# Fit the curve
params, params_covariance = curve_fit(model, x_data, y_data, p0=[2, 2])

# Plotting the data and the fit
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model(x_data, *params), label='Fitted curve', color='red')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fitting')
plt.show()

print(f'Fitted parameters: {params}')
