import os

path = '/home/mayur/Documents/Learning-Python/LearningPython/Files and IO Operations/text.txt'

print(f'Basename of the path: {os.path.basename(path)}')

print(f'Directory name of the path: {os.path.dirname(path)}')

# Join path components together
print(os.path.join('tmp', 'data', os.path.basename(path)))

path = '~/Files and IO Operations/text.txt'
print(f'Expanding to user directory: {os.path.expanduser(path)}')

# Check if its a regular file
print(f"Regular File? {os.path.isfile('text.txt')}")

# Check if its a regular directory
print(f"Regular Directory? {os.path.isdir(os.path.dirname(path))}")

# Check if there is a symlink
print(f'Symlink? {os.path.islink(path)}')

# Get size file and time
import time
print(f'Size: {os.path.getsize("text.txt")}')
print(f'Time: {time.ctime(os.path.getmtime("text.txt"))}')
