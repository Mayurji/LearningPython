import unicodedata

# Unicode Characters
s1 = 'Spicy Jalape\u00f1o' #Fully composed ñ
s2 = 'Spicy Jalapen\u0303o' #Combined n and ~

print(f'Same String? {s1==s2}')
print('len of s1: {} and s2: {}'.format(len(s1), len(s2)))

#NFC - Fully Composed or We can use NFD - Fully Decomposed
t3, t4 = unicodedata.normalize('NFC', s1), unicodedata.normalize('NFC', s2)
print(f'Same String? {t3==t4}')
print('len of t3: {} and t4: {}'.format(len(t3), len(t4)))

#Check if a character is combined character
t1  = unicodedata.normalize('NFD', s1)
print(f"Combining Character? {''.join(c for c in t1 if not unicodedata.combining(c))}")
