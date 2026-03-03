"""
np.insert(array,index,value,axix =None)
array - oringinal array
index -
value -
axis = 0 row-wise
axis = 1 column wise


"""

import numpy as np

arr=np.array([10,20,30,40,50,60])

new_arr = np.insert(arr,2,100,axis=None)

print(new_arr)

# Insert in 2d array

arr_2d=np.array([
    [1,2,3],
    [4,5,6]
])

new_arr_2d=np.insert(arr_2d,1,[200,400],axis=1)
# new_arr_2d=np.insert(arr_2d,1,[200,400],axis=None)  # If axis it none it will add in a row 
print(new_arr_2d)

# Insertion at 3d arrays

arr_3d = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

# axis = 0 means to add a new matrices 

matrix = np.array([
    [8,9],
    [10,11]
])

# Isertion a new matrix
new_arr_3d = np.insert(arr_3d,2,matrix,axis=0)
print(new_arr_3d)

# Add new row in each matrix (axis = 1)

new_arr_3d = np.insert(arr_3d,1,[100,200],axis=1)
print(new_arr_3d)

# Add new row in each matrix (axis = 2)

new_arr_3d = np.insert(arr_3d,0,[100,200],axis=2)
print(new_arr_3d)
