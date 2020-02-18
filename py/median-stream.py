import sys
import csv

MEMORY = 5000
A = []


stream = map(lambda x: int(x[6]), csv.reader(iter(sys.stdin.readline, '')))

for _ in range(MEMORY):
    A.append(next(stream))

A_min = min(A)
A_max = max(A)

larger = 0
less = 0
N = len(A)

for element in stream:
    N += 1
    if element > A_max:
        larger += 1
    elif element < A_min:
        less += 1
    else:
        if less < larger:
            A.remove(A_min)
            A.append(element)
            A_min = min(A)
            less += 1
        else:
            A.remove(A_max)
            A.append(element)
            A_max = max(A)
            larger += 1

if less < N / 2 and larger < N / 2:
    median_index = N // 2 - less
    A.sort()
    result = A[median_index]
    print(result)
else:
    print("FAIL")
    print(N, less, larger, A_min, A_max)
