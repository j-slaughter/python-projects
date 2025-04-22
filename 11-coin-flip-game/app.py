# Coin Flip App: digital coin flip
import random

print("=== 🎮 COIN FLIP GAME 🎮 ===")
print("✨ Guess heads or tails! ✨")

while True:
    # Get user's guess
    guess = input("\nEnter your guess (heads/tails): ").lower()
    # Check for vaild input
    if guess != "heads" and guess != "tails":
        print("❌ Please enter 'heads' or 'tails' ❌")
        # Go back to start of loop
        continue
    # Get random toss
    toss = random.choice(["heads", "tails"])
    print(f"\n🪙 The coin shows: {toss}")

    if guess == toss:
        print("You guessed correctly! You win! 🎉")
    else:
        print("Sorry, wrong guess. Try again!")

    # Ask if user wants to play again
    continue_game = input("\n🔄 Play again? (yes/no): ").lower()
    if continue_game.startswith("n"):
        print("Thanks for playing!")
        break
