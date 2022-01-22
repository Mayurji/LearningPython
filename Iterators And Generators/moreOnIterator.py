import heapq
a = [1, 2, 8]
b = [3, 4, 5, 7]

for c in heapq.merge(a, b):
    print(f'Sorted Sequence: {c}')

import sys
f = open('dummy.txt')
for chunk in iter(lambda: f.read(3), ''):
    n = sys.stdout.write(chunk)