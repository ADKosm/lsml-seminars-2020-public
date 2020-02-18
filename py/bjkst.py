import random
import csv
import sys


def generate_hash(size):
    p1, p2, p3 = random.randint(10, 10**8), random.randint(10, 10**8), random.randint(10, 10**8)

    def _hash(value):
        return (p1 + value * p2 + value ** 2 * p3) % size

    return _hash

def zeros(number):
    result = 0
    while number and number & 1 == 0:
        result += 1
        number = number >> 1
    return result

MEMORY = 5000

stream = map(lambda x: int(x[8]), csv.reader(iter(sys.stdin.readline, '')))

for element in stream:
    pass # DO IT

result = 0
print(result)
