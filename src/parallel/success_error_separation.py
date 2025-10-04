"""
Success/error separation example with joblib parallel execution

This example demonstrates how to separate successful results from errors
into two clean lists after parallel execution, making it easy to handle
both outcomes appropriately.
"""

from joblib import Parallel, delayed


def safe_maybe_fail(x):
    try:
        if x == 5:
            raise ValueError("Boom! I don't like 5 😤")
        return ("ok", x, x * 2)  # tag, input, output
    except Exception as e:
        return ("error", x, str(e))  # tag, input, error message


results = Parallel(n_jobs=4)(delayed(safe_maybe_fail)(i) for i in range(10))

# Separate into successes and errors
successes = [(inp, out) for tag, inp, out in results if tag == "ok"]
errors = [(inp, err) for tag, inp, err in results if tag == "error"]

print("✅ Successes:", successes)
print("❌ Errors:", errors)
