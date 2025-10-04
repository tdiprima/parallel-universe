"""
Flaky task with manual retries example using joblib

This example shows a pattern for automatically retrying failed tasks
up to a maximum number of attempts before giving up. Each task has
a 30% chance of failing to simulate real-world flaky operations.
"""

import random

from joblib import Parallel, delayed


def flaky_task(x, attempt=1, max_attempts=3):
    try:
        # Simulate a flaky failure: 30% chance of error
        if random.random() < 0.3:
            raise RuntimeError(f"Task {x} failed on attempt {attempt}")
        return ("ok", x, x * 2)
    except Exception as e:
        if attempt < max_attempts:
            # Retry by calling itself again
            return flaky_task(x, attempt + 1, max_attempts)
        return ("error", x, str(e))


results = Parallel(n_jobs=4)(delayed(flaky_task)(i) for i in range(10))

successes = [(inp, out) for tag, inp, out in results if tag == "ok"]
errors = [(inp, err) for tag, inp, err in results if tag == "error"]

print("✅ Successes:", successes)
print("❌ Errors (after retries):", errors)
