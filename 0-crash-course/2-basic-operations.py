import math

x = 10
y = 5

# Addition
print(x+y)  # 15
# Subtraction
print(x-y)  # 5
# Multiplication
print(x*y)  # 50
# Division
print(x/y)  # 2.0
# Modulo (Remainder)
print(x % y)  # 0
# Exponentiation
print(x**y)  # 100000

# x = x + 15
x += 15
print(x)  # 25

# math module operations (use import math statement at top of file)
print(math.pi)  # 3.1415926...
print(math.sqrt(16))  # 4.0
print(math.floor(4.7))  # 4
print(math.ceil(5.3))  # 6
print(math.pow(2, 3))  # 8.0

# Round
print(round(math.pi, 2))  # 3.14

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# f Strings
print(f"Hello, my name is {full_name}")

# integer floor division
a = 17
b = 5
print(a / b)  # 3.4
print(a // b)  # 3

# Multiple variable assignments
i, j, k = 1, 2, 3
print(i, j, k)  # 1 2 3

# Swap values
m = 10
n = 20
m, n = n, m
print(m, n)  # 20 10

# Comparison operators
c = 5
d = 10
print(c == d)  # False
print(c != d)  # True
print(c > d)  # False
print(c < d)  # True
print(c >= d)  # False
print(c <= d)  # True

# Logical operators
a = True
b = False
print(a and b)  # False
print(a or b)  # True
print(not b)  # True

# String slicing
text = "Python programming"
print(text[0:6])  # Python
print(text[7:])  # programming

# Reverse string
print(text[::-1])  # gnimmargorp nohtyP

# String formatting with .format()
name = "Alice"
age = 25
msg = "My name is {} and I am {} years old.".format(name, age)
print(msg)  # My name is Alice and I am 25 years old.

# Using placeholders
msg2 = "My name is {0} and I am {1} years old. {0} is a nice name.".format(
    name, age)
print(msg2)  # My name is Alice and I am 25 years old. Alice is a nice name.
