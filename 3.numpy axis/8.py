import numpy as np
x=[[1,2,3],[4,5,6],[7,1,0]]
arr=np.array(x)
print(np.where(arr>5))
#returns array([rows]) first and next array([columns])