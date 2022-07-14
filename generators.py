def gen(num):
    # for nums in range(1, num + 1):
    #     yield nums

    x = 1
    while x <= num:
        yield x                     # yield doesn't end the loop like return
        x += 1


values = gen(10)
print(values.__next__())

for i in values:
    print(i)
