from operator import attrgetter, itemgetter

rows = [{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]

# Sorting elements in dictionary based on value
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(f'Sorting Element By fname: {rows_by_fname}\n')

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(f'Sorting Element By uid: {rows_by_uid}\n')

rows_by_lname = sorted(rows, key=itemgetter('lname', 'fname'))
print(f'Sorting Element By lname and fname: {rows_by_lname}\n')

# Sorting element in dictionary using lambda
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
print(f'Sorting Element By fname: {rows_by_fname}\n')

rows_by_lname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
print(f'Sorting Element By lname and fname: {rows_by_lname}\n')

# Min, Max and Itemgetter
row_at_max = max(rows, key=itemgetter('uid'))
print(f'Max Uid: {row_at_max}\n')

