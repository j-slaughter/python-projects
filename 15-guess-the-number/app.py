"""
Guess the Number App: A number guessing game where users 
get 10 attempts to guess the number between 1 and 100.
"""
import random

print("🔢 Welcome to the Number Guessing Game! 🔢")
print("🤔 I'm thinking of a number between 1 and 100. You have 10 attempts to guess.\n")

# Initialize game
playing = True
while playing:
    # Get random number
    correct_num = random.randint(1, 100)
    # Initialize attempt count
    count = 0
    game_over = False

    while count < 10 and not game_over:
        # Increment count
        count += 1
        # Get user's guess
        try:
            guess = int(input(f"🎯 Attempt {count}/10. Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        # Check guess
        if guess > correct_num:
            print("Too high! Try a lower number! ⬇️")
        elif guess < correct_num:
            print("Too low! Try a higher number! ⬆️")
        else:
            print(
                f"🎉 Congratulations! You guessed the number {correct_num} in {count} attempts!")
            game_over = True
        # Attempts remaining
        if count < 10 and not game_over:
            print(f"⏳ You have {10 - count} attempts left.")

    # No more attempts. Lost game
    if not game_over:
        print(f"😭 Sorry! The correct number was {correct_num}!")

    # Play again?
    play_again = input("\n🔄 Would you like to play again? (yes/no): ").lower()
    if play_again.startswith("y"):
        print("New game starting...\n")
    else:
        print("Thanks for playing! 👋")
        playing = False
