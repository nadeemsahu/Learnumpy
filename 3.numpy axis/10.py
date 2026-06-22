import numpy as np
import sys

py_ar = [0,4,55,2]

np_ar = np.array(py_ar)

print(sys.getsizeof(1) * len(py_ar))

print(np_ar.itemsize * np_ar.size)