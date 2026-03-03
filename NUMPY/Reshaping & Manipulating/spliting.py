"""
np.split() => Equal part

np.hsplit() => horizontally split requires at least 2d array column wise 

np.vsplit() => vertically split requires at least 2d array row wise 

"""
import numpy as np

arr1=np.array([1,2,3,4,5,6])

# print(np.split(arr1,2))

arr2=np.array([
    [1,2,3],
    [4,5,6]
])

# print(np.vsplit(arr2,2)) # works alog axis=0
# print(np.hsplit(arr2,3)) # works alog axis=1

# For a specific row index
# When you give [1,2], it means:

# Split before column index 1
# Split before column index 2
# After last index (2) → third part → column 2

# Here: len([1,2]) = 2

# So result → 3 parts

print(np.hsplit(arr2,[1,2]))

