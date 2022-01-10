"""
Transformation And Reduction At The Same Time Using Generator Expression
"""
import os

# Sum Of Squares
sequence = [1, 2, 3, 4]
sos = sum(x * x for x in sequence)
print(f'Sum Of Squares: {sos}')

# Check if .py file type exists in directory
files = os.listdir('../DataStructure')
if any(file.endswith('.py') for file in files):
    print("Python file exists!")
else:
    print("No python file exists!")

# Output tuple as CSV
s = ('AAPL', 89, 345)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}]

min_shares = min(s['shares'] for s in portfolio)
print(f'Min Share Price: {min_shares}')

"""
Alternative Technique using temporary list
It creates an extra list, for large numbers,
it will be inefficient.
"""
min_shares = min([s['shares'] for s in portfolio])
print(f'Using List: {min_shares}')