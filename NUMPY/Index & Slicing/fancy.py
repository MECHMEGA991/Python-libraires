import numpy as np

arr1=np.array([10,20,30,40])

print(arr1[[0,2,3]])


arr=np.array([
    [1,2,3],
    [4,5,6]
])

# Fancy Indexing => selecting multiple elements at once

# Pick elements at positions (0,1) and (1,2)
rows = [0, 1]
cols = [1, 2]

print(arr[rows, cols])


