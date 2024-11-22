from sympy import *

def newtons_for_extrema(x0, tolerance, user_function):
    x_current = x0
    x_next = 0.0
    iterations = 0.0
    scaling_coefficient = 0.1

    x = symbols('x')

    # sets up a function using lambda to set up the user's given function for usability
    user_expression = eval(user_function)
    user_expression_for_use = lambda x: eval(user_function)

    # First derivative of the user's expression
    # The use of .doit() forces it to do the actual derivative
    # Casting to a string allows for the eval to use a string version of the derivative that works rather than a
    # derivative object that it can't

    derived_function = Derivative(user_expression, x).doit()
    derivative_for_use = lambda x: eval(str(derived_function))

    # Second derivative of the user's expression
    second_order_derivative = Derivative(derived_function, x).doit()
    second_order_derivative_for_use = lambda x: eval(str(second_order_derivative))

    while True:
        iterations += 1
        x_next = x_current - scaling_coefficient * (derivative_for_use(x_current) / second_order_derivative_for_use(x_current))
        if abs(x_next - x_current) <= tolerance:
            return x_next, user_expression_for_use(x_next), iterations
        else:
            x_current = x_next


if __name__ == "__main__":
    while True:
        # Gets the equation from the user
        user_input = input("Enter a function of x in a python readable line (e.g., x**2 + 3), the sympy library is "
                           "imported so please use it as you'd like: ")

        # Gets the threshold value
        delta = float(input("Enter your threshold value: "))

        # Gets x0 value
        x0 = input("Please choose a starting value relatively close to the solution: ")

        results = newtons_for_extrema(float(x0), float(delta), user_input)
        print(f"The x value of the local extrema is: {results[0]}")
        print(f"The y value of the local extrema is: {results[1]}")
        print(f"The amount of iterations it took was: {results[2]}")


