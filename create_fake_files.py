import logging
from faker import Faker
from os import path, mkdir


FILES_COUNT = 60

for i in range(3):
    try:
        parent_dir = path.relpath(f"{i}")
        mkdir(parent_dir)
    except FileExistsError:
        continue


fake = Faker()
for i in range(FILES_COUNT):
    file_name = fake.word() + ".txt"
    folder = f"{i%3}"
    file_path = path.relpath(f"{folder}/{file_name}")
    with open(file_path, "a") as f:
        for _ in range(100):
            f.write(fake.text())



