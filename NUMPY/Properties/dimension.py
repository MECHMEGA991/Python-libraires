import numpy as np

# For finding dimension of an array use ndim 

arr_1d = np.array([1,2,3,4])
arr2_d = np.array([
    [1,2,3],
    [4,5,6]
])

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

print(arr_1d)
print(arr2_d)
print(arr3_d)

print(arr_1d.ndim)
print(arr2_d.ndim)
print(arr3_d.ndim)

