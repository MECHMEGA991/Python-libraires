# To replace the nan value 
# Default value is 0

import numpy as np

arr= np.array([1,2,np.nan,4,np.nan,6])

print(np.nan_to_num(arr)) # By default value 0

print(np.nan_to_num(arr,nan=100))


