class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __str__(self):                              # override print(s1.__str__())
        return f"{self.m1} {self.m2}"


s1 = Student(43, 58)
s2 = Student(34, 70)

print(int.__add__(21, 22))

s3 = s1 + s2
print(s3.m1, s3.m2)
# this will not work as add does __int__.add(a,b) or for str, but not obj type.
# but we can create our own add method to overload add function

print(s1)  # gives <__main__.Student object at 0x0000024B7B4CBE20>, we can override this method
