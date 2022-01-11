# Dictionary Comprehension

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'FB': 10.75
}

# Find Stocks with price > 200
more_200 = {key: value for key, value in prices.items() if value > 200}
print(f'Stock with price > 200: {more_200}')

# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'FB' }
tech_stocks = { key:value for key,value in prices.items() if key in tech_names }
print(f'Tech stocks: {tech_stocks}')

# Update Dictionary
prices.update({'FB':78})
print(f'Updated FB price:{prices}')
