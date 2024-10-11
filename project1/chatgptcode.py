import math


def bisection_method(f, x1, x2, delta, flag, true_root=None):
    """
    f: the function to solve, passed as a lambda function
    x1, x2: the brackets [x1, x2] containing the root
    delta: the tolerance value for stopping (10^-6 in this case)
    flag: stopping criterion (1: absolute approx error, 2: relative approx error,
          3: true error, 4: both approx and true errors)
    true_root: optional, for true error estimation when flag is 3 or 4

    Returns:
    root: the estimated root
    iterations: number of iterations
    """
    iterations = 0
    root = (x1 + x2) / 2.0
    abs_approx_error = float('inf')
    true_error = float('inf')

    while True:
        iterations += 1
        prev_root = root
        root = (x1 + x2) / 2.0
        abs_approx_error = abs(root - prev_root)

        if true_root is not None:
            true_error = abs(true_root - root)

        # Check stopping criteria
        if flag == 1:  # Absolute approximate error
            if abs_approx_error < delta:
                break
        elif flag == 2:  # Relative approximate error
            rel_approx_error = abs_approx_error / abs(root)
            if rel_approx_error < delta:
                break
        elif flag == 3:  # True error
            if true_error < delta:
                break
        elif flag == 4:  # Both absolute approx error and true error
            if abs_approx_error < delta and true_error < delta:
                break

        # Update brackets
        if f(root) * f(x1) < 0:
            x2 = root
        else:
            x1 = root

    return root, iterations


# Define the equation: 2 * sin(x) - (e^x) / 4 - 1
f = lambda x: 2 * math.sin(x) - (math.exp(x) / 4) - 1

# Tolerance threshold
delta = 10 ** -6

# Find both roots using the four stopping criteria
intervals = [(-5, -3), (-7, -5)]
roots = []

for interval in intervals:
    print(f"Finding root in interval {interval}:")
    for flag in range(1, 5):
        root, iterations = bisection_method(f, interval[0], interval[1], delta, flag)
        roots.append(root)
        print(f"Flag {flag} - Root: {root}, Iterations: {iterations}")

# Estimating which root is closer to 0 for the given equation
f_close = lambda x: abs(2 * math.sin(x) - (math.exp(x) / 4) - 1)

print("\nComparing roots:")
for i, root in enumerate(roots):
    closeness = f_close(root)
    print(f"Root {i + 1}: {root}, Closeness to 0: {closeness}")