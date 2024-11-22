from sympy import *


def gauss_with_pivot(A):
    """

    :param A: the augmented matrix
    :return: the list of solutions
    """

    # number of rows in the matrix
    row_indices = A.shape[0]

    # forward elimination
    for i in range(row_indices - 1):
        pivot = i

        # compares the numbers in column to select pivot and saves in p
        for j in range(i+1, row_indices):
            if abs(A[j, i]) > abs(A[i, i]):
                pivot = j

        # swaps rows i and pivot if new pivot was found (if pivot changed at all)
        if pivot != i:
            A.row_swap(i, pivot)

        # if the pivot is zero there is no unique solution
        if A[i, i] == 0:
            print("No unique solution")
            return None

        # eliminates the elements below the pivot
        for j in range(i + 1, row_indices):
            multiplier = A[j, i] / A[i, i]
            for k in range(i + 1, row_indices + 1):
                A[j, k] = A[j, k] - (multiplier * A[i, k])

    # checks to see if there is a unique solution at the last pivot
    if A[row_indices - 1, row_indices - 1] == 0:
        print("There is no unique solution for this matrix")
        return None

    x = [0, 0, 0]

    # performs back substitution
    x[row_indices - 1] = A[row_indices - 1, row_indices] / A[row_indices - 1, row_indices - 1]
    for i in range(row_indices - 2, -1, -1):
        accumulation = 0
        for j in range(i + 1, row_indices):
            accumulation += A[i, j] * x[j]
        x[i] = ((A[i, row_indices] - accumulation) / A[i, i])

    return x

if __name__ == "__main__":
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
        print(gauss_with_pivot(matrix))

        continue_or = input("\nContinue or stop? (Y/N): ")
        match continue_or:
            case "Y":
                pass
            case "N":
                break
