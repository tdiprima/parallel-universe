"""
⚔️ The ultimate concurrency battle! Processes vs Threads face off.
CPU-heavy tasks? Processes rule! I/O waiting? Threads take the crown!
Choose your fighter wisely! 🥊

The if __name__ == '__main__': protection is required when using multiprocessing 
to prevent child processes from re-executing the main module code during spawning.
"""
import concurrent.futures
import time


def cpu_task(n):
    return sum(i * i for i in range(n))


def io_task(seconds):
    time.sleep(seconds)
    return f"Waited {seconds}s"


if __name__ == '__main__':
    # Multiprocessing for CPU
    with concurrent.futures.ProcessPoolExecutor() as pool:
        print(list(pool.map(cpu_task, [10_000_000, 20_000_000])))

    # Threading for I/O
    with concurrent.futures.ThreadPoolExecutor() as pool:
        print(list(pool.map(io_task, [1, 2, 3])))
