# Boolean Masking -> filtering data based on condition

import numpy as np

arr=np.array([10,20,30,49,50])

print(arr[arr>25])
print(arr[arr%2==0])
