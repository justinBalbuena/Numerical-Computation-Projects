def lagrange_interpolation(values, wanted_value, type):
    sorted_values = dict(sorted(values.items()))
    x_vals = list(sorted_values.keys())
    y_vals = list(sorted_values.values())
    x_vals.sort()
    y_vals.sort()

    match type:
        case 'quadratic':
            if len(x_vals) >= 3:
                x_vals = x_vals[0:3]
                y_vals = y_vals[0:3]
            else:
                print("Not enough values for cubic so all values will be used")
        case 'cubic':
            if len(x_vals) >= 4:
                x_vals = x_vals[0:4]
                y_vals = y_vals[0:4]
            else:
                print("Not enough values for quadratic so all values will be used")

    interpolated_value = 0

    for i in range(len(x_vals)):
        lagrange = 1.0
        for j in range(len(x_vals)):
            if j != i:
                lagrange *= (wanted_value - x_vals[j]) / (x_vals[i] - x_vals[j])
        interpolated_value += lagrange * y_vals[i]
    return interpolated_value


def lagrange_with_diff(values, step, flag, type):
    """

    :param values: dictionary of x and y values
    :param step: value of h
    :param flag: the kind of formula to use
    :param type: type of interpolation to use
    :return: the derivative found using the formulas and interpolating
    """

    values_copy = values.copy()
    user_input = float(input("What derivative value do you want: "))
    y0 = None
    if user_input not in values:
        y0 = lagrange_interpolation(values_copy, user_input, type)
        values_copy[user_input] = y0
    # at this point I have x0 and its matching y-value

    match flag:
        case 'a':
            x_plus_h = user_input + step
            if x_plus_h not in values:
                y_for_plusH = lagrange_interpolation(values, x_plus_h, type)
                values_copy[x_plus_h] = y_for_plusH

            # at this point I have both x0 and x0+h with their matching y values
            deriv_x0 = (values_copy[x_plus_h] - values_copy[user_input]) / step
            return deriv_x0
        case 'b':
            x_plus_h = user_input + step
            if x_plus_h not in values:
                y_for_plusH = lagrange_interpolation(values, x_plus_h, type)
                values_copy[x_plus_h] = y_for_plusH

            x_plus_twoh = user_input + 2 * step
            if x_plus_twoh not in values:
                y_for_plustwoH = lagrange_interpolation(values, x_plus_twoh, type)
                values_copy[x_plus_twoh] = y_for_plustwoH

            # at this point I have x0, x0+h, and x0+2h with their matching y values

            deriv_x0 = ((-1.0 * (values_copy[x_plus_twoh])) + (4*values_copy[x_plus_h]) - (3*values_copy[user_input])) / (2*step)
            return deriv_x0
        case 'c':
            x_plus_h = user_input + step
            if x_plus_h not in values:
                y_for_plusH = lagrange_interpolation(values, x_plus_h, type)
                values_copy[x_plus_h] = y_for_plusH

            x_minus_h = user_input - step
            if x_minus_h not in values:
                y_for_plusH = lagrange_interpolation(values, x_minus_h, type)
                values_copy[x_minus_h] = y_for_plusH

            # at this point I have x0-h, x0, and x0+h with their matching y values

            deriv_x0 = (values_copy[x_plus_h] - values_copy[x_minus_h]) / (2*step)
            return deriv_x0
        case _:
            return "Did not enter a flag value"


cord_dict = {
    0.15: 0.1761,
    0.21: 0.3222,
    0.23: 0.3617,
    0.27: 0.4314,
    0.32: 0.5051,
    0.35: 0.54410
}

testval = lagrange_with_diff(cord_dict, 0.01, 'a', 'cubic')
print(testval)

