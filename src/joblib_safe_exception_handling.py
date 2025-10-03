"""
Safe exception handling with joblib parallel execution

This example shows how to catch exceptions inside the worker function
and return structured results, allowing you to collect both successes
and failures in the same results list.
"""

from joblib import Parallel, delayed


def safe_maybe_fail(x):
    try:
        if x == 5:
            raise ValueError("Boom! I don't like 5 😤")
        return ("ok", x * 2)
    except Exception as e:
        return ("error", str(e))


results = Parallel(n_jobs=4)(delayed(safe_maybe_fail)(i) for i in range(10))

print(results)
