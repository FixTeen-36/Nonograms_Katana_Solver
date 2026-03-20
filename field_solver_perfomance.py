from src import *
import trace
import pickle

src_version = get_src_version()
print(f"Tested version: {src_version}")
tracer = trace.Trace(trace=0, outfile="perf_res", ignoredirs='src.data_manager.py')
tracer.runfunc(solve_field, *read_pattern("spartan"))

r = tracer.results()
r.write_results(show_missing=False, summary=True, coverdir="performance_results")

print("perf_ref:")
results = pickle.load(open("perf_res", "rb"))
total_results = sum(results[0].values())
print(f"The total number of iterations: {total_results}")
print("test is finished")