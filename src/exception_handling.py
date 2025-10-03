"""
Exception handling example with joblib parallel execution

This example shows what happens when one of the parallel tasks
raises an exception - joblib stops and propagates the first exception.
"""

from joblib import Parallel, delayed


def maybe_fail(x):
    if x == 5:
        raise ValueError("Boom! I don't like 5 😤")
    return x * 2


try:
    results = Parallel(n_jobs=4)(delayed(maybe_fail)(i) for i in range(10))
    print("Results:", results)
except Exception as e:
    print("Caught exception:", e)
