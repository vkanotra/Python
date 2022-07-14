from array import *
from math import *

arr = array('i', [0, 1, 2, 3, 4])
floor = floor(len(arr) / 2)
l = len(arr)

for i in range(floor):
    x = arr[i]
    arr[i] = arr[l-i-1]
    arr[l-i-1] = x

print(arr)