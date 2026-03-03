"""
Concat

np.concatentate((arr1,arr2),axis=0)

axis 0 => verical stacking
axis 1 => horizontal stacking

"""

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_arr = np.concatenate((arr1,arr2))
print(new_arr)

arr1 = np.array([
    [1,2],
    [3,4]
])
arr2 = np.array([
    [5,6],
    [7,8]
])

new_arr = np.concatenate((arr1,arr2),axis=0) # Row wise concate
print(new_arr)

new_arr = np.concatenate((arr1,arr2),axis=1) # Column wise concate
print(new_arr)

arr3=np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
])
arr4=np.array([
    [
        [10,20,30],
        [40,50,60]
    ],
    [
        [70,80,90],
        [100,110,120]
    ]
])

new_arr = np.concatenate((arr3,arr4),axis=0) # Concate with end
print(new_arr)

new_arr = np.concatenate((arr3,arr4),axis=1) # Concate with rows
print(new_arr)

new_arr = np.concatenate((arr3,arr4),axis=2) # Concate with column
print(new_arr)


