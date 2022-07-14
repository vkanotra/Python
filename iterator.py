# nums = [7, 5, 2, 0]
#
# it = iter(nums)
#
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# # or
# print(next(it))

# create own iterator for top 10 values

class TopTen:
    def __init__(self, number):
        self.num = 1
        self.target = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.target:
            val = self.num
            self.num = self.num + 1
            return val
        else:
            raise StopIteration


nums = TopTen(20)

for i in nums:
    print(i)