from src import *

# type a file name from 'data' directory
name = "cobra"

print(f"{name}:")
print_field(*solve_field(*read_pattern(name)))
