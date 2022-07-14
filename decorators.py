# decorators can enhance or add features to an already built function
# e.g. divide 2 numbers and take bigger parameter in denominator
import filter
def divide(a, b):
    print(a/b)


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a             # swap
        return func(a, b)
    return inner


divide = smart_div(divide)
divide(2, 4)


# another example
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)

print("decorators: " + __name__)