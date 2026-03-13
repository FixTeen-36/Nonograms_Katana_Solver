def print_indeces(row_len: int):
    print("   |", end="")
    for i in range(row_len):
        print(f"{i:2d}|", end="")
    print()


def print_row(row: list, index: int = None):
    index_text = f"{index:2d} " if (index or index == 0) else "   "
    print(f"{index_text}|", end="")
    for i in row:
        if i == 0:
            print("  |", end="")
        elif i == 1:
            print(" #|", end="")
        elif i == 2:
            print(" .|", end="")
    print("")


def print_row_options(row: list, options: list, description: str = "Row Options:"):
    print(description)
    print_indeces(len(row))
    for i, coordinates in enumerate(options):
        print(f"{i:2d} |", end="")
        for j in range(len(row)):
            if j in coordinates:
                print(" #|", end="")
            else:
                print("  |", end="")
        print()


def print_field_debuging(field: list, m: int, n: int):
    print_indeces(n)
    for i in range(m):
        print_row(field[i*n:(i + 1)*n], i)


def print_field(field: list, m: int, n: int):
    for i in range(m):
        row = field[i*n:(i + 1)*n]
        for j in row:
            if j == 1:
                print(" #", end="")
            else:
                print("  ", end="")
        print()
