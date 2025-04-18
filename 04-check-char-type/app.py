"""
Check Char Type App: checks if a charater is a 
letter, number, or special character
"""

print("📝 CHARACTER TYPE CHECKER 📝")
# Get character from user
char = input("Enter a single character: ")
# Return character type
if char.isalpha():
    print("This is a letter.")
elif char.isdigit():
    print("This is a digit.")
else:
    print("This is a special character.")
