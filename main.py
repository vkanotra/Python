import math
from math import sqrt, floor, pi
while True:
    try:
        a = int(input("Enter a: "))
    except ValueError:
        print('Please try with a value eg. 45')
    else:
        print('Value of a is ' + str(a))
        break

b = int(input("Enter b: "))

c = a + b
d = sum([a, b])
print(d)
