from sys import argv

# Read a file
script, filename = argv
text = open(filename)
print(text.read())

# Empty the file
target = open(filename, 'w')
target.truncate()

# Check if file is empty?
text = open(filename)
print(f'File is empty: {text.read()}')

text = "This is a dummy file.\nIt is read by python."

# Write to file
target.write(text)
target.close()

# Check if text is written in file.
text = open(filename)
print(f'File is not empty: {text.read()}')