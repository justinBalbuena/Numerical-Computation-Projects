import numpy as np

# Given dataset
cord_dict = {
    1.0: 1.543,
    1.1: 1.669,
    1.3: 1.971,
    1.4: 2.151,
    1.5: 2.352,
    1.7: 2.828,
    1.8: 3.107
}

# Uniformly spaced x-values (8 subintervals mean 9 points)
x_values = np.linspace(1.0, 1.8, 9)  # 9 points, 8 subintervals
y_values = []

# Interpolating y-values for these x-values
sorted_x = sorted(cord_dict.keys())
for x in x_values:
    # Find the closest known x-values surrounding this x
    for i in range(len(sorted_x) - 1):
        x1, x2 = sorted_x[i], sorted_x[i + 1]
        if x1 <= x <= x2:
            # Perform linear interpolation for y
            y1, y2 = cord_dict[x1], cord_dict[x2]
            y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
            y_values.append(y)
            break

# Step size for the interval
h = x_values[1] - x_values[0]


# 1. Multiple Application Trapezoidal Rule
def trapezoidal_rule(h, y_values):
    """
    Approximates the integral using the multiple application Trapezoidal Rule.

    Parameters:
    h (float): The width of each subinterval.
    y_values (list of float): The interpolated function values at each point.

    Returns:
    float: The approximate value of the integral.
    """
    n = len(y_values) - 1  # Number of subintervals
    integral = (h / 2) * (y_values[0] + 2 * sum(y_values[1:n]) + y_values[n])
    return integral


# 2. Composite Simpson's Rule
def simpsons_rule(h, y_values, n):
    """
    Approximates the integral using the Composite Simpson's Rule.

    Parameters:
    h (float): The width of each subinterval.
    y_values (list of float): The interpolated function values at each point.
    n (int): The number of subintervals (should be even).

    Returns:
    float: The approximate value of the integral.
    """
    # Verify n is even
    if n % 2 != 0:
        raise ValueError("Composite Simpson's rule requires an even number of subintervals.")

    integral = y_values[0] + y_values[-1]  # Start with first and last terms

    # Add the terms with 4 and 2 coefficients
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * y_values[i]
        else:
            integral += 4 * y_values[i]

    integral *= h / 3
    return integral


# Applying the functions to the dataset
# Trapezoidal Rule
trapezoidal_result = trapezoidal_rule(h, y_values)
print("Trapezoidal Rule Result:", trapezoidal_result)

# Composite Simpson's Rule
n = len(y_values) - 1  # Number of subintervals
simpsons_result = simpsons_rule(h, y_values, n)
print("Composite Simpson's Rule Result:", simpsons_result)