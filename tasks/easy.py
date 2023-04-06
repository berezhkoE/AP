import time
import threading
import multiprocessing

ns = [100000, 200000, 300000, 400000, 500000, 500000, 400000, 300000, 200000, 100000]
easy_path = "./artifacts/easy/easy.txt"


def fib(n: int):
    curr = 0
    next = 1
    ind = 0
    while ind < n:
        tmp = next
        next += curr
        curr = tmp
        ind += 1
    return curr


def get_time_parallel(lst):
    start = time.time()
    for worker in lst:
        worker.start()
    for worker in lst:
        worker.join()
    total = time.time() - start
    return total


def run_sync():
    result = 0
    for n in ns:
        start = time.time()
        fib(n)
        total = time.time() - start
        result += total

    return result


def run_with_threads():
    threads = []
    for n in ns:
        threads.append(threading.Thread(target=fib, args=(n,)))

    return get_time_parallel(threads)


def run_with_processes():
    processes = []
    for n in ns:
        processes.append(multiprocessing.Process(target=fib, args=(n,)))
    return get_time_parallel(processes)


def do_task():
    with open(easy_path, 'w') as file:
        file.write(f"Synchronously: {run_sync()} s\n")
        file.write(f"Threads: {run_with_threads()} s\n")
        file.write(f"Processes: {run_with_processes()} s\n")
