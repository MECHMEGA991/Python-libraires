"""
Delete 
It returns a new array so old array will be unchanged

np.delete(array,index,axis)

For 2D and 3D array we cant delete a particular elemenmt if we delete we have to flatten first but afterwards it difficult to reshape it
so deleting whole row and column works 

"""

import numpy as np

# arr=np.array([1,2,3,4])

# new_arr=np.delete(arr,2)
# print(new_arr)

# # For 2D array

# arr_2d =np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# new_arr=np.delete(arr_2d,1,axis=0)
# print(new_arr)

# Deleting more than two rows and column by passing [0,1]
# np.delete(arr_2d,[0,1],axis=0)

arr3 = np.array([
    [[1,2],
     [3,4]],

    [[5,6],
     [7,8]]
])

# new_arr=np.delete(arr3,0,axis=0) # It will delete the entire matrix
# print(new_arr)
# new_arr=np.delete(arr3,0,axis=1) # It will delete the 0 rows from all the matrix
# print(new_arr)
new_arr=np.delete(arr3,0,axis=2) # It will delete the entire matrix
print(new_arr)