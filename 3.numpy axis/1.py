#axis0 is rows and axis 1 are coloumns

import numpy as np
x=[[1,2,3],[4,5,6],[7,1,0]]
arr=np.array(x)
print(x)

print(arr.sum(axis=0))

print(arr.sum(axis=1))