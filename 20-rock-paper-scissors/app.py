# Classic Rock, Paper, Scissors Game
import random
import time


def display_welcome(target_score):
    """Displays rules of the game"""
    print("\n=== ROCK PAPER SCISSORS ===")
    print("\nRules:")
    print("- Rock crushes Scissors")
    print("- Scissors cuts Paper")
    print("- Paper covers Rock")
    print(f"- First to win {target_score} rounds is the champion!")
    print("\n----------------------------")


def get_player_throw():
    """Returns the player's throw as an integer [1.rock, 2.paper, 3.scissors]"""
    while True:
        # Present choices
        print("\nMake your choice:")
        print("1. Rock 🪨\n2. Paper 📄\n3. Scissors ✂️")
        # Get player's throw
        try:
            player_throw = int(input("Enter your choice (1-3): "))
            # Check for valid input
            if 1 <= player_throw <= 3:
                return player_throw
            else:
                print("❌ Error! Please input a number between 1 and 3.")
        except ValueError:
            print("❌ Error! Please input a number between 1 and 3.")


def convert_choice_to_text(choice):
    """Converts integer choice to text [1.Rock, 2.Paper, 3.Scissors]"""
    choices = {1: "Rock 🪨", 2: "Paper 📄", 3: "Scissors ✂️"}
    return choices[choice]


def determine_winner(player_throw, computer_throw):
    """Determine the winner of a single round of rock, paper, scissors"""
    # Tie
    if player_throw == computer_throw:
        print("🤝 It's a tie! Nobody wins this round.")
        return "tie"
    # Player win cases
    elif ((player_throw == 1 and computer_throw == 3) or (player_throw == 2 and computer_throw == 1) or (player_throw == 3 and computer_throw == 2)):
        print("🎉 You win this round!")
        return "player"
    # Computer win
    else:
        print("💻 Computer wins this round!")
        return "computer"


def play_game():
    """Main game function"""
    # Initialize game stats
    current_round = 1
    player_score = 0
    computer_score = 0
    target_score = 3
    # Introduce game and rules
    display_welcome(target_score)

    # Start round
    while player_score < target_score and computer_score < target_score:
        print(f"\n==== Round {current_round} ====")
        print(f"Score: You {player_score} - {computer_score} Computer")
        # Get player's throw
        player_throw = get_player_throw()
        print(f"You chose: {convert_choice_to_text(player_throw)}")
        # Get computer's throw (see bottom of file for alternative)
        print("Computer is choosing...")
        time.sleep(2)
        computer_throw = random.randint(1, 3)
        print(f"Computer chose: {convert_choice_to_text(computer_throw)}")
        # Calculate round winner
        result = determine_winner(player_throw, computer_throw)
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        # Update round
        current_round += 1

    # Game over
    print("\n==== GAME OVER ====")
    print(f"Final Score: You {player_score} - {computer_score} Computer")
    if player_score > computer_score:
        print("Congrats! You are the champion.")
    else:
        print("You lose! Better luck next time.")
    # Play again ?
    play_again = input("Play again? (yes/no): ").lower()
    if play_again.startswith("y"):
        play_game()
    else:
        print("Thanks for playing!")


play_game()

# For alternative computer choosing animation
# print("Computer is choosing", end="")
# for _ in range(3):
# print(".", end="", flush=True)
# time.sleep(0.5)
