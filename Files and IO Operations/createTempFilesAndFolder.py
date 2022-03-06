from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    f.write('this is temp file')
    f.seek(0)
    data = f.read()
    print(data)

# Destroys temp
