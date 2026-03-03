# Aggregation Function : Usen to summarize the data

# In numpy there are some aggregation functions 


import numpy as np

arr=np.array([10,20,30,40,50])

print(sum(arr)) # This is python inbuilt function
print(np.sum(arr)) # This is numpy function
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr)) # For standard deviation
print(np.var(arr)) # For variance 

arr=np.array([
    [1,2,3],
    [4,5,6]
])

# axis = 0  means vertical
# axis =   means horizontal

print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))

arr = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))
print(np.sum(arr,axis=2))