"""
TEXT FORMATTER APP: formats inputted text to user's 
specification.
"""

print("TEXT FORMATTER")
# Get text from user
text = input("Enter some text: ")
# Text format options
print("1. UPPERCASE")
print("2. lowercase")
print("3. Title Case")
print("4. Sentence case")
# Get format from user
format = input("Choose a format (1-4): ")

if format == "1":
    print(text.upper())
elif format == "2":
    print(text.lower())
elif format == "3":
    print(text.title())
elif format == "4":
    print(text.capitalize())
else:
    print("You did not choose a valid format!")
