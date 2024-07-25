import numpy as np

def lagrange_coefficients(x, y):
    def L(k, x_val):
        term = [(x_val - x[i])/(x[k] - x[i]) for i in range(len(x)) if i != k]
        return np.prod(term)
    
    def lagrange_poly(x_val):
        return sum(y[k] * L(k, x_val) for k in range(len(x)))

    return lagrange_poly

# Example usage
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
lagrange_poly = lagrange_coefficients(x, y)

# Testing the Lagrange polynomial at a few points
for xi in x:
    print(f"L({xi}) = {lagrange_poly(xi)}")
