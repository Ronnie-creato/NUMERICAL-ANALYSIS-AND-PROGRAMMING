import numpy as np

# Define the function to integrate
def f(x):
    return np.sin(x)  # Example function (sin(x))

# Implement the trapezoidal rule
def trapezoidal_rule(f, a, b, n):
    """
    Approximate the integral of f from a to b using the trapezoidal rule with n intervals.
    
    Parameters:
    f (function): Function to integrate.
    a (float): Lower limit of integration.
    b (float): Upper limit of integration.
    n (int): Number of intervals.
    
    Returns:
    float: Approximated integral of f from a to b.
    """
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    
    integral *= h
    return integral

# Example usage
a = 0  # Lower limit of integration
b = np.pi  # Upper limit of integration
n = 1000  # Number of intervals

result = trapezoidal_rule(f, a, b, n)
print(f"Approximate integral of sin(x) from {a} to {b} is {result:.6f}")
