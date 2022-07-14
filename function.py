
def new(a):
    print(a)
    even = 0
    for i in a:
        if i % 2 == 0:
            even += 1
    odd = len(a) - even
    return even, odd


ev, od = new([1, 23, 213, 6, 7, 8, 9])

print("Even numbers: {} and odd number: {}".format(ev, od))
