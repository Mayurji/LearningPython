from fnmatch import fnmatch, fnmatchcase

#Matching String using Wildcard Pattern
print(f"Matching Using Wildcard: {fnmatch('foo.txt', '*.txt')}")

print(f"Matching Using Wildcard: {fnmatch('foo.txt', '?oo.txt')}")

print(f"Matching Using Wildcard: {fnmatch('DAT45.txt', 'DAT[0-9]*')}")

filenames = ["foo.py", "foo.js", "text_1.py", "text_2.py"]
print([name for name in filenames if fnmatch(name, 'text_*')])

addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]
# Address Match
print([address for address in addresses if fnmatchcase(address, '* ST')])
print([address for address in addresses if fnmatchcase(address, '54[0-9][0-9] *CLARK*')])

# String Search
file = "Cable Issue"
print(f"First Index of the word: {file.find('Issue')}")