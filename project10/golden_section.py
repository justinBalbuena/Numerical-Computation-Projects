from sympy import *


def golden_section(a, b, user_function, type, tolerance):
    golden_num = 1.618

    user_function = lambdify(user_function)

    x1 = None
    x2 = None
    y1 = None
    y2 = None

    match type:
        case 'min':
            while abs(b - a) < tolerance:
                x1 = b - (b -a) / 2
                x2 = a + (b - a) / 2
                y1 = user_function(x1)
                y2 = user_function(x2)

                if y1 >= y2:
                    a = x1
                    x1 = x2
                    x2 = a + (b - a) / golden_num
                    y1 = user_function(x1)
                    y2 = user_function(x2)
                else:
                    b = x2
                    x2 = x1
                    x1 = b - (b - a) / golden_num
                    y1 = user_function(x1)
                    y2 = user_function(x2)
        case 'max':
            while abs(b - a) < tolerance:
                x1 = b - (b - a) / golden_num
                x2 = a + (b - a) / golden_num
                y1 = user_function(x1)
                y2 = user_function(x2)

                if y1 <= y2:
                    a = x1
                    x1 = x2
                    x2 = a + (b - a) / golden_num
                    y1 = user_function(x1)
                    y2 = user_function(x2)
                else:
                    b = x2
                    x2 = x1
                    x1 = b - (b - a) / golden_num
                    y1 = user_function(x1)
                    y2 = user_function(x2)

    return (a + b) / 2

