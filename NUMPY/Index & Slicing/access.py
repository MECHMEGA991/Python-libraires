import numpy as np

# Indexing : Selecting an element in an array

arr = np.array([1,2,3,4])

print(arr[0]) # First element
print(arr[-2]) # last second

arr=np.array([
    [1,2,3],
    [4,5,6]
    ])
# for 2d arrays arr[row][col]

print(arr[0][1])

arr2=np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
    ])

print(arr2[1][0][2])

# for 3d array arr[layer][row][col]

