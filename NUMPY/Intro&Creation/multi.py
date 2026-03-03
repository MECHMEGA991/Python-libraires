# Multi-Dimensional Array

# A multi-dimensional array is an array that contains other arrays as its elements. Essentially, it’s like a grid or table of values rather than a simple list.

# 3D array
# Multiple 2D table stacked together

# 3D array with 2 layers, 2 rows, 3 columns


import numpy as np

arr = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],

    [
        [7,8,9],
        [10,11,12]
    ]

])

print(arr)

# array3D[layer][row][column]

print(arr[0,1,0])