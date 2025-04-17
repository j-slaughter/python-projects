# For loop

print("Counting from 1 to 5:")
# range (inclusive, exclusive)
for i in range(1, 6):
    print(i)

print("\nReversed counting from 5 to 1:")
for i in range(5, 0, -1):
    print(i)

# While loop
count = 1
print("Using while loop:")
while count <= 5:
    print(count)
    count += 1

# Reversed while loop
count = 5
print("\nReversed while loop:")
while count > 0:
    print(count)
    count -= 1

# Looping through a list
fruits = ["apple", "banana", "cherry"]
print("My fruits:")
for fruit in fruits:
    print(fruit)

# Reverse looping through a list
print("\nMy fruits in reverse:")
for fruit in reversed(fruits):
    print(fruit)

# Loop with enumerate
print("fruit with indicies:")
for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")

# Looping through a dictionary
person = {"name": "John", "age": 30, "city": "New York City"}
print("\nLooping in a dict:")
for key, value in person.items():
    print(f"{key}:{value}")

# List comprehension (compact loop for creating lists)
squares = [x**2 for x in range(1, 6)]
print("\nSquares from 1 to 5", squares)  # [1, 4, 9, 16, 25]

# For loop with zip() - iterate through multiple lists in parallel
items = ["vase", "dish", "towel"]
colors = ["red", "yellow", "green"]
print("\nItems and their colors:")
for item, color in zip(items, colors):
    print(f"{item} is {color}")

# Break and continue
print("\nLoop with a break:")
for i in range(1, 10):
    if i > 5:
        break
    print(i)

print("Loop with continue:")
for i in range(1, 10):
    if i % 2 == 0:
        continue  # skips even numbers
    print(i)

# Infinite loops with break condition
i = 1
print("\nControlled infinite loop:")
while True:
    print(i)
    i += 1
    if i > 5:
        break
