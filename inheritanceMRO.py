# MRO -Method Resolution order - inheritance goes from left to right (A, B, C) -
# first A, then B, then C for constructors

class A:
    def __init__(self):
        print("In class A init")

    def feature1(self):
        print("feature1 in A")

    def feature2(self):
        print("feature2")


class B:
    def __init__(self):
        print("In class B init")
        # If obj of B is created and B inherits from A, it will first try init of B,
        # if not available then it will go for super class init

    def feature1(self):
        print("feature1 in B")

    def feature4(self):
        print("feature4")

    def feature6(self):
        print("---------------")


class C(A, B):
    def __init__(self):                          # Here it will first try init of C, if not then A, if not then B
        super().__init__()                       # same for this, first A then C
        print("In class C init")

    def feature5(self):
        print("feature5")

    def feature6(self):
        print("******************")
        print()
        super().feature2()
        super().feature4()


obj = C()
obj.feature1()  # it will call feature1 from A class because of MOR
obj.feature6()  # it will call feature6 from class 6 - METHOD OVERRIDE
