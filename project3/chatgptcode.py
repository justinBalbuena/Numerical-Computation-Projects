import math


def newtons_method(f, df, x0, delta, stop_criterion='a'):
    """
    Solves a nonlinear equation using Newton's method.

    Arguments:
    f -- the function f(x)
    df -- the derivative function f'(x)
    x0 -- initial approximation
    delta -- tolerance value for stopping criterion
    stop_criterion -- flag for stopping condition ('a', 'b', 'c', or 'd')
                      a: absolute approximate error
                      b: relative approximate error
                      c: estimated true error
                      d: conjunction of both absolute and true error

    Returns:
    x -- the root approximation
    iterations -- the number of iterations performed
    """

    max_iter = 1000  # Set a limit to avoid infinite loops
    x = x0
    iterations = 0

    def true_error(estimated_value):
        # Implement the function to calculate the true error if known, otherwise use an estimation method
        # For this example, we assume some form of true solution is known or an estimation method.
        # Replace or modify this part as necessary.
        true_value = 0  # Placeholder, adjust accordingly
        return abs(true_value - estimated_value)

    for i in range(max_iter):
        # Compute the next approximation
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("The derivative is zero. Newton's method fails.")

        # Newton's update
        x_new = x - fx / dfx
        iterations += 1

        # Absolute Approximate Error
        abs_approx_error = abs(x_new - x)

        # Relative Approximate Error
        rel_approx_error = abs_approx_error / abs(x_new) if x_new != 0 else float('inf')

        # Estimated True Error
        est_true_error = true_error(x_new)

        # Check stopping criteria based on the provided flag
        if stop_criterion == 'a':  # Absolute Approximate Error
            if abs_approx_error < delta:
                break
        elif stop_criterion == 'b':  # Relative Approximate Error
            if rel_approx_error < delta:
                break
        elif stop_criterion == 'c':  # Estimated True Error
            if est_true_error < delta:
                break
        elif stop_criterion == 'd':  # Both Absolute Approximate and True Error
            if abs_approx_error < delta and est_true_error < delta:
                break
        else:
            raise ValueError("Invalid stop_criterion option. Choose 'a', 'b', 'c', or 'd'.")

        # Update the current approximation
        x = x_new

    return x_new, iterations


def f(x):
    return 2*math.sin(x) - (pow(math.e, x) / 4) - 1


def df(x):
    return 2 * math.cos(x) - (pow(math.e, x) / 4)

x0 = -6  # Initial guess
delta = 0.0001  # Tolerance

# Find the root using Newton's method
root, iters = newtons_method(f, df, x0, delta, stop_criterion='a')
print(f"Root: {root}, Iterations: {iters}")
root, iters = newtons_method(f, df, x0, delta, stop_criterion='b')
print(f"Root: {root}, Iterations: {iters}")
root, iters = newtons_method(f, df, x0, delta, stop_criterion='c')
print(f"Root: {root}, Iterations: {iters}")
root, iters = newtons_method(f, df, x0, delta, stop_criterion='d')
print(f"Root: {root}, Iterations: {iters}")
