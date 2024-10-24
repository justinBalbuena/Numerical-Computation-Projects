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


def gauss_seidel(A, tolerance, flag):
    """

    :param A:
    :param tolerance:
    :param flag:
    :return:
    """

    diag_matrix = A.copy()
    if is_diagonally_dominant(A) == false:
        diag_matrix = diagonalization(A)

    # number of rows and columns in the matrix
    row_indices = diag_matrix.shape[0]
    column_indices = diag_matrix.shape[1]

    old_x_approximation = []

    for i in range(column_indices - 1):
        old_x_approximation.append(float(int(random() * 10)))

    new_x = old_x_approximation.copy()
    for i in range(row_indices):
        diag_matrix[i, column_indices - 1] = diag_matrix[i, column_indices - 1] / diag_matrix[i, i]
        for j in range(row_indices):
            if i != j:
                diag_matrix[i, j] = diag_matrix[i, j] / diag_matrix[i, i]

    error = 1
    while True:
        error = 0

        for i in range(column_indices - 1):
            # due to the way that error calculation is being calculated, specifically at the end
            # old_X_approximation is not being assigned values within the for loop
            old_x_approximation[i] = new_x[i]
            new_x[i] = diag_matrix[i, column_indices - 1]
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

    print(gauss_seidel(matrix, tolerance, stopping_criteria))

    continue_or = input("\nContinue or stop? (Y/N): ")
    match continue_or:
        case "Y":
            pass
        case "N":
            break
