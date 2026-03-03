# Append => It will add an element at the end of arrays
# It returns a new copy 

import numpy as np

arr=np.array([1,2,3,4,5])

new_arr =np.append(arr,[40,50,60])
print(new_arr)

# For 2d arrays 
# CASE 1 => if axis=None it flattens the 2D array
# CASE 2 => if axis=0 append the last row but no. of elements must equal to the no. of element append 
# CASE 3 => if axis=1 append the last column but no. of elements of column must equal to no. of element append
arr2=np.array([
    [1,2,3],
    [4,5,6]
])

new_arr2 = np.append(arr2,[[10,20,30]],axis=0)
print(new_arr2)

# for 3d arrays

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

#For 3d arrays 
# CASE 1 => if axis=0 it add the the new matrix at the end of array
# CASE 2 => if axis=1 append the last row but no. of elements must equal to the no. of element append 
# CASE 3 => if axis=1 append the last column but no. of elements of column must equal to no. of element append


# new_arr3 = np.append(arr3,[[[1,2,3],[4,5,6]]],axis=0)

new_rows = [
    [[13,14,15]],   # for matrix 0
    [[16,17,18]]    # for matrix 1
]

new_arr3 = np.append(arr3,new_rows,axis=1)



print(new_arr3)

