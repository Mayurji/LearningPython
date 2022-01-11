# Combine List Of Words
words = ["This", "is", "a", "sentence."]
print(f'Using join: {" ".join(w for w in words)}')
print(f'Using join: {",".join(words)}')

"""
Using + instead of join is inefficient.
- Garbage collection
- New String Object
- Memory Copies
"""
a, b, c = 'I', 'Love', 'Python'
print(a + ':' + b + ':' + c) # Ugly
print(':'.join([a, b, c])) # Still ugly
print(a, b, c, sep=':') # Better

# Usage: join over +