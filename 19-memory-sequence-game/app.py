"""
Memory Sequence Game App: Tests the player's memory by sequentially 
adding numbers for the player to memorize and repeat back to the computer.
"""
import random
import time
import os


def clear_screen():
    """Clears the terminal window"""
    os.system("cls" if os.name == "nt" else "clear")


print("\n=== 🧠 MEMORY SEQUENCE GAME 🧠 ===")
print("✨ Remember the sequence and type it back! ✨")
print("\nRules:")
print("- Watch as numbers appear one by one")
print("- After the sequence is shown, type it back in order")
print("- Each round adds one more number to remember")
print("- How far can you go? 🏆\n")
input("Press Enter to start...")

# Initialize game
sequence = []
current_round = 1
game_over = False

while not game_over:
    # Add random number to sequence
    sequence.append(random.randint(1, 9))
    # Start round
    clear_screen()
    print(f"\n=== Round {current_round} ===")
    print(f"Remember this sequence of {len(sequence)} numbers: ")
    # Show each number
    for num in sequence:
        time.sleep(0.8)
        print(f"\n{num}")
        time.sleep(0.8)
        clear_screen()
    # Ask user to repeat the sequence
    print("\nNow repeat the sequence by typing each number, seperated by spaces:")
    player_answer = input("> ")
    # Convert user answer to a list of numbers
    try:
        player_sequence = [int(num) for num in player_answer.split()]
    except ValueError:
        print("❌ Please enter numbers only!")
        game_over = True
        continue
    # Check for correct sequence
    if player_sequence == sequence:
        print(f"🎉 Congrats! You remembered all {len(sequence)} numbers!")
        current_round += 1
        time.sleep(2)
    else:
        print(f"😭 Game Over! You remembered {current_round - 1} numbers!")
        print(
            f"The correct sequence was: {" ".join(str(num) for num in sequence)}")
        game_over = True
    # Ask if user wants to play again
    if game_over:
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again.startswith("y"):
            # Reset game
            sequence = []
            current_round = 1
            game_over = False
        else:
            print("Thanks for playing! 👋")
