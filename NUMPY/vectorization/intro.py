"""
 Concept	        Meaning
 Vectorization	    Doing operations on whole arrays at once
 Broadcasting	    Automatically matching shapes for operations

What is vectorization?

Performing operations on entire arrays at once
instead of using Python loops.

"""

# Witout using numpy 

# zip() is a built-in function that:

# Combines multiple iterables (lists, tuples, etc.) element-wise.

# It pairs elements based on their positions (index).


li=[1,2,3]
li2=[4,5,6]

res=[x+y for x,y in zip(li,li2)]
print(res)

# a = [1, 2, 3]
# b = ['a', 'b', 'c']

# result = zip(a, b)
# print(list(result))

import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

print(arr1+arr2)