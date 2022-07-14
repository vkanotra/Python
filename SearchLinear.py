pos = -1      # position not found yet so -1


# def search(values, to_find):
#     for iteration, i in enumerate(values):
#         if i == to_find:
#             globals()['pos'] = iteration
#             return True

def search(values, to_find):
    iteration_no = 0
    for i in values:
        if i == to_find:
            globals()['pos'] = iteration_no
            return True
        iteration_no += 1


nums = [2, 3, 1, 8, 4, 9, 5]
n = 9

if search(nums, n):
    print("Found at index ", pos)
else:
    print("Not Found")
