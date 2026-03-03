import numpy as np

# To change the datatype of an array we use astype
# In numpy we dont use type insted we use dtype 


arr=np.array([1,2,3,4,5])

print(arr)
print(arr.dtype)

new_arr=arr.astype(float)

print(new_arr.dtype)

# so so by changing the type of arr it creates new arrray insted of changing existing one so perhaps arr are immutable

# 👉 NumPy arrays are mutable, but their size and dtype are fixed after creation.
 

print(arr.dtype)