from src import *
import trace
import pickle

src_version = get_src_version()
print(f"Tested version: {src_version}")
tracer = trace.Trace(trace=0, outfile="performance_results/tracer_results", ignoredirs='src.data_manager.py')
tracer.runfunc(solve_field, *read_pattern("spartan  "))

r = tracer.results()
r.write_results(show_missing=False, coverdir="performance_results")

results = pickle.load(open("performance_results/tracer_results", "rb"))
total_results = sum(results[0].values())
print(f"Total number of cycles: {total_results:,}")
print("Test is finished")
