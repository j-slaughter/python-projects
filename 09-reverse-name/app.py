# Reverse Name App: reverses inputted name

print("🔄 REVERSE NAME GENERATOR 🔄")

while True:
    # Get name from user
    name = input("\nEnter a name: ")

    # Check for inputted name
    if not name:
        break

    # Reverse the name
    reversed_name = name[::-1]
    # ALTERNATIVE SOLUTION
    # letters = reversed(list(name))
    # reversed_name = "".join(letters)

    print(f"Your reversed name is: {reversed_name}")
    print(
        f"In a parallel universe, they call you {reversed_name.title()}!")

    # Ask if user wants to continue
    continue_game = input("\nTry another name? (y/n): ").lower()
    if continue_game != "y":
        print(f"Goodbye, {reversed_name.title()}!")
        break
