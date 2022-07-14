# find min number in each iteration

def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        (nums[i], nums[minpos]) = (nums[minpos], nums[i])


nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)