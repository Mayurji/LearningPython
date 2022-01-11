from itertools import chain, groupby
from operator import itemgetter
from collections import ChainMap
"""
Python Best Practices - groupby

Groupby Operation - It groups or examines 
only consecutive items, hence its important
to sort the attribute.
"""
rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}]

#Sort rows by date
rows.sort(key=itemgetter('date'))

#Groupby Operation
for date, items in groupby(rows, key=itemgetter('date')):
    print(f'Date: {date}')
    for i in items:
        print(' ', i)

# Combine multiple dictionary using ChainMap
# If there are duplicate keys, the value from
# from first mapping is used.
one = {'address': '1060 W ADDISON', 'date': '07/02/2012'}
two = {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
three = ChainMap(one, two)
print(f'Combined Dicts: {three}')

# First mapping takes precedence over other mappings.
a = {'x':1, 'y':2}; b = {'y':1, 'z':2}
c = ChainMap(a, b)
print(f'C Keys: {c.keys()}')
print(f'C Values: {c.values()}')

# Mutation on C works on first mapping
del c['x'] # gets deleted
c['w'] = 0
"""
del c['z'] # throws error, since it z is not present in first mapping
print(f'Updated C: {c.keys()}')
"""

#In chainmap, Change in original dict reflects in merged dict
a['y'] = 8
print(f'C Values: {c}')

# Playing with chainmap
values = ChainMap()
values['x'] = 1
values = values.new_child() # Adds new mapping
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(f'Values: {values}')

values = values.parents # Removes Latest mapping
print(f'Values: {values}')

