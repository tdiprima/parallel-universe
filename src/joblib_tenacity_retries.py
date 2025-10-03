"""
Tenacity-based retry example with joblib parallel execution

This example demonstrates using the tenacity library for robust retry logic
with exponential backoff. Tenacity provides better retry handling than
manual retry loops with configurable stop conditions and wait strategies.

The issue is that the @retry decorator from tenacity creates a wrapper that contains thread-local
objects that can't be pickled. The solution is to move the retry logic inside the function that gets
executed in parallel, rather than decorating the function itself.
"""

import random

from joblib import Parallel, delayed
from tenacity import RetryError, retry, stop_after_attempt, wait_exponential


def flaky_task(x):
    # Create the retry decorator inside the function to avoid pickling issues
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=4))
    def _task():
        # Simulate 30% failure chance
        if random.random() < 0.3:
            raise RuntimeError(f"Task {x} failed")
        return x * 2
    
    return _task()


def safe_flaky(x):
    try:
        return ("ok", x, flaky_task(x))
    except RetryError as e:
        return ("error", x, str(e))


results = Parallel(n_jobs=4)(delayed(safe_flaky)(i) for i in range(10))

successes = [(inp, out) for tag, inp, out in results if tag == "ok"]
errors = [(inp, err) for tag, inp, err in results if tag == "error"]

print("✅ Successes:", successes)
print("❌ Errors (after retries):", errors)
