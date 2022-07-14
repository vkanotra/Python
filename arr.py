from array import *

arr = array('i', [])
length = int(input('Enter the length of the Array: '))

for i in range(length):
    nums = int(input('Enter number ' + str(i) + ': '))
    arr.append(nums)

print(arr)

ser = int(input('Enter a value to search: '))

k=0
for e in arr:

    if e == ser:
        print(k)
        break
    k += 1
else:
    print('Not Found')


print(arr.index(ser))
