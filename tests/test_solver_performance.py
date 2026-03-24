from context import *
import trace
import linecache

print("test is running")
# input data
src_version = get_src_version()
input_file = "pelican"

# run example
analyser = trace.Trace(trace=0, ignoredirs='src.data_manager.py')
analyser.runfunc(solve_field, *read_pattern(input_file))

# get analyser results
results = []
for (_, line_no), iterations in analyser.counts.items():
    results.append((line_no, iterations))
results = dict(results)

# display summary
summary  =  "solver performance test results\n"
summary += f"src version: {src_version}\n"
summary += f"input file: {input_file}.csv\n"
summary += f"total iterations: {sum(results.values()):,}"
print(summary)

# write results in file
src_version = src_version.replace('.', '_')
file_name = f"sptr_v_{src_version}_{input_file}.txt"
with open(f'tests\\solver_performance_results\\v_{src_version}\\{file_name}', "w") as f:
    f.write(summary + "\n\n")
    f.write("solver.py line execution statistics:\n")
    for line_no, code_line in enumerate(linecache.getlines('src\\solver.py'), 1):
        prefix = f"{results[line_no]:8d}: " if line_no in results.keys() else (" " * 10)
        f.write(prefix + code_line)

print("test is finished")
