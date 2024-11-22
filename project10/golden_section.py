from sympy import *


def golden_section(a, b, user_function, type, tolerance):
    golden_num = 1.618

    user_expression = lambda x: eval(user_function)

    x1 = b - (b - a) / golden_num
    x2 = a + (b - a) / golden_num
    y1 = user_expression(x1)
    y2 = user_expression(x2)
    iterations = 0

    match type:
        case 'min':
            while abs(b - a) > tolerance:
                iterations += 1

                if y1 >= y2:
                    a = x1
                    x1 = x2
                    x2 = a + ((b - a) / golden_num)
                    y1 = user_expression(x1)
                    y2 = user_expression(x2)
                else:
                    b = x2
                    x2 = x1
                    x1 = b - (b - a) / golden_num
                    y1 = user_expression(x1)
                    y2 = user_expression(x2)
        case 'max':
            while abs(b - a) > tolerance:
                iterations += 1

                if y1 <= y2:
                    a = x1
                    x1 = x2
                    x2 = a + ((b - a) / golden_num)
                    y1 = user_expression(x1)
                    y2 = user_expression(x2)
                else:
                    b = x2
                    x2 = x1
                    x1 = b - (b - a) / golden_num
                    y1 = user_expression(x1)
                    y2 = user_expression(x2)

    return (a + b) / 2, user_expression((a + b) / 2), iterations





if __name__ == "__main__":
    while True:
        a = input("Enter your left bracket value: ")
        b = input("Enter your right bracket value: ")

        # Gets the equation from the user
        user_input = input("Enter a function of x in a python readable line (e.g., x**2 + 3), the sympy library is "
                           "imported so please use it as you'd like: ")

        type = input("Enter min or max for local maximum or minimum: ")

        tolerance = input("Enter your tolerance value: ")

        results = golden_section(float(a), float(b), user_input, type, float(tolerance))
        print(f"The x value of the local extrema is: {results[0]}")
        print(f"The y value of the local extrema is: {results[1]}")
        print(f"The amount of iterations it took was: {results[2]}")
