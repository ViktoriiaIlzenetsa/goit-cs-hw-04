from threading import Thread
from time import time
from collections import defaultdict
from pathlib import Path

from boyer_moore_search import boyer_moore_search

def search_in_file(path, patterns: list, res_dict):
    folder = Path(path).glob('*')
    for file in folder:
        try:
            with open(file, "r") as f:
                text = f.read()
                for pattern in patterns:
                    result = boyer_moore_search(text, pattern)
                    if result >= 0:
                        res_dict[pattern].append(str(file))
        except IOError as e:
            print(f"Error reading file {file}: {e}")
    return res_dict



if __name__ == "__main__":
    timer = time()
    results = defaultdict(list)
    threads = [Thread(target=search_in_file, args=(f"{i}", ["Significant", "Strategy", "Million"], results)) for i in range(3)]

    
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print(f'Time taken with Threads: {round(time() - timer, 4)}\n')

    for key in results:
        print(f"{key}: {results[key]}\n")
       

