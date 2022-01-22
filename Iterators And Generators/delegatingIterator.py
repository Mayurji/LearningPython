class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._children = []

    def __repr__(self) -> str:
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
for n in root:
    print(n)

# Creating a Countdown
def countdown(n):
    print(f'Starting Count from {n}')
    while n > 0:
        yield n
        n -= 1
    print('Done!')

c = countdown(5)
print(next(c))
print(next(c))
print(next(c))
