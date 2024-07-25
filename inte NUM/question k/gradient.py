import numpy as np

def gradient_descent(learning_rate=0.1, initial_guess=(0, 0), num_iterations=1000):
    x, y = initial_guess

    # Define the function
    def f(x, y):
        return x**2 + y**2 - xy + x - y + 1

    # Define the gradient of the function
    def grad_f(x, y):
        df_dx = 2*x - y + 1
        df_dy = 2*y - x - 1
        return np.array([df_dx, df_dy])

    # Perform Gradient Descent
    for i in range(num_iterations):
        gradient = grad_f(x, y)
        x -= learning_rate * gradient[0]
        y -= learning_rate * gradient[1]

        # Optionally print the progress
        if i % 100 == 0:
            print(f"Iteration {i}: x = {x}, y = {y}, f(x, y) = {f(x, y)}")

    return x, y, f(x, y)

# Example usage
optimal_x, optimal_y, optimal_value = gradient_descent(learning_rate=0.1, initial_guess=(0, 0), num_iterations=1000)
print(f"Optimal x: {optimal_x}, Optimal y: {optimal_y}, Optimal value: {optimal_value}")
