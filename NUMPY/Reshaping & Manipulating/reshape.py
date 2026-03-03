# Reshaping :- Changing dimension without modifying

# 1D --- 2D
# 2D --- 3D

# reshape(rows,column) specify new shape
# If dimension match

# Reshaping does not create copy
# It returns a view it affect array

import numpy as np

arr= np.array([10,20,30,40,50,60])

arr2=arr.reshape(2,3)

print(arr2)
print(arr)

arr3=np.array([10,20,30,40,50,60,70,80])

arr4=arr3.reshape(2,2,2)
print(arr4)

