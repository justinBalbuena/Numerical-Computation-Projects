import math
import sympy as sp


def secant(x0, x1, choice, user_function, delta):
    """

    :param x0: left bound value
    :param x1: right bound value
    :param choice: choice of stopping criteria given by user
    :param user_function: equation given by user
    :return: x value of root, number of iterations
    """

    if math.fabs(user_function(x0)) < math.fabs(user_function(x1)):
        # swaps the values
        x0, x1 = x1, x0

    # setting up variables for use
    iteration = 0
    epsilon = 100.0

    # this begins the iterative process
    while True:
        iteration = iteration + 1
        x2 = x1 - user_function(x1) * ((x0 - x1) / (user_function(x0) - user_function(x1)))
        x0 = x1
        x1 = x2
        if user_function(x2) == 0:
            root = x2
            return root, iteration
        else:
            match choice:
                # compares using the absolute approximate error
                case 'absolute_approximate':
                    epsilon = math.fabs(x0 - x1)
                    if epsilon < delta:
                        return x1, iteration
                # compares using the absolute relative approximate error
                case 'absolute_relative':
                    epsilon = math.fabs(x0 - x1) / math.fabs(x1)
                    if epsilon < delta:
                        return x1, iteration
                # compares using the true absolute error
                case 'true_absolute_error':
                    epsilon = math.fabs(user_function(x1))
                    if epsilon < delta:
                        return x1, iteration
                # compares using a Conjunction of an absolute approximate error and an estimated true absolute error
                case 'conjunction':
                    if math.fabs(x0 - x1) < delta and math.fabs(user_function(x1)) < delta:
                        return x1, iteration


while True:
    # Gets the equation from the user
    user_input = input("Enter a function of x in a python readable line (e.g., x**2 + 3): ")
    x = lambda x: eval(user_input)

    # Gets the bounds
    left_bound = float(input("Enter your left bound value: "))
    right_bound = float(input("Enter your right bound value: "))

    # Gets the stopping criteria
    stopping_criteria = input("Enter 'absolute_approximate', 'absolute_relative', 'true_absolute_error', 'conjunction' "
                              "for the stopping criteria that you want ")
    delta = float(input("Enter your threshold value: "))
    match stopping_criteria:
        case 'absolute_approximate':
            print("Value, Iterations")
            print(secant(left_bound, right_bound, stopping_criteria, x, delta))
            print("\n")
        case 'absolute_relative':
            print("Value, Iterations")
            print(secant(left_bound, right_bound, stopping_criteria, x, delta))
            print("\n")
        case 'true_absolute_error':
            print("Value, Iterations")
            print(secant(left_bound, right_bound, stopping_criteria, x, delta))
            print("\n")
        case 'conjunction':
            print("Value, Iterations")
            print(secant(left_bound, right_bound, stopping_criteria, x, delta))
