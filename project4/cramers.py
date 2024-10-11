from sympy import *


def cramer(aug_matrix):
    square_size = aug_matrix.shape[1] - 1

    # list of solutions that will be received through cramers rule
    solution_list = []
    temp_matrix = None
    constant_col = []

    # this will extract the base matrix
    non_augmented = aug_matrix.copy()
    non_augmented.col_del(square_size)

    if non_augmented.det() == 0:
        return "This matrix has a determinant of 0"

    constant_col = aug_matrix.col(square_size)

    for i in range(0, square_size):
        # makes the temp_matrix equal to a copy of the original matrix for use in cramer's rule
        temp_matrix = non_augmented.copy()

        # exchanges column i of the matrix with the constants
        temp_matrix.col_del(i)
        temp_matrix = temp_matrix.col_insert(i, constant_col)

        # appends the solutions to an already created list
        solution_list.append(temp_matrix.det() / non_augmented.det())

    return solution_list


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
    print(cramer(matrix))

    continue_or = input("\nContinue or stop? (Y/N): ")
    match continue_or:
        case "Y":
            pass
        case "N":
            break
