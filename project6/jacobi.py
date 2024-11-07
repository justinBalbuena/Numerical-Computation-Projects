from sympy import *
from random import *


def is_diagonally_dominant(A):
    """

    :param A: augmented matrix
    :return: True if the matrix is diagonally dominant, False otherwise.
    """
    n = A.shape[0]
    for i in range(n):
        # Sum of the absolute values of the non-diagonal elements in row i
        row_sum = sum(abs(A[i, j]) for j in range(n) if j != i)

        # Check if the diagonal element is greater than or equal to the row sum
        if abs(A[i, i]) < row_sum:
            return False  # Not diagonally dominant
    return True  # Diagonally dominant


def diagonalization(A):
    row_indices = A.shape[0]

    for i in range(row_indices - 1):
        pivot = i

        # compares the numbers in column to select pivot and saves in p
        for j in range(i + 1, row_indices):
            if abs(A[j, i]) > abs(A[i, i]):
                pivot = j

        # swaps rows i and pivot if new pivot was found (if pivot changed at all)
        if pivot != i:
            A.row_swap(i, pivot)

        # if the pivot is zero there is no unique solution
        if A[i, i] == 0:
            print("No unique solution")
            return None

    return A


def jacobi_method(A, tolerance, flag):
    """
    Jacobi method for solving systems of linear equations.

    :param A: Augmented matrix (matrix + vector of constants)
    :param tolerance: Stopping criteria based on the error threshold
    :param flag: Specifies whether to use 'MAE' or 'RMSE' for stopping criteria
    :return: Approximated solution vector once the error is below tolerance
    """

    # Make a copy of the input matrix to work on
    diag_matrix = A.copy()

    # Check if the matrix is diagonally dominant, and diagonalize it if necessary
    if is_diagonally_dominant(A) == False:
        diag_matrix = diagonalization(A)

    # Get the number of rows and columns in the matrix
    row_indices = diag_matrix.shape[0]
    column_indices = diag_matrix.shape[1]

    # Initialize a list to store the old approximation values for unknowns
    old_x_approximation = []

    # Initialize the approximation with random values for all unknowns
    for i in range(column_indices - 1):
        old_x_approximation.append(float(int(random() * 10)))

    # Copy the initial approximation to create a new approximation vector
    new_x = old_x_approximation.copy()

    # Normalize the matrix to prepare for iteration (divide each row by the diagonal element)
    for i in range(row_indices):
        diag_matrix[i, column_indices - 1] = diag_matrix[i, column_indices - 1] / diag_matrix[i, i]
        for j in range(row_indices):
            if i != j:
                diag_matrix[i, j] = diag_matrix[i, j] / diag_matrix[i, i]

    # Iterative process until the stopping condition is met
    while True:
        # Reset error to 0 at the start of each iteration
        error = 0

        # Store the current approximation as the old approximation
        for i in range(row_indices):
            old_x_approximation[i] = new_x[i]

            # Update the new approximation starting with the constant value (b_i)
            new_x[i] = diag_matrix[i, column_indices - 1]

        # Iterate through the matrix rows and update the approximations using the Jacobi method formula
        for i in range(row_indices):
            for j in range(row_indices):
                if i != j:
                    # Adjust the approximation using the previous iteration's values of other unknowns
                    new_x[i] = new_x[i] - diag_matrix[i, j] * old_x_approximation[j]

        # Error evaluation based on the stopping criteria flag ('MAE' or 'RMSE')
        match flag:
            case 'MAE':
                for i in range(len(new_x)):
                    error += abs(new_x[i] - old_x_approximation[i])
                error /= row_indices
                print(error)
                if error < tolerance:
                    return new_x
            case 'RMSE':
                for i in range(len(new_x)):
                    error += pow((new_x[i] - old_x_approximation[i]), 2)
                error = sqrt((error / row_indices))
                print(error)
                if error < tolerance:
                    return new_x
            case _:
                return None


while True:
    user_augmatrix = []
    user_row = []

    constants = []

    # since it is an n x n matrix only need to get n
    matrix_size = int(input("What size square matrix do you want to input (i.e, 2, 4, 5): "))
    for x in range(0, matrix_size):
        for j in range(0, matrix_size):
            user_row.append(float(input(f"Put in a number for row {x}: ")))
        user_augmatrix.append(user_row.copy())
        user_row.clear()

    print("Top down, put in the constants for your matrix: ")
    for x in range(0, matrix_size):
        constants.append(float(input(f"Constant {x}: ")))

    # This will create the full augmented matrix
    matrix = Matrix(user_augmatrix)
    constants_col = Matrix(constants)

    matrix = matrix.col_insert(matrix_size, constants_col)

    # gets the tolerance value
    tolerance = float(input("Please enter your tolerance value: "))

    # gets the stopping criteria
    stopping_criteria = input("Please enter MAE, RMSE for your stopping criteria: ")

    print(jacobi_method(matrix, tolerance, stopping_criteria))

    continue_or = input("\nContinue or stop? (Y/N): ")
    match continue_or:
        case "Y":
            pass
        case "N":
            break
