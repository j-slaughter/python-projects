"""
Lists are collections of items that can
store different types of data
"""
numbers = [1, 2, 3, 4, 5]
# Indexing
print(numbers[0])  # 1
numbers[1] = 22
# Add to end of list
numbers.append(55)
# Remove item from list
numbers.remove(3)
print(numbers)  # [1, 22, 4, 5, 55]
# Get length of list
print(len(numbers))  # 5
# Slicing lists
print(numbers[1:4])  # [22, 4, 5] Elements from index 1 to 3
print(numbers[::2])  # [1, 4, 55] Every other element
print(numbers[::-1])  # [55, 5, 4, 22, 1] Reverse the list
# Concatenate lists
print(numbers + [6, 7, 8])  # [1, 22, 4, 5, 55, 6, 7, 8]
# Repeat the list
print(numbers * 2)  # [1, 22, 4, 5, 55, 1, 22, 4, 5, 55]

"""
Dictionaries are collections that store data
as key-value pairs.
"""
student = {
    "name": "Jane",
    "age": 22,
    "courses": ["Math", "Computer Science"]
}
# Accessing values by key
print(student["name"])  # Jane
# Add to dictionary
student["grade"] = "A"
# Update value
student["age"] += 10
print(student)
# Get list of dictionary keys
print(student.keys())  # dict_keys(['name', 'age', 'courses', 'grade'])
# Get list of dictionary values
# dict_values(['Jane', 32, ['Math', 'Computer Science'], 'A'])
print(student.values())
# Get list of dictionary key-values
print(student.items())  # dict_items([('name', 'Emma'), ('age', 32), ...])

# Loop through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

"""
Sets are unordered collections of unique items. 
No duplicates allowed
"""
unique_colors = {"red", "blue", "green", "green"}
print(unique_colors)  # {'red', 'green', 'blue'}

"""
Tuples are ordered collections that cannot be 
changed after creation.
"""
coordinates = (10.5, 20.8)
