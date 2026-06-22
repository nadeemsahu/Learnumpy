import numpy as np
x=[[1,2,3],[4,5,6],[7,1,0]]
arr=np.array(x)
print(np.count_nonzero(arr))
print(np.nonzero(arr))