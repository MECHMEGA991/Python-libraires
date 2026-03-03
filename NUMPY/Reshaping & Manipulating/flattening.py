# Flattening array :- conversion of multidimensional array to 1d array

# .ravel() -> view =>  It makes a view of arr and can affect original array
# .flatten() -> copy => It makes a copy of arr and cant affect to original

import numpy as np

arr_2d =np.array([
    [1,2,3],
    [4,5,6]
])

# arr = arr_2d.ravel()

# arr[2]=0
# print(arr)

# print(arr_2d)  # As you can see it affcts the original array

arr=arr_2d.flatten()
arr[2]=0

print(arr)  # As you can see it doesnt affects the original array

print(arr_2d)



