class Computer:

    def __init__(self, ram, gen):
        self.memory = ram
        self.processor = gen

    def config(self, value):
        print(self.memory + ', ' + self.processor)
        print("{} memory is {} and processor is {}".format(self, self.memory, self.processor))
        print(f"{self} memory is {self.memory} and processor is {self.processor} and value is {value}")
        print("(using percent s) memory is %s and processor is %s" % (self.memory, self.processor))
        # %s for string, %d for decimal or int

    def compare(self, other):
        if self.memory == other.memory:
            return True


com1 = Computer("16gb", "i7")
com2 = Computer("8gb", "i3")

# Computer.config(com1)
com1.config(5)
com2.config(8)

# same as
a = 5   # 5 is int in-built class
a.bit_count()

# if com1.memory == com2.memory:
#     print("They are same")
# else:
#     print("not same")

if com1.compare(com2):
    print("They are same")
else:
    print("not same")