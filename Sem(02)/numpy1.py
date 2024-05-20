# # ynatax
# import numpy as np
# 1> np.array(object,dtype = None, ndmin = 0)S

# task 2 
''' input - 1 2 3 4 5 5 6 
'''

import numpy1 as np
lst = list (map(int,input().split()))
arr = np.array(lst).reshape((3,3))
print(arr)


