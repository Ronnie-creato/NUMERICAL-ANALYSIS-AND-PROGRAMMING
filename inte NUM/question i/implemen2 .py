import numpy as np
def newton_coefficients(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y

    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])

    return coef[0, :]

def newton_poly(coef, x_data, x):
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

# Example usage
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
coef = newton_coefficients(x, y)

# Testing the Newton polynomial at a few points
for xi in x:
    print(f"N({xi}) = {newton_poly(coef, x, xi)}")
