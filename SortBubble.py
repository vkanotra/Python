def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                (nums[j], nums[j+1]) = (nums[j+1], nums[j])
                # swap by checking 2 numbers one by one in groups of 2


nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)
