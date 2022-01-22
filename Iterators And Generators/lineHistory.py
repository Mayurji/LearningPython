# Line History
from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3) -> None:
        self.lines = lines
        self.history = deque(maxlen=histlen)
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line
    def clear(self):
        self.history.clear()

with open("dummy.txt") as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, line in lines.history:
                print(f"Previous Lines: {lineno, line}")
