def lagrange_interpolation(x_values, y_values, x):
    """
    Perform Lagrange interpolation for a given x.

    Parameters:
    - x_values: list of x coordinates of known points
    - y_values: list of y coordinates of known points
    - x: the x coordinate to interpolate the corresponding y

    Returns:
    - The interpolated y value at x.
    """
    # Ensure that x_values and y_values have the same length
    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have the same number of elements")

    n = len(x_values)
    result = 0

    for i in range(n):
        # Compute the basis polynomial L_i(x)
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_values[j]) / (x_values[i] - x_values[j])

        # Add the current term to the result
        result += y_values[i] * L_i

    return result


# Example usage
x_points = [0.3, 0.5, 0.7, 0.9, 1.1]
y_points = [0.404958, 0.824361,  1.40963, 2.21364, 3.30458]
x_interpolate = 0.6

y_interpolated = lagrange_interpolation(x_points, y_points, x_interpolate)
print(f"Interpolated y at x = {x_interpolate} is {y_interpolated}")
