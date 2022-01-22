a = [1, 2, 3]
b = [4, 5, 6, 7, 8, 9]
c = (10, 11, 12)

for x, y in zip(a, b):
    print(f"Iterates till shortest sequence exhausts: {x, y}")

#To iterate until longest sequence exhaust
from itertools import zip_longest
for i in zip_longest(a, b):
    print(f"Iterates through longest sequence exhausts: {i}")

from itertools import chain
for x in chain(a, b, c):
    print(f'Chaining two lists: {x}')

#Flattening a nested sequence
nestedSequence = ['a', 'ab', ['c', 'cd', ['de', 'fg']]]
from collections.abc import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

for x in flatten(nestedSequence):
    print(f'Flattened Sequence: {x}')
