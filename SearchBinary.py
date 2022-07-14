# nums = [1, 3, 7, 9, 14, 19, 25]
#   index 0  1  2  3   4   5   6
#         L        M           U

# In Binary search, list should be sorted in ascending order
# then take the index of lowest value as lower bound(L = 0) and max index as upper bound(U = 6)
# add both index and divide by 2 to get mid index (int not decimals), (0+6)/2 = 3
# now check if value at mid index == our to_find value, if yes then return it
# otherwise, check if to_find value is greater than the value at mid or lower than the mid value
# if to_find is greater, then L will become as M else if lower then U will become as M
# repeat

pos = -1      # position not found yet so -1


def search(values, to_find):
    l = 0
    u = len(values) - 1

    while l <= u:
        mid = (l+u) // 2     # // gives int value on divide
        if values[mid] == to_find:
            globals()['pos'] = mid
            return True
        else:
            if to_find > values[mid]:
                l = mid + 1           # +1 to skip the mid value we already checked
            else:
                u = mid - 1           # -1 to skip the mid value we already checked
    return False


nums = [1, 3, 7, 9, 14, 19, 25]
nums.sort()
n = 25

if search(nums, n):
    print("Found at index ", pos)
else:
    print("Not Found")





