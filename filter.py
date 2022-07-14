# FILTER (filter out data using any logic) ->
# MAP (apply any operations to filtered data) ->
# REDUCE (to maybe 1 value, like avg or add all values in a list)

from functools import reduce

# def is_even(n):
#     return n % 2 == 0
#  OR

# f = lambda n : n % 2 == 0

nums = [12, 321, 123, 432, 334, 112, 123, 543, 56, 1232, 34]

evens = list(filter(lambda n: n % 2 == 0, nums))   # evens = list(filter(is_even, nums) or f,nums
print(evens)

# MAP (double all the values from evens)
doubles = list(map(lambda n: n*2, evens))
print(doubles)


# REDUCE
# def add_all(a,b):
#     return a+b


sums = reduce(lambda a, b: a+b, doubles)  # no list because we are expecting only 1 value in return
print(sums)

if __name__ == '__main__':
    print("filter: " + __name__)