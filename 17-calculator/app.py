# Calculator app

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

# Main calculation function


def main():
    print("\n=== 🧮 Simple Calculator 🧮 ===")
    print("Select operation:")
    print("1. ➕ Addition\n2. ➖ Subtraction\n3. ✖️  Multiplication\n4. ➗ Division\n")

    # Get operation from user
    while True:
        choice = input("Enter choice (1-4): ")
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid input. Please enter a number between 1 and 4.")
        else:
            break
    # Get numbers from user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Error! Please enter valid numbers.")
        return
    # Perform operation and print result
    if choice == "1":
        print(f"\n{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == "3":
        print(f"\n{num1} x {num2} = {multiply(num1, num2)}")
    elif choice == "4":
        print(f"\n{num1} / {num2} = {divide(num1, num2)}")
    # Ask if user wants to continue
    again = input(
        "\nDo you want to perform another calculation? (yes/no): ").lower()
    if not again.startswith("y"):
        print("Goodbye!")
        return
    else:
        main()


# Run app
main()
