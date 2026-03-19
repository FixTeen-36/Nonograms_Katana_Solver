from .solver import *
from .results_printers import *
from .data_manager import *

__version__ = "1.0.0"

def get_src_version() -> str:
    return __version__

def print_row_debuging(row: list, elements_lengths: list, all_options: bool = True, solved_options: bool = True):
    print("Original Row:")
    print_indeces(len(row))
    print_row(row)
    
    options = get_all_row_options(len(row), elements_lengths)
    if all_options:
        print_row_options(row, options, "All Row Options:")

    solve_row(row, options)
    if solved_options:
        print_row_options(row, options, "Solved Row Options:")

    print("Solved Row:")
    print_indeces(len(row))
    print_row(row)
