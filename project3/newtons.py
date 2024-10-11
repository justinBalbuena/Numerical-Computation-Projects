import math
from sympy import *


def newtons(x0, choice, user_function, delta):
    """

    :param x0: starting position
    :param choice: stopping criteria
    :param user_function: the mathematical function given by the user
    :param delta: tolerance threshold given by the user
    :return:
    """

    # sets up a function using lambda to set up the user's given function for usability
    user_expression = lambda x: eval(user_function)

    # sets up a function using lambda and sympy to set up the derivative of the user's function
    x = symbols('x')
    derived_function = Derivative(user_function, x)
    derivative = lambda x: eval(format(derived_function.doit()))

    # setting up iteration and epsilon variables for use
    iteration = 0
    epsilon = 100.0

    # this begins the iterative process
    while True:
        if user_expression(x0) == 0:
            return x0

        iteration = iteration + 1

        # if the value of the derivative at the position given by the user is 0, it gets a new x0
        if derivative(x0) == 0:
            while derivative(x0) == 0:
                x0 = float(input("Enter a new x0"))

        x1 = x0 - (user_expression(x0) / derivative(x0))

        match choice:
            # compares using the absolute approximate error
            case 'absolute_approximate':
                epsilon = math.fabs(x1 - x0)
                if epsilon < delta:
                    return x1, iteration
            # compares using the absolute relative approximate error
            case 'absolute_relative':
                epsilon = math.fabs(x1 - x0) / math.fabs(x1)
                if epsilon < delta:
                    return x1, iteration
            # compares using the true absolute error
            case 'true_absolute_error':
                epsilon = math.fabs(user_expression(x1))
                if epsilon < delta:
                    return x1, iteration
            # compares using a Conjunction of an absolute approximate error and an estimated true absolute error
            case 'conjunction':
                if math.fabs(x1 - x0) < delta and math.fabs(user_expression(x1)) < delta:
                    return x1, iteration

        # updates x0 to x1
        x0 = x1


while True:
    # Gets the equation from the user
    user_input = input("Enter a function of x in a python readable line (e.g., x**2 + 3), the sympy library is "
                       "imported so please use it as you'd like: ")

    # Gets the position
    position = float(input("Enter your position value: "))

    # Gets the stopping criteria
    stopping_criteria = input("Enter 'absolute_approximate', 'absolute_relative', 'true_absolute_error', 'conjunction' "
                              "for the stopping criteria that you want, or exit to leave: ")

    # Gets the threshold value
    delta = float(input("Enter your threshold value: "))
    match stopping_criteria:
        case 'absolute_approximate':
            print("Value, Iterations")
            print(newtons(position, stopping_criteria, user_input, delta))
            print("\n")
        case 'absolute_relative':
            print("Value, Iterations")
            print(newtons(position, stopping_criteria, user_input, delta))
            print("\n")
        case 'true_absolute_error':
            print("Value, Iterations")
            print(newtons(position, stopping_criteria, user_input, delta))
            print("\n")
        case 'conjunction':
            print("Value, Iterations")
            print(newtons(position, stopping_criteria, user_input, delta))
        case 'exit':
            break
