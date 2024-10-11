import math


def false_position_method(func, a, b, tol=1e-7, max_iter=10000, stop_criteria='absolute_approx'):
    """
    False Position method to find the root of a function with various stopping criteria.

    Parameters:
    func: Function for which we want to find the root.
    a: Lower bound of the interval.
    b: Upper bound of the interval.
    tol: Tolerance for convergence.
    max_iter: Maximum number of iterations.
    stop_criteria: Criteria to stop the method ('absolute_approx', 'relative_approx',
                    'true_absolute_error', 'combined').

    Returns:
    A root of the function, or None if it did not converge.
    """
    if func(a) * func(b) >= 0:
        print("The function must have different signs at the endpoints a and b.")
        return None

    for i in range(max_iter):
        # Calculate the point using the false position formula
        c = b - (func(b) * (a - b)) / (func(a) - func(b))

        # Calculate errors based on chosen stopping criteria
        absolute_error = abs(c - b)

        if i > 0:
            relative_error = abs((c - b) / b) if b != 0 else float('inf')
            true_absolute_error = abs(func(c))

        # Check stopping criteria
        if stop_criteria == 'absolute_approx':
            if absolute_error < tol:
                return c, i
        elif stop_criteria == 'relative_approx':
            if relative_error < tol:
                return c, i
        elif stop_criteria == 'true_absolute_error':
            if true_absolute_error < tol:
                return c, i
        elif stop_criteria == 'combined':
            if absolute_error < tol and true_absolute_error < tol:
                return c, i

        # Update the interval based on the function value at the new point
        if func(c) * func(a) < 0:
            b = c  # Root is in [a, c]
        else:
            a = c  # Root is in [c, b]

    print("Max iterations reached without convergence.")
    return None


# Define the function for which we want to find the root
def f(x):
    return float(2 * math.sin(x) - (pow(math.e, x) / 4.0) - 1.0)


# Example usage
root_absapprox = false_position_method(f, -5, -3, tol=0.000001, stop_criteria='absolute_approx')
root_combined = false_position_method(f, -5, -3, tol=0.000001, stop_criteria='combined')
print("Root found:", root_absapprox)
print("Root found:", root_combined)


root_relative = false_position_method(f, -5, -3, tol=0.000001, stop_criteria='relative_approx')
root_true = false_position_method(f, -5, -3, tol=0.000001, stop_criteria='true_absolute_error')
print("Root found:", root_relative)
print("Root found:", root_true)