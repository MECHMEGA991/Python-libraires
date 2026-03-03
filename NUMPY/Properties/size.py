import numpy as np

# Total no. of elements in an array

arr = np.array([
    [1,2,3],
    [4,5,6]
    ])

print(arr)

# For size use size keyword

print(arr.size)

# if row and column provide simply multiply that

arr3_d =np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
])

print(arr3_d.size)