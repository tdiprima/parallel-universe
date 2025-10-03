"""
Basic parallel execution example using joblib

This example demonstrates how to run a slow function in parallel
using joblib's Parallel and delayed functions.
"""

import time

from joblib import Parallel, delayed


def slow_square(x):
    time.sleep(0.1)  # pretend it's slow
    return x * x


# Run in parallel with 4 workers
results = Parallel(n_jobs=4)(delayed(slow_square)(i) for i in range(10))

print("Results:", results)
print("Type:", type(results))
