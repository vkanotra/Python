# Read
f = open('MyData', 'r')                 # r is the read mode

# print(f.read())    to read whole file
# print(f.__next__())  # to iterate
# print(f.readline(), end='')    # first line
# print(f.readline())    # second line
print(f.readlines())
f.close()

# Write
# f1 = open('abc', 'w')           # if no abc found, it will create one
# f1.write('Hi')
# f1.write('Hello')
# f1.writelines(['Hi\n', 'My name is vaibhav\n', 'bye'])

# Append - if the file already has something, and need to append more
# f1 = open('abc', 'a')
# f1.write('\nLaptop')

# Move all data from MyData to abc
f = open('MyData', 'r')
f1 = open('abc', 'w')

# for i in f:
#     newLine = i
#     f1.write(newLine)

# OR

fData = f.readlines()       # gives an array of lines ['Hi\n', 'My name is vaibhav\n', 'bye\n', 'asd']
f1.writelines(fData)

# Binary files
# f2 = open('Img_2.jpg', 'rb')   rb is read binary

