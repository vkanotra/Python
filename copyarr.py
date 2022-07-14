from numpy import *

arr = array([4, 12, 43, 5])

arr2 = arr.copy()

arr[1] = 13
print(arr)
print(arr2)
print(max(arr2))

