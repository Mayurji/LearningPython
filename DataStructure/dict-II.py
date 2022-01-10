# Calculating On Dictionary
stock_prices = {
    'zerodha': 100,
    'Groww': 67,
    'Upstox': 65
    }

prices = {'BBB': 34.5, 'AAA': 34.5}

"""Using zip(), we compare the values in the tuple and then key. If value are same, then key takes over."""
print(f'Stock with Max Price: {max(zip(stock_prices.values(), stock_prices.keys()))}\n')
print(f'Stock with Min Price: {min(zip(stock_prices.values(), stock_prices.keys()))}\n')
print(f'Find min, when Stock prices are same: {min(zip(prices.values(), prices.keys()))}\n')
print(f'Find max, when Stock prices are same: {max(zip(prices.values(), prices.keys()))}\n')

# Sorting Stock Prices
print(f'Sorting Stock Prices: {sorted(zip(stock_prices.values(), stock_prices.keys()))}\n')

# Find key corresponding to min/max value
print(f"Stock with min value: {min(stock_prices, key=lambda k: stock_prices[k])}\n")
print(f"Stock with max value: {max(stock_prices, key=lambda k: stock_prices[k])}\n")

# Find common between two dictionary
a = {'x': 1, 'y': 2, 'z': 3, 'f': 9}
b = {'w': 1, 'z': 2, 'a': 3, 'f': 9}

# Find keys in common
print(f'Common Keys In a and b: {a.keys() & b.keys()}\n')

# Find keys in a that are not in b
print(f'Common Keys In a and b: {a.keys() - b.keys()}\n')

# Find keys and value pairs in common
print(f'Common Key and Value pair in a and b: {a.items() & b.items()}\n')

# Create new dict from existing dict with one element removed.
c = {key: a[key] for key in a.keys() - {'f'}}
print(f'New Dict c: {c}')