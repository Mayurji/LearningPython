from itertools import compress

"""Python Best Practices - Filter"""

sequence = [3, 2, -4, 6, 8, -2, 4, -6]

#Filter Sequence & List Comprehension
print(f"Positive Numbers alone: {[num for num in sequence if num > 0]}")

#Filter Sequence & List Comprehension
print(f"Negative Numbers alone: {[num for num in sequence if num < 0]}")

"""Downside of using list comprehension, for large list it produces larger result.
better to use generators."""
print(f"Negative Numbers alone: {(num for num in sequence if num < 0)}")

# Using Filter keyword
#sequence = ['3', '4', '-6', "GAS"]
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

int_val = list(filter(is_int, sequence))
print(f'Integers: {int_val}')

# Replace instead of Discarding
print(f'Turn Negative to Zero:{[n if n>0 else 0 for n in sequence]}')

# Using Compress keyword - Takes an iterable and corresponding boolean sequence.
salary = [5000, 10000, 50000, 34000, 60000]
designation = ["Jn Dev", "Jn Dev II", 'Sn Dev', 'Sales', 'Sn Dev II']

more10k = [n>10000 for n in salary]
print(f'Designation With Salary > 10K: {list(compress(designation, more10k))}')