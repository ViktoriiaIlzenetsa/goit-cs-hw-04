from threading import Thread, current_thread
from multiprocessing import Process, current_process
from time import time
from pathlib import Path

from boyer_moore_search import boyer_moore_search

def worker(path, pattern):
    folder = Path(path).glob('*')
    for file in folder:
        with open(file, "r") as f:
            text = f.read()
            result = boyer_moore_search(text, pattern)
        if result >= 0:
            print(f"{current_process().name:^25}|{current_thread().name:^25}|{result:^20}|    {file}")



if __name__ == "__main__":
    threads = [Thread(target=worker, args=(f"{i}", "Significant")) for i in range(3)]

    timer = time()
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print(f'Elapsed time Threads: {round(time() - timer, 4)}')

    processes = [Process(target=worker, args=(f"{i}", "Significant")) for i in range(3)]

    timer = time()
    [process.start() for process in processes]
    [process.join() for process in processes]
    print(f'Elapsed time Process: {round(time() - timer, 4)}')
