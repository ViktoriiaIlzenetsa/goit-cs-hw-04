from multiprocessing import Process, Queue
from collections import defaultdict
from time import time
from pathlib import Path

from boyer_moore_search import boyer_moore_search


def search_in_file(path, patterns: list, res_queue):
    folder = Path(path).glob('*')
    for file in folder:
        try:
            with open(file, "r") as f:
                text = f.read()
                for pattern in patterns:
                    result = boyer_moore_search(text, pattern)
                    if result >= 0:
                        res_queue.put((pattern, str(file)))
        except IOError as e:
            print(f"Error reading file {file}: {e}")

if __name__ == "__main__":
    timer = time()
    res_queue = Queue()
    results = defaultdict(list)

    processes = [Process(target=search_in_file, args=(f"{i}", ["Significant", "Strategy", "Million"], res_queue)) for i in range(3)]

    [process.start() for process in processes]
    [process.join() for process in processes]

    while not res_queue.empty():
        pattern, file = res_queue.get()
        results[pattern].append(file)

    print(f'Time taken with Processes: {round(time() - timer, 4)}\n')

    for key in results:
        print(f"{key}: {results[key]}\n")


