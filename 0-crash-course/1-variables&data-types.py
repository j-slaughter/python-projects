"""
This is a multi-line comment.
Weclome to learning Python!

"""
# Print to console
print("Hello World!")

# Strings
name = "John"
# Integer (Whole numbers)
age = 25
# Float (Decimal number)
height = 9.5
# Boolean
is_programmer = True

# String Concatenation
print("Hello, my name is " + name)
print("Hello, my name is", name)

# String indexing
print(name[0])  # J
print(name[-1])  # n

# String methods
message = "hello World"
print(message.upper())  # HELLO WORLD
print(message.lower())  # hello world
print(message.capitalize())  # Hello world
print(message.replace("l", "L"))  # heLLo WorLd
print(len(message))  # 11

# Python is a case-sensitive language, so "hello" and "Hello" are different strings
print("World" in message)  # True
print("world" in message)  # False

greeting1 = "Hello"
greeting2 = "hello"

if greeting1 == greeting2:
    print("They are the same")
else:
    print("They are different")  # This will print

# Type conversion
age_str = "30"
age_num = int(age_str)
print(type(age_str))  # <class 'str'>
print(type(age_num))  # <class 'int'>

price_float = 29.99
price_int = int(price_float)
print(type(price_float))  # <class 'float'>
print(type(price_int))  # <class 'int'>
