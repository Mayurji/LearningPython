import os
import glob
from fnmatch import fnmatch

pyfiles = [name for name in os.listdir('./') if fnmatch(name, '*.py')]
print(f'All py Files in current directory: {pyfiles}')

pyfiles = glob.glob('*.py')
print(f'All py Files in current directory: {pyfiles}')

name_size_date = [(name, os.path.getsize(name), os.path.getatime(name)) for name in pyfiles]
print(name_size_date)