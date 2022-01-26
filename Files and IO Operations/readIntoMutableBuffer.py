import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

with open('sample.bin', 'wb') as f:
    f.write(b'hello world')

buf = read_into_buffer('sample.bin')
print(f'Reading buffer: {buf}')

buf[0:5] = b'Hallo'
print(f'Overwritten buffer: {buf}')
