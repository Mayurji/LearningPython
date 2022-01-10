from collections import defaultdict
from collections import OrderedDict

# Typical use of dict is to map a value to a key
capital= {
    'TamilNadu': 'Chennai'
    }

# Storing multiple values to a key
vehicle = {
    'vehicle': ['car', 'bus', 'cycle']
    }

# Using defaultdict
"""defaultdict - It automatically creates keys that are accessed later on."""
d = defaultdict(set) # checkout defaultdict(list)
d['num'].add(10)
d['num'].add(20)
d['num'].add(30)
d['alpha'] = 'a'
print(f'Using defaultdict: {d} \n')

# Using dict
d = {}
d.setdefault('color', []).append('Black')
d.setdefault('color', []).append('White')
d.setdefault('Place', []).append('Italy')
print(f'Using dict: {d} \n')

# Using Ordered Dict - It preserves the order in which the data is inserted
d = OrderedDict()
""" 
Under the hood, it uses Doubly Linked List. 
Its size is twice that of normal dictionary since it uses extra linked list.
"""
d['apple'] = 1; d['orange'] = 2; d['grapes'] = 50
print(f'Ordered Dict: {d} \n')