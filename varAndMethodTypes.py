class Car:
    wheels = 4       # Static or class variable

    def __init__(self, model, color):
        self.model = model               # Instance Variables
        self.color = color
        # print("hello init")

    def show(self):                      # Instance methods - Accessors (get) and Mutators (set)
        print(f"Model is {self.model} and color is {self.color}")

    def get_model(self):
        return self.model

    def set_model(self, value):
        self.model = value

    @classmethod
    def show_wheels(cls):                # Class methods
        return cls.wheels

    @staticmethod                        # Static method  - no class or instance veriables used
    def info():
        print("price of car is 17L")
        # return 56


audi = Car("audi a4", "blue")
ferrari = Car("ferrari 488", "green")

audi.show()
ferrari.show()

print(Car.show_wheels())
Car.info()

