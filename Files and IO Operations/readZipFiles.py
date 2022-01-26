import gzip
import bz2
from functools import partial

text = "This is a gzip file"
with gzip.open('somefile1.gz', 'wt', compresslevel=9) as f:
    f.write(text)

text = "This is a bz2 file"
with bz2.open('somefile.bz2', 'wt', compresslevel=5) as f:
    f.write(text)

# Reading Chunk of a file
RECORD_SIZE = 32
with open('text.txt', 'rt') as f:
    records = iter(partial(f.read, RECORD_SIZE), '')
    for i, r in enumerate(records):
        print(f'Chunks {i}: {r}\n')