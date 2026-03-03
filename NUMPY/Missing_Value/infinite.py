# np.isinf(arr) 10**1000000
# 1/0 

import numpy as np

arr = np.array([1,2,np.inf,4,-np.inf,6])

print(np.isinf(arr))

# To replace
# Two type of Infinite postive and negative
print(np.nan_to_num(arr,posinf=100,neginf=100))