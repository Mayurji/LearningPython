from collections import deque

# Fixed Size Queue

fixed_size_queue = deque(maxlen=3)
fixed_size_queue.append(1)
fixed_size_queue.append(2)
fixed_size_queue.append(3)
print(f"At size 3: {fixed_size_queue}")

fixed_size_queue.append(4)
fixed_size_queue.append(5)
print(f"Replacing after size 3 is filled: {fixed_size_queue}")

fixed_size_queue.appendleft(9)
print(f'Appending to left: {fixed_size_queue}')

"""
Checkout:
.appendleft()
.pop()
.popleft()
"""
# Finding the last N items

def search(lines, pattern, history=3):
    previous_line = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_line
        previous_line.append(line)


with open('dummy.txt') as f:
    for line, previousLine in search(f, 'python', 3):
        for pline in previousLine:
            print(pline, end='')
        print(line, end='')
        print('-'*20)