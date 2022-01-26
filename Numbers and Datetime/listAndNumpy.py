# Numpy Over List
import LearningPython.numberDateAndTime.PythonNumpy as np

a = [1, 2, 3, 4]

try:
    print(f'Adding Scalar to List?: {a + 10}')
except TypeError:
    print("Cannot add a int with list object")

a = np.array([1, 2, 3, 4])

print(f'Adding Scalar to Numpy array: {a + 10}')

# Multidimensional Array
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Broadcasting
print(f'Broadcasting: {a + [100, 101, 102, 103]}')

# Conditional Assignment
print(f'Conditional Assignement: {np.where(a<10, a, 10)}')
