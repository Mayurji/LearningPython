import numpy as np

a = np.matrix([ [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

#Transpose 
print(f'Transpose Of a Matrix: {a.T}')

#Matrix Inverse
print(f'Inverse Of a Matrix: {a.I}')

#Vector
v = np.matrix([[1], [2], [3]])

#Multiply Vector With Matrix
print(a * v)