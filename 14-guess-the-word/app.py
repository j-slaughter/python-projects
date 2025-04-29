"""
Guess the Word App: Player's are given a scrambled word 
that they have to guess the unscrambled version.
"""
import random

print("\n=== 🔤 GUESS THE WORD! 🔤 ===")
print("✨ Unscramble the letters to find the word! ✨")

words = ["python", "coding", "game", "computer", "fun", "learn", "word"]

while True:
    # Get a random word
    unscrambled = random.choice(words)
    letters = list(unscrambled)
    random.shuffle(letters)
    scrambled = "".join(letters)

    print(f"\nScrambled word: {scrambled}")
    # Get user's guess
    guess = input("🤔 What's the word? ").lower()

    # Check the guess
    if guess == unscrambled:
        print("🎉 Correct! You win!")
    else:
        print(f"Sorry, the word was: {unscrambled}")

    # Check if user wants to continue
    if not input("\nPlay again? (yes/no): ").lower().startswith("y"):
        print("Thanks for playing! 👋")
        break
