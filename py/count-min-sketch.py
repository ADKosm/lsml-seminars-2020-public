import argparse
import csv
import random
import sys

TABLE_SIZE = 5000
HASHES_COUNT = 10


def generate_hash(size):
    p1, p2, p3 = random.randint(10, 10**8), random.randint(10, 10**8), random.randint(10, 10**8)

    def _hash(value):
        return (p1 + value * p2 + value ** 2 * p3) % size

    return _hash


def main(query_file_path):
    stream = map(lambda x: int(x[8]), csv.reader(iter(sys.stdin.readline, '')))

    for element in stream:
        pass # DO IT

    with open(query_file_path, "r") as f:
        for query in map(int, f):
            print(0) # DO NOT FORGET TO ALSO UPDATE THIS


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('queries', metavar='query', type=str, nargs='?',
                        help='path to queries file')
    args = parser.parse_args()
    main(args.queries)
