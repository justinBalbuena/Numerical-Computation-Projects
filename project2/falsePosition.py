import math
import sympy as sp


def false_position(x0, x1, choice, user_function, delta):
    """

    :param x0: left bound value
    :param x1: right bound value
    :param choice: choice of stopping criteria given by user
    :param user_function: equation given by user
    :param delta: threshold value
    :return: x value of root, number of iterations
    """

    if user_function(x0) * user_function(x1) < 0:
        pass
    else:
        while user_function(x0) * user_function(x1) > 0:
            x0 = float(input("Choose a proper value for x0: "))
            x1 = float(input("Choose a proper value for x1: "))

    x = x1
    # setting up variables for use
    iteration = 0
    epsilon = 100.0

    # this begins the iterative process
    while True:
        iteration = iteration + 1
        x2 = x1 - user_function(x1) * ((x0 - x1) / (user_function(x0) - user_function(x1)))
        if user_function(x2) == 0:
            root = x2
            return root, iteration
        else:
            if user_function(x0) * user_function(x2) < 0:
                x1 = x2
            else:
                x0 = x2
            match choice:
                # compares using the absolute approximate error
                case 'absolute_approximate':
                    epsilon = math.fabs(x - x2)
                    if epsilon < delta:
                        return x2, iteration
                    else:
                        # updates x
                        x = x2
                # compares using the absolute relative approximate error
                case 'absolute_relative':
                    epsilon = math.fabs(x - x2) / math.fabs(x2)
                    if epsilon < delta:
                        return x2, iteration
                    else:
                        # updates x
                        x = x2
                # compares using the true absolute error
                case 'true_absolute_error':
                    epsilon = math.fabs(user_function(x2))
                    if epsilon < delta:
                        return x2, iteration
                # compares using a Conjunction of an absolute approximate error and an estimated true absolute error
                case 'conjunction':
                    if math.fabs(x - x2) < delta and math.fabs(user_function(x2)) < delta:
                        return x2, iteration
                    else:
                        # updates x
                        x = x2


while True:
    # Gets the equation from the user
    user_input = input("Enter a function of x in a python readable line (e.g., x**2 + 3): ")
    x = lambda x: eval(user_input)

    # Gets the bounds
    left_bound = float(input("Enter your left bound value: "))
    right_bound = float(input("Enter your right bound value: "))

    # Gets the stopping criteria
    stopping_criteria = input("Enter 'absolute_approximate', 'absolute_relative', 'true_absolute_error', 'conjunction' "
                              "for the stopping criteria that you want: ")
    delta = float(input("Enter your threshold value: "))
    match stopping_criteria:
        case 'absolute_approximate':
            print("Value, Iterations")
            print(false_position(left_bound, right_bound, stopping_criteria, x, delta))
            print("\n")
        case 'absolute_relative':
            print("Value, Iterations")
            print(false_position(left_bound, right_bound, stopping_criteria, x, delta))
            print("\n")
        case 'true_absolute_error':
            print("Value, Iterations")
            print(false_position(left_bound, right_bound, stopping_criteria, x, delta))
            print("\n")
        case 'conjunction':
            print("Value, Iterations")
            print(false_position(left_bound, right_bound, stopping_criteria, x, delta))
            print("\n")
        case _:
            print("Type in an appropriate stopping criteria\n")
