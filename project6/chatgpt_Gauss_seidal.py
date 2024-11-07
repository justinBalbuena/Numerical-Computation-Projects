import numpy as np


def gauss_seidel_method(A, b, tolerance, stopping_criteria='MAE', random_start=True):
    """
    Solves the system of linear equations Ax = b using the Gauss-Seidel iterative method.

    :param A: Coefficient matrix (n x n)
    :param b: Constant vector (n x 1)
    :param tolerance: Stopping tolerance for error
    :param stopping_criteria: 'MAE' or 'RMSE'
    :param random_start: Boolean to decide random start or [1,...,1]
    :return: Solution vector x
    """
    n = len(b)

    # Initial guess for x
    x = np.random.rand(n) if random_start else np.ones(n)
    x_old = x.copy()

    error = tolerance + 1  # Initial error
    while error > tolerance:
        for i in range(n):
            sum_Ax = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_Ax) / A[i, i]

        # Compute error based on stopping criteria
        if stopping_criteria == 'MAE':
            error = np.mean(np.abs(x - x_old))
        elif stopping_criteria == 'RMSE':
            error = np.sqrt(np.mean((x - x_old) ** 2))
        else:
            raise ValueError("Stopping criteria must be either 'MAE' or 'RMSE'")

        x_old = x.copy()

    return x


A = np.array([[1, -2, 4],
              [8, -3, 2],
              [-1, 10, 2]])

b = np.array([6, 2, 4])

# Solve using Gauss-Seidel with MAE
gauss_seidel_solution = gauss_seidel_method(A, b, tolerance=0.001, stopping_criteria='MAE', random_start=True)
print("Gauss-Seidel MAE Solution:", gauss_seidel_solution)

# Solve using Gauss-Seidel with RMSE
gauss_seidel_solution = gauss_seidel_method(A, b, tolerance=0.001, stopping_criteria='RMSE', random_start=True)
print("Gauss-Seidel RMSE Solution:", gauss_seidel_solution)