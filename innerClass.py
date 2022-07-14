class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap1 = self.Laptop("hp", 16)     # Object of inner class in outer class
        self.lap2 = self.Laptop("dell", 32)

    def show_info(self):
        print(self.name, self.roll)
        self.lap1.show_info()

    class Laptop:                       # Inner Class

        def __init__(self, brand, ram):
            self.brand = brand
            self.ram = ram

        def show_info(self):
            print(self.brand, self.ram)


s1 = Student("Vaibhav", 45)
s2 = Student("Navin", 12)
s2.show_info()

# s1lap = Student.Laptop("hp", 12)                # Object of inner class, outside classes

