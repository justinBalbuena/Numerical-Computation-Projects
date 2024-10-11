import math
import sympy as sp


def bisect(x1, x2, choice, math_function, delta):
    # this ensures that valid brackets are chosen
    if math_function(x1) * math_function(x2) >= 0:
        while (math_function(x1) * math_function(x2)) >= 0:
            print("Please select values for x1 and x2 such that their multiplied value is negative")
            x1 = float(input("New Value for x1: "))
            x2 = float(input("New Value for x2: "))

    # setting up variables for use
    iteration = 0
    x3 = 0.0
    x4 = 0.0
    epsilon = 100.0

    # this begins the iterative process
    while True:
        iteration = iteration + 1
        x3 = (x1 + x2) / 2
        if math_function(x3) == 0:
            root = x3
            return root, iteration
        else:
            # narrows the interval
            if math_function(x1) * math_function(x3) < 0:
                x2 = x3
                x4 = x1
            else:
                x1 = x3
                x4 = x2

            match choice:
                # compares using the absolute approximate error
                case 'absolute_approximate':
                    epsilon = math.fabs(x1 - x2)
                    if epsilon < delta:
                        return x3, iteration
                # compares using the absolute relative approximate error
                case 'absolute_relative':
                    epsilon = math.fabs(x3 - x4) / math.fabs(x3)
                    if epsilon < delta:
                        return x3, iteration
                # compares using the true absolute error
                case 'true_absolute_error':
                    epsilon = math.fabs(math_function(x3))
                    if epsilon < delta:
                        return x3, iteration
                # compares using a Conjunction of an absolute approximate error and an estimated true absolute error
                case 'conjunction':
                    if math.fabs(x1 - x2) < delta and math.fabs(math_function(x3)) < delta:
                        return x3, iteration


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
            print(bisect(left_bound, right_bound, stopping_criteria, x, delta))
            print("\n")
        case 'absolute_relative':
            print("Value, Iterations")
            print(bisect(left_bound, right_bound, stopping_criteria, x, delta))
            print("\n")
        case 'true_absolute_error':
            print("Value, Iterations")
            print(bisect(left_bound, right_bound, stopping_criteria, x, delta))
            print("\n")
        case 'conjunction':
            print("Value, Iterations")
            print(bisect(left_bound, right_bound, stopping_criteria, x, delta))
