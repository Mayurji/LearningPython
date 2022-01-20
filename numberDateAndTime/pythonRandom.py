import random

a = [1, 2, 3, 4, 5]
print(f'Selecting at Random: {random.choice(a)}')
print(f'Sampling n at Random: {random.sample(a, 2)}')
random.shuffle(a)
print(f'Shuffling at Random: {a}')
print(f'Selecting Int in Range: {random.randint(0, 10)}')
print(f'Selecting Float in [0-1]: {random.random()}')
