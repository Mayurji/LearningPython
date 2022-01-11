import heapq

numbers = [89, 45, 23, -19, 78, 23, 56, -98]

# Find N Largest
print(f'Three Largest Number: {heapq.nlargest(3, numbers)}')

# Find N Smallest
print(f'Three Smallest Number: {heapq.nsmallest(3, numbers)} \n')

# Heap On Dict
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09}
]

cheap_stock = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
print(f'Cheap Stock: {cheap_stock}')

expensive_stock = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
print(f'Expensive Stock: {expensive_stock}\n')

# Find the smallest or the largest one at a time.
heap = numbers
heapq.heapify(numbers)
print(f'Heapified Heap: {heap}\n')

print(f'First Smallest: {heapq.heappop(heap)} \n')
print(f'Second Smallest: {heapq.heappop(heap)}')

"""
Also checkout:
.heappop()
.heappush()
.heappushpop()
"""