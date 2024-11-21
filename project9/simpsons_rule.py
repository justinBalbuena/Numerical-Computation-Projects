def count_decimal_places(number):
    """

    :param number:
    :return: the amount of numbers after the decimal point
    """
    # Convert to string
    number_str = str(number)

    # Split at the decimal point and count the length of the decimal part
    if '.' in number_str:
        decimal_part = number_str.split(".")[1]
        return len(decimal_part)
    else:
        return 0  # No decimal part


def lagrange_interpolation(values, wanted_value):
    """

    :param values: dictionary of x and matching f(x) values
    :param wanted_value: the value that the user wants to interpolate
    :return: the interpolated value
    """
    sorted_values = dict(sorted(values.items()))
    x_vals = list(sorted_values.keys())
    y_vals = list(sorted_values.values())
    x_vals.sort()
    y_vals.sort()

    x_vals = x_vals[0:3]
    y_vals = y_vals[0:3]

    interpolated_value = 0

    for i in range(len(x_vals)):
        lagrange = 1.0
        for j in range(len(x_vals)):
            if j != i:
                lagrange *= (wanted_value - x_vals[j]) / (x_vals[i] - x_vals[j])
        interpolated_value += lagrange * y_vals[i]
    return interpolated_value


def composite_simpsons(values, h, n):
    """

    :param values: dictionary of x and matching f(x) values
    :param h: length of sub intervals
    :param n: amount of sub intervals
    :return:
    """
    if n % 2 != 0:
        return "Composite Simpsons rule requires an even about of intervals"

    values_copy = values.copy()
    sorted_values = dict(sorted(values.items()))
    x_vals = list(sorted_values.keys())

    i = x_vals[0]

    # Keeps track of how many numbers after the decimal point are
    # important because of a floating point error in this solution
    # when calculating x_vals based off of the distance between x values
    amount_of_decimals = count_decimal_places(i + h)
    counter = 0
    while i < x_vals[-1]:
        if i not in values_copy:
            values_copy[i] = lagrange_interpolation(values, i)

        i = i + h
        i = round(i, amount_of_decimals)
        counter = counter + 1
    # After this while loop, every value that should have its output, based on the steps between x values
    # have been found are catalogued

    sorted_values = dict(sorted(values_copy.items()))
    x_vals = list(sorted_values.keys())
    y_vals = list(sorted_values.values())

    summation = y_vals[0] + y_vals[len(y_vals) - 1]
    for i in range(1, len(x_vals) - 1):
        if i % 2 == 0:
            summation += 2 * y_vals[i]
        else:
            summation += 4 * y_vals[i]

    return (h / 3) * summation


cord_dict = {
    1.0: 1.543,
    1.1: 1.669,
    1.3: 1.971,
    1.4: 2.151,
    1.5: 2.352,
    1.7: 2.828,
    1.8: 3.107
}

testval = composite_simpsons(cord_dict, 0.1, 8)
print(testval)
