import numpy as np

arr=np.array([1,2,3,4,5])
arr2=np.array([1.9,2.3,3.5,4])
arr3=np.array(['hellow','boy','cat'])
# arr4=np.array(['h','b','c',100]) # It shows <U21
arr4=np.array(['h','b','c',100],dtype=object) # It shows object

print(arr)
print(arr2)
print(arr3)
print(arr4)

# For data type us dtype

print(arr.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)

# If you mix types → NumPy converts everything to the most flexible type.