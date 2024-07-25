import numpy as np

def f(x):
    return np.sin(x)  # Example function

x = np.linspace(0, 10, 100)
dx = x[1] - x[0]  # Assuming uniform spacing
dy_dx = np.gradient(f(x), dx)

import matplotlib.pyplot as plt

plt.plot(x, f(x), label='f(x) = sin(x)')
plt.plot(x, dy_dx, label="f'(x)")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Differentiation')
plt.show()
