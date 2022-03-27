"""Function with arbitrary no. of arguments"""

def average(x, *y):
    return (x + sum(y)) / (1 + len(y))

print(f'Avg of two no. {average(5, 4)}')

print(f'Avg of arbitrary nos. {average(5, 4, 3, 2, 1)}')