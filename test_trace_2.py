from src import *
import trace

print("Test is started")
# Run example
analyser = trace.Trace(trace=0, ignoredirs='src.data_manager.py')
analyser.runfunc(solve_field, *read_pattern("castle"))

solver_statictics = []
for (_, line_no), iterations in analyser.counts.items():
    solver_statictics.append((line_no, iterations))

print("Test is finished")
