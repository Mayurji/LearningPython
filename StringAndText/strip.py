
string = " This is an unknown text      \n"
print(f'Left Strip: {string.lstrip()}')
print(f'Right Strip: {string.rstrip()}')

messedUpString = "--------Garbage======"
print(f'Left Strip: {messedUpString.lstrip("-")}')
print(f'Right Strip: {messedUpString.rstrip("=")}')
print(f'Strip: {messedUpString.strip("-=")}')