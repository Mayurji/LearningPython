from decimal import Decimal

print(f'Rounding No. to One decimal: {round(1.234, 1)}')
print(f'Rounding No. to Two decimal: {round(1.256, 2)}')

print(f'Rounding No. at Once: {round(123.4, -1)}')
print(f'Rounding No. at tens : {round(123.4, -2)}')

# Don't confuse, round vs formatting the decimal

x = 1.244342
print(f'Formatting to two Decimal: {format(x,"0.2f")}')
print(f'Rounding to two Decimal: {round(x, 2)}')

# False - Small mathematical error
a, b = 4.2, 2.1
c = 6.3
print(f'C equals a + b?: {c == (a+b)}')

# Works Well
a, b = Decimal('4.2'), Decimal('2.1')
c = Decimal('6.3')
print(f'C equals a + b?: {c == (a+b)}')
