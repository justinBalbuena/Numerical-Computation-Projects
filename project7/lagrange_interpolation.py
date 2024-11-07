from sympy import *


def lagrange_interpolation(x_vals, y_vals, wanted_value):
    """

    :param x_vals: list of x values (positions)
    :param y_vals: list of y values (outputs)
    :param wanted_value: the position you want to interpolate
    :return: the interpolated value
    """

    interpolated_value = 0
    for i in range(len(x_vals)):
        lagrange = 1.0
        for j in range(len(x_vals)):
            if j != i:
                lagrange *= (wanted_value - x_vals[j]) / (x_vals[i] - x_vals[j])
        interpolated_value += lagrange * y_vals[i]
    return interpolated_value


x_array = [0.3, 0.5, 0.7, 0.9, 1.1]
y_array = [0.404958, 0.824361,  1.40963, 2.21364, 3.30458]

print(lagrange_interpolation(x_array, y_array, 0.6))
