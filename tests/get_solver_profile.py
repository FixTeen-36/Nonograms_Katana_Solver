from cProfile import Profile
from context import *

# input data
input_file = "spartan"
input_data = read_pattern(input_file)

# run prolifer
profiler = Profile()
profiler.runcall(solve_field, *input_data)

# dump statistics
src_version = get_src_version()
src_version = "v_" + src_version.replace('.', '_')
file_name = f"{src_version}_{input_file}_profile"
profiler.dump_stats(f'tests\\solver_performance_results\\{src_version}\\{file_name}')

# print stats
profiler.print_stats()
