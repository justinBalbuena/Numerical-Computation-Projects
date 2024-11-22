import sympy as sp
import math

# Define the function and symbols
x = sp.symbols('x')
f = x ** 3 - 4 * x

# First and second derivatives for Newton's method
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)

# Convert expressions to callable functions
f_func = sp.lambdify(x, f)
f_prime_func = sp.lambdify(x, f_prime)
f_double_prime_func = sp.lambdify(x, f_double_prime)


def GoldenSection(a, b, tol=1e-6, find_min=True):
    """ Golden Section Method for finding a minimum or maximum of a function. """
    # Golden ratio constant
    golden_ratio = (math.sqrt(5) - 1) / 2

    # Set up initial points
    c = b - golden_ratio * (b - a)
    d = a + golden_ratio * (b - a)

    while abs(b - a) > tol:
        # Evaluate function at c and d
        f_c = f_func(c)
        f_d = f_func(d)

        if find_min:
            # Minimize: choose the interval that gives a smaller function value
            if f_c < f_d:
                b = d
            else:
                a = c
        else:
            # Maximize: choose the interval that gives a larger function value
            if f_c > f_d:
                b = d
            else:
                a = c

        # Update points
        c = b - golden_ratio * (b - a)
        d = a + golden_ratio * (b - a)

    # Return the midpoint of the final interval
    return (b + a) / 2


def NewtonMinMax(x0, tol=1e-6):
    """ Newton's Method to find an extremum (min or max) of a function. """
    x_current = x0

    while True:
        # Calculate the next point using Newton's method formula
        f_prime_val = f_prime_func(x_current)
        f_double_prime_val = f_double_prime_func(x_current)

        # Avoid division by zero
        if f_double_prime_val == 0:
            raise ValueError("Second derivative is zero; Newton's method fails.")

        x_next = x_current - f_prime_val / f_double_prime_val

        # Check for convergence
        if abs(x_next - x_current) < tol:
            break

        x_current = x_next

    return x_current


# Test the methods on f(x) = x^3 - 4x
a, b = -3, 3
tolerance = 1e-6

# Using Golden Section to find minimum and maximum
min_x = GoldenSection(a, b, tol=tolerance, find_min=True)
max_x = GoldenSection(a, b, tol=tolerance, find_min=False)

# Using Newton's Method starting from an initial guess
initial_guess = -1.75
extremum_x = NewtonMinMax(initial_guess, tol=tolerance)
extremum_x_2 = NewtonMinMax(1.75, tol=tolerance)

# Display the results
print("Golden Section Method:")
print(f"Minimum found at x = {min_x}, f(x) = {f_func(min_x)}")
print(f"Maximum found at x = {max_x}, f(x) = {f_func(max_x)}")

print("\nNewton's Method:")
print(f"Extremum found at x = {extremum_x}, f(x) = {f_func(extremum_x)}")
print(f"Extremum found at x = {extremum_x_2}, f(x) = {f_func(extremum_x_2)}")