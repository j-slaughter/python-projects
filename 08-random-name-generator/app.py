# Random Name Generator: Generates a random name.
import random

print("✨ FANTASY NAME GENERATOR ✨")

first_names = [
    "Sky",
    "Star",
    "Moon",
    "Sun",
    "Fire",
    "Ice",
    "Earth",
    "Ocean",
]

last_names = [
    "rider",
    "walker",
    "hunter",
    "seeker",
    "dancer",
    "keeper",
    "singer",
    "bringer",
]

# Get number of names to be generated
count = int(input("How many names do you want? "))

# Generate names
# Convention is to use '_' if not using the variable, otherwise typically 'i'
for _ in range(count):
    first = random.choice(first_names)
    last = random.choice(last_names)
    print(f"{first}{last}")
