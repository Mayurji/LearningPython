# Filtering - Skip first occurence of t.
from itertools import dropwhile
from math import comb
with open('dummy.txt') as f:
    for line in dropwhile(lambda line: line.startswith('t'), f):
        print(line, end='')

#Filtering - When Input and output bound is known
from itertools import islice
items = ['a', 'b', 'c', 1, 2, 3, 4]
for x in islice(items, 3, None):
    print(x)

#Permutations
from itertools import permutations
items = ['a', 'b', 'c']
for p in permutations(items):
    print(f'All Combinations: {p}')

#Combinations
from itertools import combinations
for c in combinations(items, 3):
    print(f'Combinations {c}')

for c in combinations(items, 2):
    print(f'Combinations of two from 3 elements: {c}')

#Combinations with replacement
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(f'Combinations With Replacement: {c}')
