# for slicing an array we pass 
# start stop step
# Slicing do view window into original

import numpy as np

arr=np.array([1,2,3,4,5])

print(arr[1:5:1])

#Reverse 

print(arr[::-1])

# for 2D array

arr2=np.array([
    [1,2,3],
    [4,5,6]
])

# arr[row_start:row_end, col_start:col_end]

# First row
print(arr2[0,0:3])

# last two column
print(arr2[0:,1:])

# Middle column
print(arr2[0:,1:2])

# Slicing in 3d arrays

import numpy as np

arr3 = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])

# arr[matrix_slice, row_slice, column_slice]

# axix=0 :-> matrices (outermost)
# axix=1 :-> rows (middle)
# axix=2 :-> columns (innermost)

# matrix 1
print(arr3[0,:,:])

#matrix 2
print(arr3[1,:,:])


print(arr3[0,:,1:2])

