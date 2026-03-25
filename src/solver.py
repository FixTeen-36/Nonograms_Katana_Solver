def get_all_row_options(row_len: int, elements: list) -> list:  # el: elments_ length
    remainder = row_len - (sum(elements) + len(elements) - 1)  # remainder: how many blank spaces are after the last element 
    cc = remainder
    coordinates = []
    for length in elements:
        to_extend = range(cc, (cc + length))
        coordinates.extend(list(to_extend))
        cc += length + 1

    options = [coordinates]
    number_of_copies = [0] * remainder
    s_n = 1  # sum of number of copies
    for i in range(len(elements)):
        for _ in range(remainder):
            for coordinates in options[-s_n:]:
                c_copy = coordinates[:]
                j_a = sum(elements[:i])
                c_copy.insert(j_a, (c_copy[j_a] - 1))
                j_b = sum(elements[:(i + 1)])
                c_copy.pop(j_b)
                options.append(c_copy)
            number_of_copies.append(s_n)
            s_n -= number_of_copies.pop(0)
        s_n = sum(number_of_copies)

    return options


def solve_row(row: list, options: list) -> set:
    points = set()
    crosses = set()
    for i, value in enumerate(row):
        if value == 1:
            points.add(i)
        if value == 2:
            crosses.add(i)
    
    to_pop = []
    intersection = set(range(len(row))) - points
    substraction = set(range(len(row))) - crosses
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

    return intersection | substraction


def solve_blank_row(row: list, elements: list) -> set:
    remainder = len(row) - (sum(elements) + len(elements) - 1)  # remainder: how many blank spaces are after the last element 
    coordinate = 0
    points = []
    for length in elements:
        if remainder < length:
            to_extend = range((coordinate + remainder), (coordinate + length))
            points.extend(list(to_extend))
        coordinate += length + 1
    
    for i in points:
        row[i] = 1
    
    if remainder == 0:
        coordinate = 0
        for length in elements[:-1]:
            coordinate += length
            row[coordinate] = 2
            coordinate += 1
        return set(range(len(row)))
    
    return set(points)


def solve_field(x_elements: list, y_elements: list) -> list:
    m = len(x_elements)  # number of rows
    n = len(y_elements)  # number of columns
    field = [0] * (m * n)

    columns_to_solve = set()
    for i in range(m):  # solve blank rows
        row = [0] * n
        columns_to_solve |= solve_blank_row(row, x_elements[i])
        field[i*n:(i + 1)*n] = row

    rows_to_solve = set() 
    for i in (set(range(n)) - columns_to_solve):  # solve blank columns
        column = [0] * m
        rows_to_solve |= solve_blank_row(column, y_elements[i])
        field[i::n] = column

    x_options = [get_all_row_options(n, elements) for elements in x_elements]
    y_options = [get_all_row_options(m, elements) for elements in y_elements]

    to_continue = True
    while to_continue:
        for i in rows_to_solve:  # solve rows
            row = field[i*n:(i + 1)*n]
            columns_to_solve |= solve_row(row, x_options[i])
            field[i*n:(i + 1)*n] = row
        rows_to_solve = set()
        
        for i in columns_to_solve:  # solve columns
            column = field[i::n]
            rows_to_solve |= solve_row(column, y_options[i])
            field[i::n] = column
        columns_to_solve = set()

        to_continue = True if rows_to_solve else False

    return field, m, n
