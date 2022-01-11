"""
- Hashable data types: int , float , str , tuple , and NoneType . 
- Unhashable data types: dict , list , and set .

Yield Keyword
    -> Removing duplicate element from sequence without changing the order.
    -> Applicable on hashable type.
"""
# Yield On Hashable type
def dedupe(items):
    seen = set()
    for element in items:
        if element in seen:
            yield element
        seen.add(element)

a = [1, 2, 3, 4, 1, 2, 5, 6, 7, 4]
print(f'Remove Duplicates Without Changing Order: {list(dedupe(a))}\n')

#Yield On Unhashable type
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':2}]
print(f"Unique x and y pair on Unhashable Type: {list(dedupe(a, key=lambda d: (d['x'],d['y'])))}\n")
print(f"Unique x alone: {list(dedupe(a, key=lambda d: d['x']))}\n")

"""
Using Slice, to split unreadable mess of a string.
-> To avoid using hardcoded indices on string.
-> Better readability and maintenance.
"""

string = "ABCDEF#0123456789"
alpha = slice(0, 6)
number = slice(7, len(string))

print(f'Alphabets: {string[alpha]}\n')
print(f'Numbers: {string[number]}\n')

# Slice(start, stop, step)
a = slice(2, 10, 2)
for i in range(*a.indices(len(string))):
    print(string[i])