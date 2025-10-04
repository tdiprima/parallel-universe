# 💪 CPU muscles flexing! One process per core, maximum power mode.
# When math gets heavy, spawn an army of processes to crunch those numbers.
# GIL who? These processes laugh in the face of Python's limitations! 🔥

from multiprocessing import Process, cpu_count


def compute(n):
    print(f"Computing {n}")
    total = sum(i * i for i in range(10_000_000))
    print(f"Done {n}: {total}")


if __name__ == "__main__":
    processes = []
    for i in range(cpu_count()):
        p = Process(target=compute, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
