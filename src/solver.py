def get_all_row_options(row_len: int, el: list) -> list:  # el: elments_ length
    remainder = row_len - (sum(el) + len(el) - 1)  # remainder: how many blank spaces are after the last element 
    cc = remainder
    coordinates = []
    for length in el[:]:
        to_extend = range(cc, (cc + length))
        coordinates.extend(list(to_extend))
        cc += length + 1

    options = [coordinates]
    number_of_copies = [0] * remainder
    s_n = 1  # sum of number of copies
    for i in range(len(el)):
        for _ in range(remainder):
            for coordinates in options[-s_n:]:
                c_copy = coordinates[:]
                j_a = sum(el[:i])
                c_copy.insert(j_a, (c_copy[j_a] - 1))
                j_b = sum(el[:(i + 1)])
                c_copy.pop(j_b)
                options.append(c_copy)
            number_of_copies.append(s_n)
            s_n -= number_of_copies.pop(0)
        s_n = sum(number_of_copies)

    return options


def solve_row(row: list, options: list) -> bool:
    points = set()
    crosses = set()
    for i, value in enumerate(row):
        if value == 1:
            points.add(i)
        if value == 2:
            crosses.add(i)
    
    to_pop = []
    intersection = set(range(len(row)))
    substraction = set(range(len(row)))
    for i, option in enumerate(options):
        coordinates = set(option)
        if (coordinates & crosses) or not(points <= coordinates):
            to_pop.append(i)
        else:
            intersection = intersection & coordinates
            substraction = substraction - coordinates

    for i in reversed(to_pop):
        options.pop(i)
    for i in intersection:
        row[i] = 1
    for i in substraction:
        row[i] = 2

    return True if to_pop else False


def solve_field(x_elements: list, y_elements: list) -> list:
    m = len(x_elements)  # number of rows
    n = len(y_elements)  # number of columns
    field = [0] * (m * n)

    x_options = [get_all_row_options(n, elements) for elements in x_elements]
    y_options = [get_all_row_options(m, elements) for elements in y_elements]

    to_continue = True
    while to_continue:
        to_continue = False
        for i in range(m):  # solve rows
            row = field[i*n:(i + 1)*n]
            if solve_row(row, x_options[i]):
                to_continue = True
            field[i*n:(i + 1)*n] = row

        for i in range(n):  # solve columns
            column = field[i::n]
            if solve_row(column, y_options[i]):
                to_continue = True
            field[i::n] = column

    return field, m, n
