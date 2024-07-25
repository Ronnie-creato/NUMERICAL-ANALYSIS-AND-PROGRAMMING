def f(x):
    return x**3 - 0.165*x**2 + 3.993e-4

def f_prime(x):
    return 3*x**2 - 0.33*x

def newtons_method(x0, iterations):
    results = []
    for i in range(iterations):
        fx = f(x0)
        fpx = f_prime(x0)
        x1 = x0 - fx / fpx
        error = abs((x1 - x0) / x1) * 100
        results.append((x0, x1, fx, fpx, error))
        x0 = x1
    return results

# Initial guess
initial_guess = 0.05

# Number of iterations
iterations = 3

# Perform Newton's method
results = newtons_method(initial_guess, iterations)

# Print the results
for i, (x0, x1, fx, fpx, error) in enumerate(results, start=1):
    print(f"Iteration {i}:")
    print(f"  x0 = {x0:.6f}")
    print(f"  f(x0) = {fx:.6e}")
    print(f"  f'(x0) = {fpx:.6e}")
    print(f"  x1 = {x1:.6f}")
    print(f"  Absolute Relative Approximate Error = {error:.6f}%")
    print()
    print("initial guess was 0.5 for my case")
    
