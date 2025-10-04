# 🧵 Threading the needle! Classic concurrent workers doing I/O busy work.
# Perfect for waiting tasks - while one thread naps, others keep hustling.
# The OG way to make Python do multiple things at once! 👷‍♀️

import threading
import time


def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)  # simulate work
    print(f"Worker {name} done")


if __name__ == "__main__":
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
