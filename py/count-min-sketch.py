import random
import csv
import sys


def generate_hash(size):
    p1, p2, p3 = random.randint(10, 10**8), random.randint(10, 10**8), random.randint(10, 10**8)

    def _hash(value):
        return (p1 + value * p2 + value ** 2 * p3) % size

    return _hash

TABLE_SIZE = 5000
HASHES_COUNT = 10

stream = map(lambda x: int(x[8]), csv.reader(iter(sys.stdin.readline, '')))

for element in stream:
    pass # DO IT

query_file_path = sys.argv[1]
with open(query_file_path, "r") as f:
    for query in map(int, f):
        print(0) # DO NOT FORGET TO ALSO UPDATE THIS
