"""Reading File as Single String"""
with open('text.txt', 'rt') as f:
    data = f.read()

"""Reading File as list of lines"""
with open('text.txt', 'rt') as f:
    for line in f:
        print(f'{line}')

"""Write to File"""
text1 = "Writing to text file."
with open('someTxt.txt', 'wt') as f:
    f.write(text1)

"""Append to Existing File"""
with open('text.txt', 'at') as f:
    f.write("Appending more content to file.")

"""Append to Existing File"""
with open('text.txt', 'at') as f:
    print('Hello World!', file=f)

with open('text.txt', 'rt') as f:
    data = f.read()
    print(data)

with open('somefile', 'xb') as f:
    f.write(b'Hello\n')