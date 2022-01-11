import heapq

class PriorityQueue:
    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """
        Priority is negated, bcz by default heap uses min-heap.
        min-heap orders values from small to large. Hence, 
        we negate to keep values from large to small.

        index property: It helps when item with similar priority
        is appended. It pops element which entered first based on
        value.
        """
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return 'Item({!r})'.format(self.name)

queue = PriorityQueue()
queue.push(Item('foo'), 1)
queue.push(Item('bar'), 5)
queue.push(Item('spam'), 4)
queue.push(Item('grok'), 1)

print(f'Popping Out Item with first highest priority: {queue.pop()}')
print(f'Popping Out Item with second highest priority: {queue.pop()}')