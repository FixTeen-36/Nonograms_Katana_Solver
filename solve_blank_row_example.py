from src import *

# filled = 1, cross = 2, empty = 0
row = [0] * 10
elements = [1, 1, ]

solve_blank_row(row, elements)

print_indeces(len(row))
print_row(row)
