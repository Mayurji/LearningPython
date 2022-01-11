"""Unpacking In Python - Unpacking is applicable on all python iterables"""

# Unpacking Tuple
p = (4, 5)
a, b = p
print(f'a, b: {a, b}')

# Unpacking Lists
share_details = ['HUL', '10', '2435', (2021, 12, 31)]
name, quantity, price, date = share_details
print(f'Share Name: {name}, Q: {quantity}, Price: {price}, date: {date}')

year, month, day = date
print(f"Year: {year}, Month: {month}")

# Unpacking String
s = 'python'
a, b, c, d, e, f = s
print(f'String Unpacking: {a, b, c, d, e, f}')

# Unpacking Arbitrary Length Iterables using * expression
*string_type, tup = ['HUL', '10', '2435', (2021, 12, 31)]
print(f'String Variables: {string_type}')
print(f'tup Variables: {tup}')

name, *places, animal = ['you', 'Italy', 'France', "Elephant"]
print(f'Name: {name}')
print(f'Places: {places}')
print(f'Animal: {animal}')

# Unpacking and ignore elements not required
*string_type, (*_, day) = ['HUL', '10', '2435', (2021, 12, 31)]
print(f"Ignored Year and Month, only Day: {day}")