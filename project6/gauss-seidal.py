from sympy import *
from random import *


def is_diagonally_dominant(A):
    """
    Checks if the matrix A is diagonally dominant.
    A matrix is diagonally dominant if for every row, the magnitude of the diagonal element
    is greater than or equal to the sum of the magnitudes of all other elements in that row.

    :param A: augmented matrix
    :return: True if the matrix is diagonally dominant, False otherwise.
    """
    n = A.shape[0]  # Get the number of rows in matrix A
    for i in range(n):
        # Sum of the absolute values of the non-diagonal elements in row i
        row_sum = sum(abs(A[i, j]) for j in range(n) if j != i)

        # Check if the diagonal element is greater than or equal to the row sum
        if abs(A[i, i]) < row_sum:
            return False  # Not diagonally dominant
    return True  # Diagonally dominant


def diagonalization(A):
    """
    Attempts to diagonalize the matrix A by swapping rows to make it diagonally dominant.
    This is necessary for the convergence of iterative methods like Gauss-Seidel.

    :param A: augmented matrix
    :return: Diagonalized matrix if possible, None if a unique solution does not exist.
    """
    row_indices = A.shape[0]  # Get the number of rows in matrix A

    # Iterate through each row to ensure diagonal dominance
    for i in range(row_indices - 1):
        pivot = i

        # Compares values in column to find a larger pivot (for diagonal dominance)
        for j in range(i + 1, row_indices):
            if abs(A[j, i]) > abs(A[i, i]):
                pivot = j

        # Swap rows i and pivot if a better pivot was found
        if pivot != i:
            A.row_swap(i, pivot)

        # If the pivot is zero, no unique solution exists
        if A[i, i] == 0:
            print("No unique solution")
            return None

    return A


def gauss_seidel(A, tolerance, flag):
    """
    Performs the Gauss-Seidel iterative method to solve a system of linear equations.
    Stops when the error (based on either MAE or RMSE) is below the specified tolerance.

    :param A: augmented matrix (including constants)
    :param tolerance: error threshold to stop the iterations
    :param flag: error criterion ('MAE' or 'RMSE')
    :return: Solution vector (approximation of the unknowns)
    """

    # Make a copy of the matrix A to avoid modifying the original
    diag_matrix = A.copy()

    # Check for diagonal dominance and diagonalize if necessary
    if is_diagonally_dominant(A) == False:
        diag_matrix = diagonalization(A)

    # Get the number of rows and columns in the matrix
    row_indices = diag_matrix.shape[0]
    column_indices = diag_matrix.shape[1]

    # Initialize the old approximation of the solution with random values
    old_x_approximation = []
    for i in range(column_indices - 1):
        old_x_approximation.append(float(int(random() * 10)))

    # Copy old approximation to initialize the new approximation vector
    new_x = old_x_approximation.copy()

    # Normalize the matrix (dividing each element by its diagonal value)
    for i in range(row_indices):
        diag_matrix[i, column_indices - 1] = diag_matrix[i, column_indices - 1] / diag_matrix[i, i]
        for j in range(row_indices):
            if i != j:
                diag_matrix[i, j] = diag_matrix[i, j] / diag_matrix[i, i]

    error = 1  # Initial error set to a high value
    while True:
        error = 0  # Reset error for each iteration

        # Perform Gauss-Seidel update for each unknown
        for i in range(column_indices - 1):
            # Old approximation is assigned after the new values are updated
            old_x_approximation[i] = new_x[i]

            # Update the current approximation using the known value (b_i)
            new_x[i] = diag_matrix[i, column_indices - 1]

            # Iterate through all other elements in the row and adjust the new approximation
            for j in range(column_indices - 1):
                if i != j:
                    new_x[i] = new_x[i] - diag_matrix[i, j] * new_x[j]

        match flag:
            case 'MAE':
                for i in range(len(new_x)):
                    error += abs(new_x[i] - old_x_approximation[i])
                error /= row_indices
                if error < tolerance:
                    return new_x
            case 'RMSE':
                for i in range(len(new_x)):
                    error += pow((new_x[i] - old_x_approximation[i]), 2)
                error = sqrt((error / row_indices))
                if error < tolerance:
                    return new_x


while True:
    user_augmatrix = []  # List to store user input for the augmented matrix
    user_row = []  # Temporary storage for each row of the matrix

    constants = []  # List to store the constants (b values)

    # Ask the user for the size of the square matrix (n x n)
    matrix_size = int(input("What size square matrix do you want to input (i.e, 2, 4, 5): "))

    # Collect matrix elements row by row from user input
    for x in range(0, matrix_size):
        for j in range(0, matrix_size):
            user_row.append(float(input(f"Put in a number for row {x}: ")))
        user_augmatrix.append(user_row.copy())
        user_row.clear()  # Clear temporary row after adding it to the matrix

    # Collect constants (b values) from user input
    print("Top down, put in the constants for your matrix: ")
    for x in range(0, matrix_size):
        constants.append(float(input(f"Constant {x}: ")))

    # Create the full augmented matrix
    matrix = Matrix(user_augmatrix)
    constants_col = Matrix(constants)
    matrix = matrix.col_insert(matrix_size, constants_col)

    tolerance = float(input("Please enter your tolerance value: "))

    stopping_criteria = input("Please enter MAE, RMSE for your stopping criteria: ")

    print(gauss_seidel(matrix, tolerance, stopping_criteria))

    continue_or = input("\nContinue or stop? (Y/N): ")
    match continue_or:
        case "Y":
            pass
        case "N":
            break