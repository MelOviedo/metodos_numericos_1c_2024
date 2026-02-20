import numpy as np

A = np.array([[1, 2,3],[3, 4,3],[3, 4,4]])
B = np.array([[5, 6,0], [1,7, 8],[1,7, 8]])

result = np.dot(A, B)
print(result)