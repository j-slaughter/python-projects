# Vowel Counter: returns number of vowels in a string

print("🔤 VOWEL COUNTER 🔤")

# Vowel list
vowels = ["a", "e", "i", "o", "u"]

while True:
    # Get input from user
    text = input("\nEnter some text (or 'quit'): ").lower()

    # Check for exiting app
    if text == "quit":
        break
    else:
        # Count number of vowels in text
        vowel_count = 0
        for letter in text:
            if letter in vowels:
                vowel_count += 1
        print(f"That text has {vowel_count} vowels!")

# ALTERNATIVE SOLUTION FOR COUNTING

# vowel_count = sum(1 for char in text.lower() if char in "aeiou")
