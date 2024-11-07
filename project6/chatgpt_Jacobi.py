import numpy as np


def jacobi_method(A, b, tolerance, stopping_criteria='MAE', random_start=True):
    """
    Solves the system of linear equations Ax = b using the Jacobi iterative method.

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

    # Diagonal and non-diagonal matrices
    D = np.diag(np.diag(A))
    L_U = A - D  # L and U combined (everything except the diagonal)

    error = tolerance + 1  # Initial error
    while error > tolerance:
        # Update x using the Jacobi formula
        x = np.linalg.inv(D) @ (b - L_U @ x_old)

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

# Solve using Jacobi with MAE
jacobi_solution = jacobi_method(A, b, tolerance=0.001, stopping_criteria='MAE', random_start=False)
print("Jacobi MAE Solution:", jacobi_solution)

# Solve using Jacobi with RMSE
jacobi_solution = jacobi_method(A, b, tolerance=0.001, stopping_criteria='RMSE', random_start=False)
print("Jacobi RMSE Solution:", jacobi_solution)