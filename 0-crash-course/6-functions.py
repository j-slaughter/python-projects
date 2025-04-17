# Functions in python

def greet_everyone():
    print("Hello everyone!")


greet_everyone()


def greet_user(name):
    print("Hello,", name)
    print("Welcome to our app!")


greet_user("John")


def power(base, exponent):
    return base**exponent


x = power(2, 5)
print("x:", x)  # 32
y = power(8, 2)
print("y:", y)  # 64
