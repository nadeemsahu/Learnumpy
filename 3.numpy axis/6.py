import numpy as np
x=[[1,2,3],[4,5,6],[7,1,0]]
arr=np.array(x)
print(arr)

print(arr.argmax())
print(arr.argmin())

print(arr.argmax(axis=0))
print(arr.argmax(axis=1))

print(arr.argsort(axis=0))
print(arr.argsort(axis=1))