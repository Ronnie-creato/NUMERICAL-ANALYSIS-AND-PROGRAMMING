# Define the points for interpolation
x0, y0 = 2.00, 7.2
x1, y1 = 4.25, 7.1
x = 4.00

# Calculate the interpolated value of y
y = y0 + ((x - x0) / (x1 - x0)) * (y1 - y0)

# Print the result
print(f'The value of y at x = {x} is {y:.2f}')
