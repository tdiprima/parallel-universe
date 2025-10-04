# 🎭 Twin executors in action! Same task, different stages.
# ThreadPool for the warm-up act, ProcessPool for the main event.
# Same function, different performance - it's all about the venue! 🎪

import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def square(n):
    time.sleep(1)
    return n * n


if __name__ == "__main__":
    # Thread pool
    with ThreadPoolExecutor() as executor:
        results = executor.map(square, range(5))
        print("Thread results:", list(results))

    # Process pool
    with ProcessPoolExecutor() as executor:
        results = executor.map(square, range(5))
        print("Process results:", list(results))
