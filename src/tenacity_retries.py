"""
Tenacity + Joblib Retry Example

Shows how to use Tenacity for clean exponential backoff retries when running tasks in parallel.

⚠️ Gotcha: Tenacity's @retry decorator can't be pickled (thread-local stuff), so don't decorate the function directly.
✅ Instead, put the retry logic inside the function that runs in parallel.
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


# Run safe_flaky(i) in parallel across 4 processes for i = 0..9
results = Parallel(n_jobs=4)(delayed(safe_flaky)(i) for i in range(10))

# Loop over each item in results, unpack tuple, only keep the "ok" tuples
successes = [(inp, out) for tag, inp, out in results if tag == "ok"]
errors = [(inp, err) for tag, inp, err in results if tag == "error"]

print("✅ Successes:", successes)
print("❌ Errors (after retries):", errors)
