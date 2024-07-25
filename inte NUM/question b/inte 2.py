from scipy.integrate import quad, simps

def f(x):
    return np.sin(x)  # Example function

# Integration limits
a = 0
b = np.pi

# Using quad (adaptive quadrature)
result_quad, _ = quad(f, a, b)
print(f'Integration using quad: {result_quad}')

# Using Simpson's rule
x = np.linspace(a, b, 100)
y = f(x)
result_simps = simps(y, x)
print(f'Integration using simps: {result_simps}')
