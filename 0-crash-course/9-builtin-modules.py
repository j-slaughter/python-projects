import random
import math
import datetime
import os
import sys
import time

# Random number module
# Returns random number between 1 and 10 inclusive
random_number = random.randint(1, 10)
print(f"Random number is {random_number}")
# Choose a random element from a list
fruits = ["apple", "orange", "cherry", "banana"]
random_fruit = random.choice(fruits)
print(f"Random fruit is {random_fruit}")
# Shuffle the list
random.shuffle(fruits)
print(f"Shuffled list: {fruits}")

# Math module
print(f"Square root of 16: {math.sqrt(16)}")  # 4.0
print(f"Pi: {math.pi}")  # 3.14159...
print(f"Ceiling of 4.3: {math.ceil(4.3)}")  # 5
print(f"Floor of 4.8: {math.floor(4.8)}")  # 4
print(f"5 raised to power of 3: {math.pow(5, 3)}")  # 125.0

# Datetime module
current_time = datetime.datetime.now()
print(f"Current date and time: {current_time}")  # 2025-04-16 10:39:07
print(f"Today's date: {datetime.date.today()}")  # 2025-04-16
print(f"Current year: {datetime.date.today().year}")  # 2025

# OS module
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")
print(f"List of files: {os.listdir('.')}")

# Sys module
print(f"Python version: {sys.version}")  # Python version: 3.13.2
print(f"Platform: {sys.platform}")  # e.g. 'win32, 'darwin', 'linux'

# Time module
print("Waiting for 2 seconds...")
time.sleep(2)
print("Done!")
