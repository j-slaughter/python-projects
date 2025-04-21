# Word Scrambler App: scrambles inputted word
import random

print("🔤 WORD SCRAMBLER 🔤")

while True:
    # Get input from user
    word = input("\nEnter a word to scramble (or 'quit'): ")
    # Scramble word or quit
    if word.lower() == 'quit':
        print("👋 Goodbye!")
        break
    else:
        # Convert input to a list
        letters = list(word)
        # Shuffle the list
        random.shuffle(letters)
        # Join list back into string
        scrambled_word = "".join(letters)
        print(f"Scrambled: {scrambled_word}")
